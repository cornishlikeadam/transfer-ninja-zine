#!/usr/bin/env python3
"""Build the Transfer Ninja Zine from the research that lives on this computer.

Reads (read-only):
  - Vault dossiers:   Transfer Admissions HQ 1/01 - Target Schools/**/*.md
  - Research library: Desktop/2025:2026 Universe/Kendren_Transfer_Admissions_Master_Packet/
                      (schools_*.md, online_presence_and_supplement_matrix.md, CONNECTIONS_MAP.md)
  - Route plans:      Downloads/SCAD_Transfer_Execution_2027.xlsx

Writes:
  - data/zine-data.json           (the extracted research, for inspection)
  - transfer-ninja-zine.html      (claude.ai artifact build, soft code lock)
  - vercel/                       (Vercel build: tutor/admin data served only after the code is checked)
  - vault/                        (Obsidian vault: one note per school, Common App and questions)

Deliberately NOT read or embedded: transcripts, GPA figures, call debriefs, essay drafts,
personal odds on the public page. Private strategy is behind the existing code. The page is meant to be shared with a tutor, not to expose the record.

Run:  python3 build_zine.py   (needs TUTOR_CODE in .env)
"""
import csv, glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
VAULT = os.environ.get("ADMISSIONS_VAULT", "/Users/kjcornish/Downloads/New Folder With Items/Transfer Admissions HQ 1")
HOME = os.path.expanduser("~")
PACKET = os.path.join(HOME, "Desktop", "2025:2026 Universe", "Kendren_Transfer_Admissions_Master_Packet")
XLSX = os.path.join(HOME, "Downloads", "SCAD_Transfer_Execution_2027.xlsx")

# library heading -> id
LIB_IDS = [
    ("Michigan", "michigan"), ("Notre Dame", "nd"), ("Emory", "emory"), ("Southern California", "usc"),
    ("Vanderbilt", "vandy"), ("School of General Studies", "columbia"), ("George Washington", "gwu"), ("Washington University", "washu"),
    ("Virginia", "uva"), ("Cornell", "cornell"), ("Northeastern", "northeastern"), ("Yale", "yale"),
    ("Brown", "brown"), ("Princeton", "princeton"), ("Southern Methodist", "smu"), ("Case Western", "case"),
    ("Morehouse", "morehouse"), ("Tufts", "tufts"), ("Howard", "howard"), ("Pennsylvania", "penn"),
    ("New York University", "nyu"), ("Miami", "miami"), ("Texas at Austin", "utaustin"),
    ("Illinois", "uiuc"), ("Florida", "florida"), ("Rice", "rice"), ("Dartmouth", "dartmouth"),
    ("Johns Hopkins", "jhu"), ("North Carolina", "unc"), ("Tulane", "tulane"),
    ("Georgia", "uga"), ("Chicago", "uchicago"), ("Northwestern", "nu"),
]
# library order (the matrix numbers 1..33 follow the same order as the DI strategy index)
MATRIX_ORDER = ["michigan", "nd", "emory", "usc", "vandy", "columbia", "washu", "uva", "cornell", "northeastern",
                "yale", "brown", "princeton", "smu", "case", "morehouse", "howard", "penn", "nyu", "miami",
                "utaustin", "uiuc", "florida", "rice", "dartmouth", "jhu", "unc", "tulane", "gwu", "uga",
                "uchicago", "nu", "tufts"]

DOSSIER_IDS = [
    ("Brown", "brown"), ("Columbia", "columbia"), ("Cornell", "cornell"), ("Dartmouth", "dartmouth"),
    ("Harvard", "harvard"), ("Princeton", "princeton"), ("Pennsylvania", "penn"), ("Yale", "yale"),
    ("Carnegie", "cmu"), ("Duke", "duke"), ("Emory", "emory"), ("Georgetown", "gt"), ("Johns Hopkins", "jhu"),
    ("Massachusetts Institute", "mit"), ("New York University", "nyu"), ("Northeastern", "northeastern"),
    ("Northwestern", "nu"), ("Rice", "rice"), ("Southern Methodist", "smu"), ("Stanford", "stanford"),
    ("Texas Christian", "tcu"), ("Tufts", "tufts"), ("Tulane", "tulane"), ("Chicago", "uchicago"),
    ("Miami", "miami"), ("Notre Dame", "nd"), ("Southern California", "usc"), ("Vanderbilt", "vandy"),
    ("Washington University", "washu"), ("UC Berkeley", "berkeley"), ("UCLA", "ucla"),
    ("UNC", "unc"), ("Georgia (UGA)", "uga"), ("Illinois", "uiuc"), ("Michigan", "michigan"),
    ("Virginia", "uva"), ("Amherst", "amherst"), ("Bowdoin", "bowdoin"), ("Caltech", "caltech"),
    ("CalArts", "calarts"), ("Swarthmore", "swarthmore"), ("Williams", "williams"),
]


def idfor(name, table):
    for key, i in table:
        if key.lower() in name.lower():
            return i
    return None


def de_md(s):
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r"\1 \2", s)
    return re.sub(r"[`*]", "", s)


def clean_md(s):
    s = re.sub(r"\[([^\]]+)\]\((?:https?://[^)]*)\)", r"\1", s)
    return re.sub(r"[`*]", "", s).strip()


# ---------- research library ----------
def parse_library():
    out = {}
    for f in ["schools_01_08", "schools_09_16", "schools_17_24", "schools_25_32"]:
        path = os.path.join(PACKET, "03_RESEARCH_LIBRARY", f + ".md")
        text = open(path, encoding="utf-8").read()
        for part in re.split(r"^## ", text, flags=re.M)[1:]:
            head, _, body = part.partition("\n")
            title = re.sub(r"^\d+\.\s*", "", head).strip()
            sid = idfor(title, LIB_IDS)
            if not sid:
                print("WARN no id for library entry:", title, file=sys.stderr)
                continue
            m_act = re.search(r"^Actions[^\n]*:\s*$", body, re.M)
            m_lnk = re.search(r"^Official links[^\n]*:\s*$", body, re.M)
            end_prose = m_act.start() if m_act else (m_lnk.start() if m_lnk else len(body))
            prose = body[:end_prose]
            acts, links = [], []
            if m_act:
                seg = body[m_act.end(): (m_lnk.start() if m_lnk else len(body))]
                acts = [re.sub(r"^\d+\.\s*", "", l).strip() for l in seg.split("\n") if re.match(r"^\d+\.", l.strip())]
            if m_lnk:
                links = [l.strip()[2:].strip() for l in body[m_lnk.end():].split("\n") if l.strip().startswith("- ")]
            paras = [de_md(p.strip()) for p in prose.split("\n\n") if p.strip()]
            out[sid] = {"title": title, "paras": paras, "actions": [de_md(a) for a in acts], "links": [de_md(l) for l in links]}
    return out


def classify_di(paras, sid=""):
    """Labels: none = school says interest is not tracked/counted; counts = school says it counts;
    firstyear = first-year data counts it but no transfer rule is published; ted = binding transfer
    early decision is the only legit signal; ask = unclear, ask once."""
    txt = " ".join(paras)
    sents = re.split(r"(?<=[.!?])\s+", txt)

    def first(pattern):
        for st in sents:
            if re.search(pattern, st, re.I):
                return st.strip()[:420]
        return ""

    if sid in ("nu", "uchicago"):
        return "ted", first(r"(TED|transfer early decision|interest)") or "Transfer Early Decision is the strongest legitimate interest signal, and it is binding."
    none_pat = (r"(does not track|do not track|not track|Not Considered|does not consider|no published (transfer )?interest|"
                r"no comparable interest factor|not a school where|interest-driven|no basis for treating)")
    st = first(none_pat)
    if st:
        return "none", st
    st = first(r"(says demonstrated interest is a factor|considers[^.]{0,120}interest in the university)")
    if st:
        return "counts", st
    st = first(r"(first-year|first-time)[^.]{0,120}interest|interest[^.]{0,160}(first-year|first-time)")
    if st:
        return "firstyear", st
    st = first(r"(demonstrated interest)")
    return "ask", st or "No published transfer interest rule found in the research. Ask once."


def parse_matrix():
    path = os.path.join(PACKET, "03_RESEARCH_LIBRARY", "online_presence_and_supplement_matrix.md")
    text = open(path, encoding="utf-8").read()
    rows = {}
    for r in text.split("\n"):
        if not re.match(r"^\|\s*\d+\s*\|", r):
            continue
        c = [x.strip() for x in r.strip().strip("|").split("|")]
        n = int(c[0])
        if len(c) >= 7 and 1 <= n <= len(MATRIX_ORDER):
            rows[MATRIX_ORDER[n - 1]] = {"channel": clean_md(c[3])[:520], "safest": clean_md(c[6])[:620], "name": clean_md(c[1])[:80]}
    return rows


# ---------- vault dossiers ----------
def parse_dossiers():
    out = {}
    for p in glob.glob(os.path.join(VAULT, "01 - Target Schools", "*", "*", "*.md")):
        folder = os.path.basename(os.path.dirname(p))
        sid = idfor(folder, DOSSIER_IDS)
        if not sid:
            print("WARN no id for dossier:", folder, file=sys.stderr)
            continue
        t = open(p, encoding="utf-8").read()
        fm = re.search(r"^---\n(.*?)\n---", t, re.S)
        d = {}
        if fm:
            for line in fm.group(1).split("\n"):
                m = re.match(r'^(\w+):\s*"?(.*?)"?\s*$', line)
                if m:
                    d[m.group(1)] = m.group(2)
        anchors = ""
        m = re.search(r"Core Campus Anchor:\*\*\s*(.+)", t)
        if m:
            anchors = clean_md(m.group(1))
        di = re.search(r"Demonstrated Interest Policy:\s*(.+)", t)
        wg = re.search(r"Winter Grade Treatment:\s*(.+)", t)
        out[sid] = {
            "folder": folder,
            "route": d.get("route", ""), "major": d.get("intended_major", ""),
            "deadline": d.get("application_deadline", ""), "aid": d.get("financial_aid_deadline", ""),
            "testing": d.get("standardized_testing", ""), "vet": d.get("veteran_friendly", ""),
            "yr": d.get("yellow_ribbon", ""), "portal": d.get("portal", ""), "url": d.get("official_url", ""),
            "anchors": anchors, "di": clean_md(di.group(1))[:300] if di else "",
            "winter": clean_md(wg.group(1))[:300] if wg else "",
        }
    return out


# ---------- connections map ----------
def parse_connections():
    path = os.path.join(PACKET, "00_START_HERE", "CONNECTIONS_MAP.md")
    text = open(path, encoding="utf-8").read()
    rows = []
    for r in text.split("\n"):
        if r.startswith("|") and not r.startswith("|---") and not r.startswith("| Profile evidence"):
            c = [x.strip() for x in r.strip().strip("|").split("|")]
            if len(c) >= 4:
                rows.append({"evidence": c[0], "question": c[1], "schools": c[2], "use": c[3]})
    return rows


# ---------- route plans (xlsx) ----------
def parse_routes():
    try:
        import openpyxl
    except ImportError:
        print("INFO openpyxl missing: using preserved route-plan snapshot", file=sys.stderr)
        return json.load(open(os.path.join(HERE, "data", "route-plans.json"), encoding="utf-8"))
    if not os.path.exists(XLSX):
        return json.load(open(os.path.join(HERE, "data", "route-plans.json"), encoding="utf-8"))
    ws = openpyxl.load_workbook(XLSX, data_only=True)["School Plans"]
    rows = [r for r in ws.iter_rows(values_only=True) if any(c is not None for c in r)]
    head = [str(c) for c in rows[0]]
    ix = {h: i for i, h in enumerate(head)}

    def g(r, k, n=300):
        v = r[ix[k]] if k in ix and ix[k] < len(r) else None
        return str(v).strip()[:n] if v is not None else ""

    out = []
    for r in rows[1:]:
        name = g(r, "University / Route", 120)
        if not name:
            continue
        out.append({
            "name": name, "type": g(r, "Route Type"), "degree": g(r, "Recommended Degree"),
            "second": g(r, "Secondary Degree"), "basis": g(r, "Review Basis"),
            "condition": g(r, "Key Condition", 360), "deadline": g(r, "Official / Planning Deadline"),
            "confidence": g(r, "Deadline Confidence"), "portfolio": g(r, "Portfolio Requirement"),
            "aid": g(r, "Aid / Tuition Outlook", 360), "credit": g(r, "Transfer-Credit Reality", 360),
            "next": g(r, "Immediate Next Action", 360), "src": g(r, "Primary Official Source", 200),
        })
    return out


def load_env():
    env = {}
    p = os.path.join(HERE, ".env")
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip()
    if os.environ.get("TUTOR_CODE"):
        env["TUTOR_CODE"] = os.environ["TUTOR_CODE"]
    return env


CYRB = ("function cyrb53(str){var h1=0xdeadbeef,h2=0x41c6ce57;for(var i=0,ch;i<str.length;i++){ch=str.charCodeAt(i);"
        "h1=Math.imul(h1^ch,2654435761);h2=Math.imul(h2^ch,1597334677)}h1=Math.imul(h1^(h1>>>16),2246822507)^"
        "Math.imul(h2^(h2>>>13),3266489909);h2=Math.imul(h2^(h2>>>16),2246822507)^Math.imul(h1^(h1>>>13),3266489909);"
        "return 4294967296*(2097151&h2)+(h1>>>0)}")


def code_hash(code):
    import subprocess
    r = subprocess.run(["node", "-e", CYRB + ";console.log(cyrb53(process.argv[1]))", "tn:" + code],
                       capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit("node is needed to compute the code hash: " + r.stderr)
    return r.stdout.strip()


FULL_HEAD = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
             '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
             '<meta name="robots" content="noindex,nofollow">'
             '<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}'
             'body{margin:0;font:14px system-ui}img{max-width:100%}[hidden]{display:none!important}</style></head><body>')


def slug(name):
    return re.sub(r"[^A-Za-z0-9 ._-]", "", name).strip()


def write_vault(schools, lens, lib, dossier):
    root = os.path.join(HERE, "vault")
    for sub in ("Schools", "Application Questions", "Common App", ".obsidian"):
        os.makedirs(os.path.join(root, sub), exist_ok=True)
    open(os.path.join(root, ".obsidian", "app.json"), "w").write("{}\n")
    links = []
    for s in schools:
        L = lens.get(s["id"], {})
        n = slug(s["name"])
        links.append("- [[Schools/%s|%s]] (%s)" % (n, s["name"], s["pri"]))
        md = ["---", "school: %s" % s["name"], "id: %s" % s["id"], "route: %s" % s["route"], "priority: %s" % s["pri"],
              "interest_policy: %s" % s.get("di", ""), "deadlines:"]
        md += ["  - %s: %s" % (d[0], d[1]) for d in s["d"]]
        md += ["tags: [school, transfer-2027]", "---", "# %s" % s["name"], "", "**Route:** %s" % s["route"], "",
               "> The one thing: %s" % s["one"], ""]
        if s.get("gate"):
            md += ["**Gate:** %s" % s["gate"], ""]
        md += ["## Facts"] + ["- %s" % f for f in s["facts"]] + ["", "## Next move", s["next"], ""]
        md += ["## Fit (the real degree path)", L.get("path", ""), ""]
        if L.get("know"):
            md += ["## People and research to know (anchors, not contacts)"] + ["- **%s.** %s" % (k[0], k[1]) for k in L["know"]] + [""]
        if L.get("gap"):
            md += ["> Gap: %s" % L["gap"], ""]
        md += ["## Interest", L.get("diText", ""), "", "## Connect", "**Who:** %s" % L.get("who", ""), "",
               "**Question to ask:** %s" % L.get("ask", ""), "", "## Show your knowledge (RECAP)",
               "- Resource: %s" % L.get("res", ""), "- Evidence: %s" % L.get("evi", ""), "- Connection:", "- Application:", "- Proof:", "",
               "**Show:** %s" % L.get("show", ""), "", "**Avoid:** %s" % L.get("dont", ""), ""]
        f = s.get("fin", {})
        md += ["## Money", "- **Application fee:** %s" % f.get("waiver", ""), "- **Aid model:** %s" % f.get("model", ""),
               "- **Aid forms and dates:** %s" % f.get("aid", ""), "- **Veterans benefits:** %s" % f.get("vet", "")]
        if f.get("note"):
            md += ["- **Note:** %s" % f["note"]]
        md += ["", "## Study abroad", s.get("abroad", ""), "", "## Links"]
        md += ["- [%s](%s)" % (l[0], l[1]) for l in s.get("links", [])]
        lb = lib.get(s["id"])
        if lb and lb.get("actions"):
            md += ["", "## Steps from the research (written July 2026)"] + ["%d. %s" % (i + 1, a) for i, a in enumerate(lb["actions"])]
        md += ["", "## Application questions", "See [[Application Questions/%s Questions]].".replace("%s", n), "", "## My notes", ""]
        open(os.path.join(root, "Schools", n + ".md"), "w", encoding="utf-8").write("\n".join(md))
        q = ["---", "school: %s" % s["name"], "tags: [questions]", "---", "# %s questions" % s["name"], "",
             "Paste each prompt from the application. Write the answer yourself.", "",
             "| Prompt | Limit | Status | Draft |", "|---|---|---|---|", "| | | Not started | |", "",
             "Back to [[Schools/%s]]." % n]
        qp = os.path.join(root, "Application Questions", n + " Questions.md")
        if not os.path.exists(qp):
            open(qp, "w", encoding="utf-8").write("\n".join(q))
    ca = ["---", "tags: [common-app]", "---", "# Common App entries", "",
          "Limits are starting values. Set each from your application screenshots.", "",
          "## Writing", "- [ ] Personal essay (650 words)", "- [ ] Reasons for transferring (650 words)", "- [ ] Additional information (650 words)",
          "", "## Activities (up to 10, description 150 characters)"] + ["- [ ] Activity %d" % i for i in range(1, 11)] + \
         ["", "## Honors (up to 5, title 100 characters)"] + ["- [ ] Honor %d" % i for i in range(1, 6)] + \
         ["", "## Notes", "- Education history", "- Testing"]
    cp = os.path.join(root, "Common App", "Common App Entries.md")
    if not os.path.exists(cp):
        open(cp, "w", encoding="utf-8").write("\n".join(ca))
    home = ["# Transfer Ninja Zine vault", "", "Fall 2027 transfer cycle. One note per school, plus the Common App and school questions.",
            "", "## Schools"] + links + ["", "## Common App", "- [[Common App/Common App Entries]]", "",
            "Generated by `build_zine.py`. Notes you edit in Obsidian are not overwritten when only the Application Questions and Common App files already exist; school notes are regenerated, so keep your own writing in the My notes section of a copy or in the question files."]
    open(os.path.join(root, "Home.md"), "w", encoding="utf-8").write("\n".join(home))


def main():
    env = load_env()
    code = env.get("TUTOR_CODE")
    if not code:
        raise SystemExit("Set TUTOR_CODE in .env")
    sj = json.load(open(os.path.join(HERE, "data", "schools.json"), encoding="utf-8"))
    lib = parse_library()
    for sid, e in lib.items():
        e["di"], e["diText"] = classify_di(e["paras"], sid)
    matrix = parse_matrix()
    for sid, m in matrix.items():
        if sid in lib:
            lib[sid]["channel"], lib[sid]["safest"] = m["channel"], m["safest"]
    gated = {"lib": lib, "dossier": parse_dossiers(), "routes": parse_routes(),
             "connections": parse_connections(), "lens": sj["lens"],
             "strategy": json.load(open(os.path.join(HERE, "data", "strategy.json"), encoding="utf-8"))}
    pub = {"schools": sj["schools"], "bench": sj["bench"]}
    os.makedirs(os.path.join(HERE, "data"), exist_ok=True)
    json.dump(gated, open(os.path.join(HERE, "data", "zine-data.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    tpl = open(os.path.join(HERE, "zine.template.html"), encoding="utf-8").read()

    def dump(o):
        return json.dumps(o, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")

    empty = {"lib": {}, "dossier": {}, "routes": [], "connections": [], "lens": {}}
    soft = tpl.replace("/*__DATA__*/", "var GATE_MODE='soft';var CODEHASH=%s;var PUB=%s;var DATA=%s;" % (code_hash(code), dump(pub), dump(gated)))
    open(os.path.join(HERE, "transfer-ninja-zine.html"), "w", encoding="utf-8").write(soft)

    server = tpl.replace("/*__DATA__*/", "var GATE_MODE='server';var CODEHASH=0;var PUB=%s;var DATA=%s;" % (dump(pub), dump(empty)))
    vdir = os.path.join(HERE, "vercel")
    os.makedirs(os.path.join(vdir, "public"), exist_ok=True)
    os.makedirs(os.path.join(vdir, "api"), exist_ok=True)
    open(os.path.join(vdir, "public", "index.html"), "w", encoding="utf-8").write(FULL_HEAD + server + "</body></html>")
    json.dump(gated, open(os.path.join(vdir, "gated.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    open(os.path.join(vdir, "api", "unlock.js"), "w").write(UNLOCK_JS)
    open(os.path.join(vdir, "vercel.json"), "w").write(json.dumps({"headers": [{"source": "/(.*)", "headers": [{"key": "X-Robots-Tag", "value": "noindex"}]}]}, indent=1))
    write_vault(sj["schools"], sj["lens"], lib, gated["dossier"])
    print("schools:", len(sj["schools"]), "| library:", len(lib), "| dossiers:", len(gated["dossier"]), "| routes:", len(gated["routes"]),
          "| artifact bytes:", len(soft), "| vercel page bytes:", len(server))


UNLOCK_JS = """const crypto = require('crypto');
const gated = require('../gated.json');

function same(a, b) {
  const x = Buffer.from(String(a)), y = Buffer.from(String(b));
  return x.length === y.length && crypto.timingSafeEqual(x, y);
}

module.exports = async (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  if (req.method !== 'POST') { res.status(405).json({ ok: false }); return; }
  let body = req.body;
  if (typeof body === 'string') { try { body = JSON.parse(body); } catch (e) { body = {}; } }
  const code = String((body && body.code) || '').trim();
  const expected = String(process.env.TUTOR_CODE || '');
  await new Promise((r) => setTimeout(r, 600));
  if (expected && same(code, expected)) { res.status(200).json({ ok: true, data: gated }); }
  else { res.status(401).json({ ok: false }); }
};
"""


if __name__ == "__main__":
    main()
