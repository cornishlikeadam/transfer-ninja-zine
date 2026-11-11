#!/usr/bin/env python3
"""Add Penn to data/schools.json and mark the applications not opened yet. Safe to run again.

Penn sources: Kendren's Penn dossier and research library (03_RESEARCH_LIBRARY/schools_17_24.md,
compact_comparison_13_24.md), Penn's transfer requirements page, Penn Today on the Yellow Ribbon
expansion, and a March 2026 Inquirer report on veteran admissions (web search 2026-11-11).
"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(HERE, "schools.json")
d = json.load(open(P, encoding="utf-8"))

REQ = "https://admissions.upenn.edu/how-to-apply/transfer-applicants/requirements-deadlines"
penn = {
    "id": "penn", "name": "Penn", "route": "College of Arts and Sciences transfer", "pri": "core", "talked": 0,
    "one": "Choose the College of Arts and Sciences and one major before you write: Penn locks you into the school you apply to.",
    "facts": [
        "Penn admitted 145 of 4,521 transfer applicants in 2024-25 (3.2%), across all four schools.",
        "At least half the degree must be completed at Penn, and transfer entry is fall only.",
        "Penn required testing in the 2025-26 cycle, with a hardship waiver. Check the 2027 rule.",
    ],
    "next": "Open the application, capture the three Penn essays, decide on testing, and ask Penn how SCAD quarter credits and studio courses are evaluated.",
    "src": REQ,
    "d": [["2027-03-15", "Transfer application (March 15 in the last cycle; confirm 2027)", "x", REQ],
          ["2027-03-20", "Financial aid documents (dossier date; confirm)", "x", "https://srfs.upenn.edu/financial-aid/yellow-ribbon"]],
    "di": "none",
    "fin": {
        "waiver": "Penn waives the application fee for veterans (your research library).",
        "model": "Penn meets full demonstrated need with grant-based aid. Need-blind status for transfer applicants was not confirmed.",
        "aid": "CSS Profile and FAFSA. The dossier lists March 20 for aid documents; confirm for 2027.",
        "vet": "Unlimited undergraduate Yellow Ribbon, and Penn pays tuition the Post-9/11 GI Bill leaves unpaid for 100% eligible veterans admitted to one of the four undergraduate schools.",
        "note": "Admitted transfers generally cannot change undergraduate schools. Supervisor letters can substitute if you have been out of school more than five years."},
    "abroad": "Penn Abroad rules for transfer students were not researched. With half the degree required at Penn, ask Penn Abroad how a semester away fits your residency.",
    "links": [["Transfer requirements and deadlines", REQ],
              ["Transfer writing prompts", "https://admissions.upenn.edu/how-to-apply/preparing-your-application/writing"],
              ["Yellow Ribbon", "https://srfs.upenn.edu/financial-aid/yellow-ribbon"],
              ["Veteran benefits", "https://admissions.upenn.edu/affording-penn/financial-aid/veteran-benefits"],
              ["Supplementary materials", "https://admissions.upenn.edu/how-to-apply/preparing-your-application/supplementary-materials"],
              ["VetLink guidebook page", "https://service2school.gitbook.io/vetlink-guidebook/university-of-pennsylvania"]],
    "opened": False,
}
lens = {
    "di": "none", "diText": "Penn's Common Data Set lists applicant interest as not considered, and no transfer interest factor is published.",
    "path": "College of Arts and Sciences: Africana Studies or Philosophy, Politics and Economics, with Science, Technology and Society as a third option. Not Wharton, not Engineering, not computer science. Confirm your pick.",
    "know": [["Desmond Upton Patton", "Penn Integrates Knowledge professor (Social Policy and Annenberg); directs SAFElab on AI, social media and violence prevention."],
             ["Shiyan Jiang", "Penn GSE; AI, learning, identity and design-based research."]],
    "gap": "No Africana Studies or PPE faculty are researched yet.",
    "res": "SAFElab",
    "evi": "SAFElab found that systems trained on dominant English misread grief in African American English as aggression, and now builds community context into model labels.",
    "who": "Penn transfer admissions and Service to School VetLink.",
    "ask": "For a SCAD transfer applying to the College, which completed courses can be evaluated toward requirements before enrollment, and how should quarter-system studio credits be documented?",
    "show": "Three essays on one through-line, two recent academic recommendations, and a one-page project abstract at most.",
    "dont": "Do not send a portfolio unless you apply to a program that asks for one, and do not ask faculty for favors.",
}

d["schools"] = [s for s in d["schools"] if s["id"] != "penn"] + [penn]
d["lens"]["penn"] = lens
for s in d["schools"]:
    if s["id"] in ("yale", "dartmouth", "penn"):
        s["opened"] = False
json.dump(d, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("schools:", len(d["schools"]), "| not opened:", [s["id"] for s in d["schools"] if s.get("opened") is False])
