# Transfer Ninja Zine

Fall 2027 transfer-cycle field guide: one move per school, a deadline clock, a profile checklist, trackers,
a tutor board with per-school research briefs, a vault of every school on file, and a Common App and
school-questions log. Pizza Ninjas styling from the Robotic Discipline portal.

**Live (Vercel build):** https://transfer-ninja-zine.vercel.app  
**Artifact (claude.ai):** https://claude.ai/artifact/Fef8b37redK5XTqiUYYsxW

Vercel needs `TUTOR_CODE` set as a production environment variable. Redeploy with `cd vercel && vercel deploy --prod --yes`.

## Layout

| Path | What it is |
|---|---|
| `zine.template.html` | The page (HTML, CSS, JS). Data is injected at build time. |
| `data/schools.json` | Source of truth for the 21 active cards: facts, majors, money, study abroad, links. Edit by hand. |
| `data/make_schools.py` | The one-off script that produced `schools.json`. |
| `build_zine.py` | Reads the vault dossiers, research library, spreadsheet and `schools.json`, then writes every output below. |
| `transfer-ninja-zine.html` | Build for the claude.ai artifact. Soft code lock, shared storage for the Common App log. |
| `vercel/` | Build for Vercel. Tutor and admin data stays on the server until the code is checked. |
| `vault/` | Obsidian vault. Open this folder as a vault. One note per school, plus Common App and questions. |
| `.env` | `TUTOR_CODE` (gitignored). |

## Agent and source library

Admin-only (behind the code). On the claude.ai artifact, a source library lets you add folders, files (PDF, TXT, MD,
SRT, VTT, CSV, JSON) or pasted text. An agent chat reads it with tools: `search_sources`, `read_source`,
`analyze_text` (stats, keywords, readability, speaker share), `school_data` and `tracker_status`. It runs on the
viewer's own Claude account through the `sample` capability. Library collections (`folders`, `docs`, `chunks`) are
readable and writable by editors only, so a view-only tutor cannot read your transcripts. On the Vercel build the
library stores in the browser and the agent is off, because it needs the artifact runtime.

## November 10 strategy update

The six former bench-tier schools are active. A separate five-school reserve bench is excluded from the active application count and stats comparison. Unlock the site, then open **Dojo → School strategy** or **Stats and GPA**. School supplement guidance also appears under **Apps → School questions**. The personal record and guidance remain in the gated payload.

`data/strategy.json` contains dated profile evidence, official research, a provisional acceptance-rate-free compatibility order, and five guidance bullets for each supplement inventory item. Missing/current-portal-only requirements are explicitly flagged. The ordinal ranking is an advising judgment, not a prediction. GPA scenarios use editable planning hours and do not change that fixed ranking.

The printable PDF and editable Markdown are in `documents/`. Regenerate with `python3 scripts/export_strategy.py` (requires reportlab). `data/route-plans.json` preserves the prior route snapshot when openpyxl or the original workbook is unavailable.

## Rebuild

```bash
python3 build_zine.py
```

## The code lock

- Tutor board, research briefs, the vault, the Common App log, trackers and backup/reset need the code.
- **Artifact build:** the check runs in the browser against a hash, so it keeps casual viewers out but is not
  security. Anyone who can open the artifact can read its page source.
- **Vercel build:** the gated data is not in the page. `api/unlock.js` returns it only when the posted code
  matches the `TUTOR_CODE` environment variable. A 4-digit code can be guessed, so use a longer one for
  anything sensitive.

## Not in this repo's public pages

Transcripts, GPA, withdrawals, call debriefs and essay drafts are deliberately not read or embedded.
The research briefs and the vault do include contact names and call notes, which is why the repo is private.
