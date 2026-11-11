import json,pathlib,html
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,KeepTogether
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib import colors
R=pathlib.Path(__file__).resolve().parents[1];A=json.loads((R/'data/strategy.json').read_text());D=json.loads((R/'data/schools.json').read_text());out=R/'documents';out.mkdir(exist_ok=True)
L=['# Kendren Cornish — 21-school transfer strategy','','Updated November 10, 2026','',A['method'],'',A['inventoryNote'],'','## Personal background and evidence']
for p in A['profile']:L+=['','### '+p['title'],p['text'],'Source: '+p['source']]
L+=['','## Equal-base-rate academic and route compatibility ranking']
for s in sorted(D['schools'],key=lambda s:A['schools'][s['id']]['rank']):
 x=A['schools'][s['id']];L+=[f"{x['rank']}. {s['name']} — {x['rankReason']}"]
for s in D['schools']:
 x=A['schools'][s['id']];r=next(r for r in A['research']['schools'] if r['id']==s['id'])
 L+=['','## '+s['name'],x['summary'],'']+['- '+b for b in x['bullets']]+['',f"Provisional academic/route rank: {x['rank']}/21. {x['rankReason']}",'','### Official research · '+r['verifiedDate']]+['- '+f for f in r['findings']]+['Limitations: '+r['limitations'],'Official source: '+r['source']]
 for q in x['supplements']:L+=['','### '+q['title'],q['limit']+' · '+q['status'],q['provenance']]+['- '+b for b in q['guidance']]
L+=['','## New reserve bench']
for b in D['bench']:
 r=next(r for r in A['research']['bench'] if r['id']==b['id']);L+=['','### '+b['name'],b['one']]+['- '+f for f in r['findings']]+['Official source: '+r['source'],'Limitations: '+r['limitations']]
b=A['benchSupplement'];L+=['','### '+b['school']+' — '+b['title'],b['limit'],b['status']]+['- '+t for t in b['guidance']]
L+=['','## What can change this ranking','Current official GPA and GPA-bearing hours, completed composition/statistics/economics/science, a settled degree choice, verified route eligibility, credit classification and two recent academic recommendations could materially change the order. No admissions probability has been calculated.','', '## Source ledger','Local: August application workbook; July profile/artifact audit and evidence inventory; October 22 transcript-based school review; October master evidence fact sheet; current school lenses; 37 November supplement screenshots. Conflicts and stale figures are marked above. Official school URLs are listed with each school.']
text='\n'.join(L)+'\n';(out/'Kendren_21_School_Strategy.md').write_text(text)
styles=getSampleStyleSheet();styles.add(ParagraphStyle(name='BodyCompact',fontName='Helvetica',fontSize=9.5,leading=13,spaceAfter=7));styles['Title'].textColor=colors.HexColor('#172b37');styles['Heading1'].fontSize=20;styles['Heading1'].leading=24;styles['Heading2'].fontSize=12;styles['Heading2'].leading=16
story=[]
for ln in L:
 if not ln:continue
 if ln.startswith('# '):story+=[Paragraph(html.escape(ln[2:]),styles['Title']),Spacer(1,12)]
 elif ln.startswith('## '):
  if story:story.append(PageBreak())
  story.append(Paragraph(html.escape(ln[3:]),styles['Heading1']))
 elif ln.startswith('### '):story.append(Paragraph(html.escape(ln[4:]),styles['Heading2']))
 elif ln.startswith('- '):story.append(Paragraph('&#8226; '+html.escape(ln[2:]),styles['BodyCompact']))
 else:story.append(Paragraph(html.escape(ln),styles['BodyCompact']))
grouped=[]; pending=[]
for flow in story:
 if isinstance(flow,PageBreak) or (isinstance(flow,Paragraph) and flow.style.name in ["Heading1","Heading2"]):
  if pending:grouped.append(KeepTogether(pending));pending=[]
  if isinstance(flow,Paragraph) and flow.style.name=="Heading2":pending=[flow]
  else:grouped.append(flow)
 elif pending:pending.append(flow)
 else:grouped.append(flow)
if pending:grouped.append(KeepTogether(pending))
story=grouped
def footer(c,d):
 c.setFont('Helvetica',8);c.setFillColor(colors.HexColor('#586875'));c.drawString(42,25,'Kendren Cornish | Private transfer strategy | November 10, 2026');c.drawRightString(570,25,str(d.page))
SimpleDocTemplate(str(out/'Kendren_21_School_Strategy.pdf'),rightMargin=42,leftMargin=42,topMargin=42,bottomMargin=42,title='Kendren Cornish — 21-school transfer strategy').build(story,onFirstPage=footer,onLaterPages=footer)
print('Document paragraphs:',len(L))
