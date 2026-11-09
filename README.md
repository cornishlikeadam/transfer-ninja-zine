# Transfer Ninja Zine

Fall 2027 transfer-cycle field guide: one move per school, a deadline clock, a profile checklist, trackers,
a tutor board with per-school research briefs, a vault of every school on file, and a Common App and
school-questions log. Pizza Ninjas styling from the Robotic Discipline portal.

## Layout

| Path | What it is |
|---|---|
| `zine.template.html` | The page (HTML, CSS, JS). Data is injected at build time. |
| `data/schools.json` | Source of truth for the 15 active cards: facts, majors, money, study abroad, links. Edit by hand. |
| `data/make_schools.py` | The one-off script that produced `schools.json`. |
| `build_zine.py` | Reads the vault dossiers, research library, spreadsheet and `schools.json`, then writes every output below. |
| `transfer-ninja-zine.html` | Build for the claude.ai artifact. Soft code lock, shared storage for the Common App log. |
| `vercel/` | Build for Vercel. Tutor and admin data stays on the server until the code is checked. |
| `vault/` | Obsidian vault. Open this folder as a vault. One note per school, plus Common App and questions. |
| `.env` | `TUTOR_CODE` (gitignored). |

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
