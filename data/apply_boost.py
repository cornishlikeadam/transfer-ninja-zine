#!/usr/bin/env python3
"""Merge the reviewed profile, school summaries, ranking and supplement guidance into data/strategy.json.

Keeps ChatGPT's official-research ledger and GPA baseline. Replaces the profile, per-school text,
the ranking and every supplement entry. Safe to run again.

Run:  python3 data/add_penn.py && python3 data/apply_boost.py && python3 build_zine.py
"""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import boost_core as C
import boost_supps1  # noqa: F401  (registers the first half)
import boost_supps2 as S2
import record as R
import military as MIL

P = os.path.join(HERE, "strategy.json")
st = json.load(open(P, encoding="utf-8"))
schools = json.load(open(os.path.join(HERE, "schools.json"), encoding="utf-8"))["schools"]
ids = [s["id"] for s in schools]

st["updated"] = "2026-11-11"
st["method"] = C.METHOD
st["inventoryNote"] = C.INVENTORY
st["whatMoves"] = C.WHAT_MOVES
st["profile"] = C.PROFILE
st["benchSupplement"] = S2.BENCH_SUPP
st["record"] = R.record()
st["military"] = MIL.military()

problems = []
for sid in ids:
    new = C.S.get(sid)
    if not new:
        problems.append("no core entry for " + sid)
        continue
    old = st["schools"].get(sid, {})
    gate = old.get("gate") or re.sub(r"^Academic gate:\s*", "", (old.get("bullets") or ["", "", ""])[2])
    sup = []
    for i, q in enumerate(S2.Q.get(sid, []), 1):
        q = dict(q)
        q["id"] = "%s-%d" % (sid, i)
        sup.append(q)
    if not sup:
        problems.append("no supplements for " + sid)
    n_sent = len(re.findall(r"[.!?](?:\s|$)", new["summary"]))
    if n_sent != 2:
        problems.append("%s summary has %d sentences" % (sid, n_sent))
    st["schools"][sid] = {"path": new["path"], "summary": new["summary"], "bullets": new["bullets"],
                          "gate": gate, "rank": new["rank"], "rankReason": new["rankReason"],
                          "stat": new["stat"], "portal": new["portal"],
                          "source": old.get("source", ""), "supplements": sup}

ranks = sorted(st["schools"][s]["rank"] for s in ids)
if ranks != list(range(1, len(ids) + 1)):
    problems.append("ranks are not 1..%d: %s" % (len(ids), ranks))
for sid in ids:
    if sid not in st["military"]["schools"]:
        problems.append("no military entry for " + sid)
for sid in ids:
    x = st["schools"][sid]
    if len(x["bullets"]) != 3:
        problems.append(sid + " bullets")
    for q in x["supplements"]:
        if len(q["guidance"]) != 5:
            problems.append(q["id"] + " guidance count")
text = json.dumps(st, ensure_ascii=False)
if "—" in text.split('"research"')[0]:
    problems.append("em dash in authored text")

if problems:
    print("PROBLEMS:\n - " + "\n - ".join(problems))
    sys.exit(1)
json.dump(st, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
total = sum(len(st["schools"][s]["supplements"]) for s in ids)
print("ok: %d schools, %d supplement entries, %d guidance points, %d profile sections"
      % (len(ids), total, total * 5, len(st["profile"])))
