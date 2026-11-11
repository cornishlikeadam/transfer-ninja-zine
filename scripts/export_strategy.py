#!/usr/bin/env python3
"""Write the strategy document: best approaches, standouts, reasons and the stats-only ranking.

Reads data/strategy.json and data/schools.json.
Writes documents/Kendren_<N>_School_Strategy.md and .pdf (N = number of schools).

Run:  python3 scripts/export_strategy.py
"""
import html, json, pathlib
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Table, TableStyle

R = pathlib.Path(__file__).resolve().parents[1]
A = json.loads((R / "data/strategy.json").read_text(encoding="utf-8"))
D = json.loads((R / "data/schools.json").read_text(encoding="utf-8"))
out = R / "documents"
out.mkdir(exist_ok=True)
ranked = sorted(D["schools"], key=lambda s: A["schools"][s["id"]]["rank"])
research = {r["id"]: r for r in A["research"]["schools"]}
N = len(D["schools"])
NAME = "Kendren_%d_School_Strategy" % N
MIL = A.get("military", {})
REC = A.get("record", {})
U = {"campus": "On campus", "cross": "Cross-town", "unclear": "Unclear", "none": "None"}


def gpa(pred):
    p = h = 0.0
    for c in REC.get("courses", []):
        if c["grade"] in REC["gp"] and pred(c):
            hh = c["cr"] * (2 / 3 if c["unit"] == "QH" else 1)
            p += REC["gp"][c["grade"]] * hh
            h += hh
    return "%.2f" % (int(p / h * 100 + 1e-9) / 100) if h else "n/a"


fin = lambda c: c["status"] == "final"
GPA_ROWS = [["Broward, as the transcript shows", gpa(lambda c: fin(c) and c["inst"] == "Broward")],
            ["SCAD, as the transcript shows", gpa(lambda c: fin(c) and c["inst"] == "SCAD")],
            ["All colleges pooled", gpa(fin)],
            ["Pooled, developmental course dropped", gpa(lambda c: fin(c) and not c["code"].startswith("ENC0"))],
            ["SCAD with Fall 2026 midterms", gpa(lambda c: c["status"] != "registered" and c["inst"] == "SCAD")],
            ["Pooled with Fall 2026 midterms", gpa(lambda c: c["status"] != "registered")]]

# ------------------------------------------------------------------ markdown
L = ["# Kendren Cornish: %d-school transfer strategy" % N, "", "Best approaches, standouts, reasons and a stats-only ranking.",
     "Updated " + A["updated"], "", "## How to read the ranking", A["method"], "", A["inventoryNote"], "",
     "## Stats-only ranking, acceptance rates set aside", "", "| # | School | Published line and your numbers |", "|---|---|---|"]
for s in ranked:
    x = A["schools"][s["id"]]
    L.append("| %d | %s | %s |" % (x["rank"], s["name"], x["stat"]))
L += ["", "### What would move this order"] + ["- " + b for b in A.get("whatMoves", [])]
L += ["", "## About you"]
for p in A["profile"]:
    L += ["", "### " + p["title"], p["text"], "", "Source: " + p["source"]]
if REC:
    L += ["", "## Academic record", "_" + REC["source"] + "_", ""] + ["- %s: %s" % tuple(r) for r in GPA_ROWS]
    L += ["", "| Term | Course | Credit | Grade |", "|---|---|---|---|"]
    L += ["| %s %s | %s %s | %s %s | %s |" % (c["inst"], c["term"], c["code"], c["title"], c["cr"], c["unit"], (c["grade"] or "registered") + ("" if fin(c) else " (" + c["status"] + ")")) for c in REC["courses"]]
    L += ["", "### Military record"] + ["- " + x for x in REC["service"]["lines"]] + ["", "### Check before you write about service"] + ["- " + x for x in REC["service"]["flags"]]
    L += ["", "### Timeline"] + ["- **%s** %s (%s)" % tuple(t) for t in REC["timeline"]]
if MIL:
    r_ = MIL["rules"]
    L += ["", "## Military and ROTC: the rules for you", r_["summary"], ""] + ["- " + x for x in r_["you"]]
    for br in r_["branches"]:
        L += ["", "### %s: %s" % (br["branch"], br["verdict"]), "- Age: " + br["age"], "- Prior service: " + br["prior"], "- Gate: " + br["gate"], "- " + br["extra"]]
    L += ["", "### Money and obligations"] + ["- " + x for x in r_["money"]]
L += ["", "## School by school, in ranking order"]
for s in ranked:
    x = A["schools"][s["id"]]
    r = research.get(s["id"])
    L += ["", "## %d. %s" % (x["rank"], s["name"]), "*" + x["path"] + "*", "", x["summary"], ""]
    L += ["- " + b for b in x["bullets"]]
    L += ["", "**Why it sits at %d of %d:** %s" % (x["rank"], N, x["rankReason"]), "", "**Numbers:** " + x["stat"]]
    ml = MIL.get("schools", {}).get(s["id"])
    if ml:
        L += ["", "### Military and ROTC", "- Army: %s. %s" % (U[ml["army"][0]], ml["army"][1]), "- Air Force: %s. %s" % (U[ml["af"][0]], ml["af"][1]),
              "- Navy: %s. %s" % (U[ml["navy"][0]], ml["navy"][1]), "", "**Projection:** " + ml["projection"], "", "**Unique:** " + ml["unique"], "", "**Veteran side:** " + ml["vets"]]
    if x.get("gate"):
        L += ["", "**Check first:** " + x["gate"]]
    if x.get("portal"):
        L += ["", "**In your portal now:** " + x["portal"]]
    if r:
        L += ["", "### Official research, checked " + r["verifiedDate"]] + ["- " + f for f in r["findings"]]
        L += ["", "Limits of this research: " + r["limitations"], "", "Source: " + r["source"]]
    L += ["", "### Supplements: %d" % len(x["supplements"])]
    for q in x["supplements"]:
        L += ["", "#### " + q["title"], "%s. %s" % (q["limit"], q["status"]), "", "Prompt, paraphrased: " + q["prompt"], ""]
        L += ["- " + g for g in q["guidance"]]
        L += ["", "_" + q["provenance"] + "_"]
L += ["", "## Reserve bench"]
for b in D["bench"]:
    L += ["- **%s:** %s" % (b["name"], b["one"])]
b = A["benchSupplement"]
L += ["", "### %s: %s" % (b["school"], b["title"]), "%s. %s" % (b["limit"], b["status"]), "", "Prompt, paraphrased: " + b.get("prompt", ""), ""]
L += ["- " + g for g in b["guidance"]]
(out / (NAME + ".md")).write_text("\n".join(L) + "\n", encoding="utf-8")

# ------------------------------------------------------------------ pdf
ss = getSampleStyleSheet()
INK = colors.HexColor("#141413")
body = ParagraphStyle("body", parent=ss["BodyText"], fontName="Helvetica", fontSize=9.5, leading=13.5, textColor=INK, spaceAfter=5)
small = ParagraphStyle("small", parent=body, fontSize=8, leading=11, textColor=colors.HexColor("#5b564c"))
h1 = ParagraphStyle("h1", parent=ss["Title"], fontName="Helvetica-Bold", fontSize=22, leading=26, textColor=INK, alignment=0, spaceAfter=4)
h2 = ParagraphStyle("h2", parent=ss["Heading2"], fontName="Helvetica-Bold", fontSize=15, leading=19, textColor=INK, spaceBefore=10, spaceAfter=4)
h3 = ParagraphStyle("h3", parent=ss["Heading3"], fontName="Helvetica-Bold", fontSize=11, leading=14, textColor=colors.HexColor("#b83300"), spaceBefore=8, spaceAfter=3)
h4 = ParagraphStyle("h4", parent=ss["Heading4"], fontName="Helvetica-Bold", fontSize=10, leading=13, textColor=INK, spaceBefore=6, spaceAfter=2)
bul = ParagraphStyle("bul", parent=body, leftIndent=12, bulletIndent=2, spaceAfter=2)
cell = ParagraphStyle("cell", parent=body, fontSize=8.5, leading=11.5, spaceAfter=0)


def e(t):
    return html.escape(str(t))


def P(t, st=body):
    return Paragraph(e(t), st)


def B(t):
    return Paragraph(e(t), bul, bulletText="•")


story = [Paragraph("Kendren Cornish: %d-school transfer strategy" % N, h1),
         P("Best approaches, standouts, reasons and a stats-only ranking. Updated " + A["updated"] + ".", small),
         Paragraph("How to read the ranking", h2), P(A["method"]), P(A["inventoryNote"], small),
         Paragraph("Stats-only ranking, acceptance rates set aside", h2)]
rows = [[Paragraph("<b>#</b>", cell), Paragraph("<b>School</b>", cell), Paragraph("<b>Published line and your numbers</b>", cell)]]
for s in ranked:
    x = A["schools"][s["id"]]
    rows.append([Paragraph(str(x["rank"]), cell), Paragraph("<b>%s</b>" % e(s["name"]), cell), Paragraph(e(x["stat"]), cell)])
t = Table(rows, colWidths=[0.35 * inch, 1.45 * inch, 5.2 * inch], repeatRows=1)
t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#ffd400")), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                       ("LINEBELOW", (0, 0), (-1, -1), 0.4, colors.HexColor("#b8b09c")), ("BOX", (0, 0), (-1, -1), 1, INK),
                       ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
story += [t, Paragraph("What would move this order", h3)] + [B(b_) for b_ in A.get("whatMoves", [])]
story += [PageBreak(), Paragraph("About you", h2)]
for p in A["profile"]:
    story += [Paragraph(e(p["title"]), h3), P(p["text"]), P("Source: " + p["source"], small)]
if REC:
    story += [PageBreak(), Paragraph("Academic record", h2), P(REC["source"], small)] + [B("%s: %s" % tuple(r)) for r in GPA_ROWS]
    rows2 = [[Paragraph("<b>Term</b>", cell), Paragraph("<b>Course</b>", cell), Paragraph("<b>Credit</b>", cell), Paragraph("<b>Grade</b>", cell)]]
    for c in REC["courses"]:
        rows2.append([Paragraph(e(c["inst"] + " " + c["term"]), cell), Paragraph(e(c["code"] + " " + c["title"]), cell), Paragraph("%s %s" % (c["cr"], c["unit"]), cell),
                      Paragraph(e((c["grade"] or "registered") + ("" if fin(c) else " (" + c["status"] + ")")), cell)])
    t2 = Table(rows2, colWidths=[1.35 * inch, 3.85 * inch, 0.7 * inch, 1.1 * inch], repeatRows=1)
    t2.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#ffd400")), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                            ("LINEBELOW", (0, 0), (-1, -1), 0.4, colors.HexColor("#b8b09c")), ("BOX", (0, 0), (-1, -1), 1, INK)]))
    story += [t2, Paragraph("Military record", h3)] + [B(x) for x in REC["service"]["lines"]] + [Paragraph("Check before you write about service", h4)] + [B(x) for x in REC["service"]["flags"]]
    story += [Paragraph("Timeline, back and forward", h3)] + [B("%s: %s (%s)" % tuple(t)) for t in REC["timeline"]]
if MIL:
    r_ = MIL["rules"]
    story += [PageBreak(), Paragraph("Military and ROTC: the rules for you", h2), P(r_["summary"])] + [B(x) for x in r_["you"]]
    for br in r_["branches"]:
        story += [Paragraph(e("%s: %s" % (br["branch"], br["verdict"])), h3), B("Age: " + br["age"]), B("Prior service: " + br["prior"]), B("Gate: " + br["gate"]), B(br["extra"])]
    story += [Paragraph("Money and obligations", h3)] + [B(x) for x in r_["money"]]
for s in ranked:
    x = A["schools"][s["id"]]
    r = research.get(s["id"])
    story += [PageBreak(), Paragraph("%d. %s" % (x["rank"], e(s["name"])), h2), P(x["path"], small), P(x["summary"])]
    story += [B(b_) for b_ in x["bullets"]]
    story += [Paragraph("<b>Why it sits at %d of %d:</b> %s" % (x["rank"], N, e(x["rankReason"])), body),
              Paragraph("<b>Numbers:</b> " + e(x["stat"]), body)]
    ml = MIL.get("schools", {}).get(s["id"])
    if ml:
        story += [Paragraph("Military and ROTC", h3), B("Army: %s. %s" % (U[ml["army"][0]], ml["army"][1])), B("Air Force: %s. %s" % (U[ml["af"][0]], ml["af"][1])),
                  B("Navy: %s. %s" % (U[ml["navy"][0]], ml["navy"][1])), Paragraph("<b>Projection:</b> " + e(ml["projection"]), body),
                  Paragraph("<b>Unique:</b> " + e(ml["unique"]), body), Paragraph("<b>Veteran side:</b> " + e(ml["vets"]), body)]
    if x.get("gate"):
        story.append(Paragraph("<b>Check first:</b> " + e(x["gate"]), body))
    if x.get("portal"):
        story.append(Paragraph("<b>In your portal now:</b> " + e(x["portal"]), body))
    if r:
        story += [Paragraph("Official research, checked " + e(r["verifiedDate"]), h3)] + [B(f) for f in r["findings"]]
        story += [P("Limits of this research: " + r["limitations"], small), P("Source: " + r["source"], small)]
    story.append(Paragraph("Supplements: %d" % len(x["supplements"]), h3))
    for q in x["supplements"]:
        story += [Paragraph(e(q["title"]), h4), P("%s. %s" % (q["limit"], q["status"]), small),
                  Paragraph("<i>Prompt, paraphrased:</i> " + e(q["prompt"]), body)]
        story += [B(g) for g in q["guidance"]]
        story.append(P(q["provenance"], small))
story += [PageBreak(), Paragraph("Reserve bench", h2)]
story += [Paragraph("<b>%s:</b> %s" % (e(b_["name"]), e(b_["one"])), bul, bulletText="•") for b_ in D["bench"]]
story += [Paragraph(e(b["school"] + ": " + b["title"]), h3), P("%s. %s" % (b["limit"], b["status"]), small),
          Paragraph("<i>Prompt, paraphrased:</i> " + e(b.get("prompt", "")), body)] + [B(g) for g in b["guidance"]]


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(colors.HexColor("#5b564c"))
    canvas.drawString(0.75 * inch, 0.5 * inch, "Private planning document. Guidance supports your own writing. Verify every date and prompt in the live application.")
    canvas.drawRightString(7.75 * inch, 0.5 * inch, "Page %d" % doc.page)
    canvas.restoreState()


SimpleDocTemplate(str(out / (NAME + ".pdf")), pagesize=letter, leftMargin=0.75 * inch, rightMargin=0.75 * inch,
                  topMargin=0.7 * inch, bottomMargin=0.8 * inch, title="Kendren Cornish: %d-school transfer strategy" % N,
                  author="Kendren Cornish").build(story, onFirstPage=footer, onLaterPages=footer)
print("wrote", out / (NAME + ".md"), "and .pdf")
