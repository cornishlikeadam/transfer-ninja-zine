#!/usr/bin/env python3
"""One-off authoring step: turns data/base.json (the first 12 cards) into data/schools.json,
the source of truth the build reads. Edit data/schools.json by hand afterwards, or rerun this
script after changing the dictionaries below.

Sources for the money / study abroad / links fields: official school pages found by web search
in November 2026, plus Kendren's own call transcripts (Notre Dame, Brown, Cornell). Anything a
school does not publish for transfer students is written as "not found: ask <office>".
"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
base = json.load(open(os.path.join(HERE, "base.json"), encoding="utf-8"))
S = {s["id"]: s for s in base["schools"]}
L = base["lens"]

# ---------------------------------------------------------------- corrections to existing lenses
L["princeton"].update({
    "path": "Top three on your list: Operations Research and Financial Engineering (ORFE), African American Studies and Computer Science. Your notes name African American Studies as the Princeton pick. The overview you prepared for Alex Bustin points to a BSE in Mechanical and Aerospace Engineering, so settle the final order before the essays.",
    "know": [["Ruha Benjamin", "African American Studies; science, technology and social inequity."],
             ["Arvind Narayanan", "Directs the Center for Information Technology Policy (technology and policy lane)."],
             ["Olga Russakovsky", "Visual AI Lab: human-centered AI and fairness (Computer Science lane)."]],
    "gap": "ORFE faculty and research are not yet researched. Add one current ORFE paper or project.",
    "ask": "How are my courses evaluated toward distribution and the prerequisites for ORFE or African American Studies, and which graded paper best shows readiness?",
    "show": "The graded paper with its prompt, grade and instructor comments, and two academic recommenders including one college instructor. Show the preparation each lane expects, such as quantitative coursework for ORFE. The arts supplement only if the work truly fits.",
})
L["vandy"].update({
    "path": "Peabody College: Human and Organizational Development (HOD), your ILR equivalent. Not computer science.",
    "know": [["Jenny L. Davis", "Sociology; the politics and ethics of technological design. A cross-college anchor, not an HOD faculty member."]],
    "gap": "HOD faculty and research are not yet researched.",
    "ask": "How would my courses be evaluated for Peabody HOD, and what syllabus evidence helps the evaluator?",
    "show": "Two instructor recommendations, at least one from a college instructor. A theme of how people, organizations and systems work or fail, with the Nashville emergency-routing project as a civic example.",
})
L["nu"].update({
    "path": "Not Computer Science. Your target major is not recorded yet. Candidates close to your ILR and Peabody interest are the School of Education and Social Policy (Learning and Organizational Change, Social Policy) and Weinberg (Sociology, African American Studies). Confirm the exact names with Northwestern before choosing.",
    "know": [["Elizabeth Gerber", "Co-directs the Center for Human-Computer Interaction + Design. A cross-school anchor, not a degree path."],
             ["Nicholas Diakopoulos", "Directs the Computational Journalism Lab; algorithmic accountability. A cross-school anchor."]],
    "gap": "Faculty for the School of Education and Social Policy and Weinberg paths are not yet researched.",
    "ask": "Which School of Education and Social Policy or Weinberg major fits a veteran transfer interested in people, organizations and policy, and how do my credits map?",
    "show": "A school-specific reason that names a real major and cites cross-school pathways accurately.",
})
L["brown"].update({
    "path": "A policy-oriented concentration, Africana Studies, Science, Technology and Society, or Modern Culture and Media. Not computer science first. On your call Brown noted that a concentration is like a major with its own requirements, and that even a policy concentration can carry a math requirement, so statistics helps. Confirm the exact concentration.",
    "know": [["Suresh Venkatasubramanian", "Directs the Center for Technological Responsibility, Reimagination and Redesign (CNTR): technology and policy lane."],
             ["Harini Suresh", "Sociotechnical dimensions of AI, fairness and how affected communities experience automated systems."]],
    "ask": "How have project-based courses typically mapped into Brown credit, and what sequencing would remain for a policy, Africana Studies or STS concentration?",
})
L["tufts"].update({
    "path": "Arts and Sciences social-science or cognitive path: sociology, Science, Technology and Society, cognitive and brain science or economics. Computer science appears only as coursework, not the major. SMFA studio work needs written confirmation from REAL and SMFA.",
    "ask": "Which syllabi should I supply to separate credit for my intended Arts and Sciences major from general electives, and can REAL students use SMFA studio courses?",
})
L["washu"].update({
    "path": "Arts and Sciences: Sociology, Philosophy-Neuroscience-Psychology, or anthropology with digital humanities. Sam Fox (Design) only with a portfolio. Not computer science. A new 15-credit computational AI minor is open across schools.",
})
L["yale"].update({
    "path": "Ethnicity, Race and Migration through Eli Whitney is the pick in your notes. Computing and the Arts and African American Studies also appear in your research. Confirm the order.",
})
L["cornell"].update({
    "path": "ILR BS: labor, technology, workplace systems, policy and economics. Africana Studies is available as a minor, and as a transfer you cannot double major across two Cornell colleges (Kyle, call). The earlier faculty research was written for Information Science, so treat it as method context until ILR faculty are researched.",
})
L["nd"].update({
    "path": "College of Arts and Letters with Africana Studies as the likely major, plus the cross-college Tech Ethics minor. Law school is the long-term aim, and the veterans law clinic came up on your call. The IDEA Center is a resource, not a degree.",
})
L["smu"].update({
    "path": "Meadows BA in Creative Computing is the closest fit but leans toward computing. Film and Media Arts or Public Relations and Strategic Communication are the alternates in your plan.",
})

# ---------------------------------------------------------------- new schools
S["williams"] = {
    "id": "williams", "name": "Williams", "route": "Liberal Arts Transfer", "pri": "core", "talked": 0,
    "one": "Plan around the two-year residence rule: a junior-entry transfer must give up transfer credit to study away.",
    "facts": ["Transfer credit is capped at two years of credit, and Williams requires two years in residence.",
              "Offers only need-based aid, with no merit scholarships. The CSS Profile is required for non-federal aid.",
              "Official dates conflict: the aid page lists March 3, the Common App March 2, an older catalog March 1."],
    "next": "Confirm the March date on the official page, decide sophomore or junior entry, and ask the admission office how a veteran transfer is reviewed.",
    "src": "https://www.williams.edu/admission-aid/apply/transfer/",
    "d": [["2027-03-01", "Application and financial aid (official page may list March 3)", "x", "https://www.williams.edu/admission-aid/apply/transfer/"]],
}
L["williams"] = {
    "di": "ask", "diText": "No published transfer interest rule was found. Ask once.",
    "path": "Majors on file are Africana Studies and Cognitive Science (older dossier). Your target is not recorded yet. Confirm it.",
    "know": [], "gap": "Not researched in the library yet. Add one Williams department, course or project you have read.",
    "res": "", "evi": "",
    "who": "Williams admission office. The Service to School VetLink guidebook has a Williams page.",
    "ask": "How does Williams review a veteran transfer with SCAD and prior college credit, and does the two-year residence rule change my entry year?",
    "show": "A school-specific reason that names a real department and shows tested fit.",
    "dont": "Do not send extras or contact faculty for admissions help.",
}
S["wesleyan"] = {
    "id": "wesleyan", "name": "Wesleyan", "route": "Transfer (Common App for Transfer)", "pri": "core", "talked": 0,
    "one": "Apply for aid with the application: the fee is waived then, and skipping aid costs you aid eligibility for a year.",
    "facts": ["Fall transfer applications are due March 15, with notification on May 15 (a Wesleyan aid page gives a conflicting late-April date).",
              "Meets 100% of demonstrated need with loan-free packages, but is need-aware for transfer admission.",
              "Applicants who say they will not seek aid are not eligible for Wesleyan aid until after one year enrolled."],
    "next": "Confirm the Fall 2027 dates, file the aid request with the application, and ask how a veteran transfer is reviewed.",
    "src": "https://www.wesleyan.edu/admission/apply/transfer.html",
    "d": [["2027-03-15", "Application and financial aid request (confirm Fall 2027 date)", "x", "https://www.wesleyan.edu/admission/apply/transfer.html"]],
}
L["wesleyan"] = {
    "di": "ask", "diText": "No interest policy has been researched yet. Ask once.",
    "path": "No major is on file for Wesleyan, and your notes do not cover it. Name the one you want.",
    "know": [], "gap": "Not researched in the library or your notes. Add one department, course or project you have read.",
    "res": "", "evi": "",
    "who": "Wesleyan transfer admission office.",
    "ask": "Given need-aware transfer admission, how does applying for aid affect review, and how are veteran transfers evaluated?",
    "show": "A school-specific reason that names a real major.",
    "dont": "Do not skip the aid request to look stronger: it limits aid for a year.",
}
S["amherst"] = {
    "id": "amherst", "name": "Amherst", "route": "Liberal Arts Transfer", "pri": "core", "talked": 1,
    "one": "Send the transfer essay (250 to 500 words on your reasons for transferring) and confirm the Fall 2027 date.",
    "facts": ["Transfer applicants submit the Common App or Coalition transfer application plus the Amherst supplement.",
              "A Veteran Fee Waiver is listed on the Common App, and the fee can also be waived through Quick Pass.",
              "No interview is required for admission consideration."],
    "next": "Follow up after your admissions call, confirm the March date on the official page, and ask about transfer aid and study abroad.",
    "src": "https://www.amherst.edu/admission/apply/transfer",
    "d": [["2027-03-01", "Application (confirm on the official page)", "x", "https://www.amherst.edu/admission/apply/transfer"]],
}
L["amherst"] = {
    "di": "ask", "diText": "No interest policy has been researched yet. Ask once.",
    "path": "Black Studies and the Open Curriculum are on file (older dossier). Your target is not recorded yet. Confirm it.",
    "know": [], "gap": "Not researched in the library yet. Add one Amherst course or project you have read.",
    "res": "", "evi": "",
    "who": "Nick Fritz (admissions, call held Oct 23).",
    "ask": "How does the Open Curriculum handle transfer credit, and what aid does Amherst offer a veteran transfer?",
    "show": "A transfer essay that names the real reason for moving and a specific Amherst fit.",
    "dont": "Do not send extra papers unless Nick asks.",
}

# SMU: stays, on a scholarship gate
S["smu"]["one"] = "Apply only if a scholarship plus benefits makes SMU close to free. Get a written net-cost estimate first."
S["smu"]["gate"] = "Stays on the list only with a full, decent scholarship. Automatic transfer merit needs 24 transferable hours and a 3.3 GPA, and the larger awards need 3.5 or higher."

# ---------------------------------------------------------------- money, study abroad, links
M = {}
M["brown"] = dict(
    fin=dict(
        waiver="No application fee for veterans, who use the separate Veterans Application.",
        model="Veterans are admitted need-blind. General transfer admission is need-aware. Brown meets full demonstrated need.",
        aid="Veterans submit the FAFSA, a prior-year tax return and a VA Certificate of Eligibility. Veteran aid materials were due March 1 in the 2026 cycle, so recheck 2027. On your call: VR&E pays out like a Post-9/11 GI Bill.",
        vet="Service to School VetLink partner with an unlimited undergraduate Yellow Ribbon program for eligible students.",
        note="The binding rolling option means you withdraw other applications if admitted. Compare aid first."),
    abroad="Brown students in good standing can study abroad for a semester or year in sophomore, junior or senior year, after declaring a concentration. Brown aid can apply if aid requirements are met and a Consortium Agreement is filed for non-Brown programs. Courses need pre-approval to earn credit. No rule specific to transfer or veteran-route entrants was found: ask Brown study abroad advising.",
    links=[["Veterans Application", "https://admission.brown.edu/veterans/application-details"], ["Veteran financial aid", "https://admission.brown.edu/veterans/financial-aid"], ["Veteran students and aid", "https://finaid.brown.edu/veteran-students-new-and-current"], ["Study abroad FAQs", "https://studyabroad.brown.edu/explore/study-abroad-faqs"], ["Study abroad and aid", "https://studyabroad.brown.edu/apply/you-apply/financial-planning/financial-aid"], ["Transfer credit guidelines", "https://college.brown.edu/design-your-education/review-academic-policies/transfer-credit-guidelines"]])
M["cornell"] = dict(
    fin=dict(
        waiver="No transfer fee-waiver rule was found. Ask ILR admissions.",
        model="ILR says transfer aid follows the same need-based policies as first-year students. Whether domestic transfer admission is need-blind was not confirmed.",
        aid="ILR admits transfers for fall only, with a March 15 application deadline. The CSS Profile transfer deadline was March 15 in the 2026 cycle.",
        vet="Yellow Ribbon participant with a Veterans Summer Bridge and a veteran admissions pathway that can waive some documents.",
        note=""),
    abroad="ILR says transfer students are eligible to apply for semester study abroad and ILR credit internship programs (Ireland, England, Australia). The usual rules: full-time, junior or senior year, good standing and the ILR core finished. Aid transfers for Office of Global Learning programs and is revised for the term abroad. Meet the ILR study abroad advisor to check how transfer status counts.",
    links=[["ILR transfer guidelines", "https://www.ilr.cornell.edu/programs/undergraduate-admissions/apply-ilr/transfer-guidelines"], ["Cornell transfer instructions", "https://admissions.cornell.edu/resources/transfer-option-instructions"], ["ILR financial aid", "https://www.ilr.cornell.edu/current-students/credit-internships/students/financial-aid"], ["ILR exchange programs", "https://www.ilr.cornell.edu/current-students/international-opportunities/exchange-programs"], ["ILR global learning", "https://www.ilr.cornell.edu/current-students/international-opportunities/office-global-learning"], ["Aid for study abroad", "https://www.finaid.cornell.edu/study-abroadoff-campus-programs"]])
M["nd"] = dict(
    fin=dict(
        waiver="No transfer fee-waiver rule was found. Ask admissions.",
        model="A VetLink guide lists Notre Dame as need-blind for all admitted students. An official statement for transfers was not found. Transfer students are not eligible for merit scholarships.",
        aid="From your call: a household income of $60,000 or less covers tuition, fees, housing and food, and up to $150,000 covers at least full tuition. You do not have to use the GI Bill to attend. Fall transfer deadline March 15.",
        vet="Yellow Ribbon school. On your call, a 100% GI Bill pays up to about $30,000 a year more or less. Service to School VetLink, Warrior-Scholar Project and a veterans law clinic.",
        note=""),
    abroad="Students in approved programs count as enrolled at Notre Dame for federal aid. Aid is not guaranteed abroad, and non-Notre Dame programs need a Consortium Agreement. Because Notre Dame meets need, outside funds can adjust your aid. Same fees as campus plus a $750 study abroad fee. No rule specific to transfer entrants was found: ask Global Study Abroad.",
    links=[["Transfer applicants", "https://admissions.nd.edu/information-for/transfer-applicants/"], ["Admitted transfers: financial aid", "https://admissions.nd.edu/admitted-transfers/financial-aid/"], ["Transfer student aid", "https://financialaid.nd.edu/apply-or-renew/transfer-students/"], ["Study abroad aid policy", "https://financialaid.nd.edu/policies/study-abroad/"], ["Veterans", "https://admissions.nd.edu/apply/resources-for/veterans/"], ["Service to School VetLink", "https://omva.nd.edu/prospective-students/service-to-school-vetlink/"], ["Global study abroad", "https://studyabroad.nd.edu/"]])
M["yale"] = dict(
    fin=dict(
        waiver="Automatic for U.S. veterans and active duty: answer Yes to the military fee waiver question in the Program Materials section.",
        model="Yale admits without regard to ability to pay and meets 100% of demonstrated need for Eli Whitney students. EWSP students are treated as independent, so parental income is not counted.",
        aid="Financial aid application due April 1. Materials due March 15 (one Yale page says March 18, so confirm).",
        vet="Yellow Ribbon participant. Yale's veteran and military student office handles benefit coordination.",
        note=""),
    abroad="Eli Whitney students can study abroad for a year or term with approval from the program director and the Committee on the Year or Term Abroad, doing full-time university-level work. Yale aid carries abroad with a budget form, capped at two terms. After returning you must enroll in Yale College: the catalog says two terms and a study abroad page says one, so confirm.",
    links=[["EWSP application", "https://admissions.yale.edu/eli-whitney-apply"], ["EWSP financial aid", "https://admissions.yale.edu/eli-whitney-students-program-financial-aid"], ["Yale aid for EWSP", "https://finaid.yale.edu/ewsp"], ["Veterans", "https://admissions.yale.edu/veterans"], ["Year or term abroad eligibility", "https://studyabroad.yale.edu/node/1233"], ["EWSP catalog rules", "https://catalog.yale.edu/ycps/academic-regulations/eli-whitney-students-program"], ["Veteran and military office", "https://vetmil.yale.edu/undergraduate-students"]])
M["princeton"] = dict(
    fin=dict(
        waiver="Automatic: choose the US military veterans and servicemembers fee waiver option on the application. Lower-income applicants who apply for aid also get a waiver.",
        model="Aid is need-based and Princeton aims to meet 100% of need. A clear official statement of need-blind transfer admission was not retrieved. Princeton aid can supplement or replace veterans benefits.",
        aid="Princeton uses its own Princeton Financial Aid Application (PFAA) and does not require or accept the CSS Profile or IDOC. Transfer aid deadline March 9.",
        vet="Participates in Service to School VetLink, Warrior-Scholar Project and the Leadership Scholar Program. Yellow Ribbon coordination through financial aid.",
        note=""),
    abroad="Study abroad is open to spring-term sophomores, juniors and fall-term seniors with a 3.0 or higher GPA the prior year, and most students go no earlier than spring of sophomore year. Princeton need-based aid carries to approved academic-year programs, but the Princeton Grant does not cover summer programs. Transfer-specific rules were not found: ask the Study Abroad Program.",
    links=[["Transfer dates and deadlines", "https://admission.princeton.edu/apply/application-dates-deadlines/transfer-application-dates-deadlines"], ["Transfer checklist", "https://admission.princeton.edu/how-apply/transfer-students/transfer-application-checklist"], ["Graded written paper", "https://admission.princeton.edu/apply/graded-written-paper"], ["Military applicants", "https://admission.princeton.edu/apply/us-military-applicants"], ["Apply for aid", "https://finaid.princeton.edu/apply-aid-prospective-students"], ["Study abroad and aid", "https://finaid.princeton.edu/policies-procedures/study-abroad"], ["Study abroad policy", "https://www.princeton.edu/oip/sap/policies/academic-year/"], ["ORFE department", "https://orfe.princeton.edu/"], ["African American Studies", "https://aas.princeton.edu/"], ["Computer Science", "https://www.cs.princeton.edu/"]])
M["tufts"] = dict(
    fin=dict(
        waiver="No automatic waiver is stated on the REAL page: contact REAL if the fee is a hardship. Tufts Engineering lists an $85 waiver for military and veterans, so confirm for REAL.",
        model="Need-based aid for eligible REAL students, meeting 100% of demonstrated need. Need-blind status was not confirmed. File the Tufts Financial Aid Form as well as the FAFSA. If you do not apply for aid now, you are not eligible for institutional aid in later years.",
        aid="Application due March 15, 2027. Aid materials are due mid-April, with the exact day unpublished. Say on the REAL application that you intend to use VA benefits.",
        vet="Yellow Ribbon: $5,000 a year from Tufts, matched by the VA, for veterans at 100% Post-9/11 eligibility.",
        note=""),
    abroad="Aid transfers automatically for Tufts-run programs. For external programs only federal and state aid and loans transfer, through a Consortium Agreement, and Tufts grants do not. Courses need department approval. Whether REAL students can use study abroad was not found: ask REAL.",
    links=[["REAL application", "https://admissions.tufts.edu/apply/applying-as-a-transfer-candida/real-application/"], ["REAL for veterans", "https://students.tufts.edu/academic-advising-and-undergraduate-studies/real-program-veterans"], ["Apply for aid", "https://students.tufts.edu/financial-services/undergraduate-aid/prospectiveadmitted-students/apply-aid-prospective-undergraduate-students"], ["Transfer student aid", "https://admissions.tufts.edu/tuition-and-aid/applying-for-aid/transfer-student-aid"], ["Semester and year programs", "https://students.tufts.edu/tufts-global-education/explore/semesteryear-programs"], ["Study abroad funding", "https://students.tufts.edu/tufts-global-education/prepare/accepted-students/financial-aid-and-funding"]])
M["washu"] = dict(
    fin=dict(
        waiver="The $75 fee is waived for U.S. veterans applying for first-year or transfer admission: indicate eligibility on the Common App or Coalition App. It is also waived for applicants applying for need-based aid.",
        model="International transfer applicants are not eligible for aid. Need-blind status for domestic transfers was not confirmed.",
        aid="Application and aid working date March 1, 2027. Verify when WashU relabels the Fall 2027 calendar.",
        vet="Yellow Ribbon was not confirmed in this search: ask financial aid.",
        note=""),
    abroad="Need-based aid and scholarships can apply to approved WashU study abroad programs, but generally not to summer programs. A 3.0 GPA is required, and a C or better for credit. Transfer-specific rules were not found: ask Overseas Programs.",
    links=[["Transfer admission", "https://admissions.washu.edu/how-to-apply/transfer-students-us-and-international/"], ["Financial aid", "https://financialaid.washu.edu/"], ["Overseas programs", "https://overseas.washu.edu/"], ["Study abroad eligibility", "https://overseas.washu.edu/plan"]])
M["nu"] = dict(
    fin=dict(
        waiver="Armed Forces or Veteran Fee Waiver, plus hardship waivers, requested through a Common App or Coalition profile question. The fee is $75 otherwise. Requesting a waiver does not disadvantage you.",
        model="Need-aware or need-blind status for transfers was not established. Verify with admissions.",
        aid="FAFSA and CSS Profile are both required (Northwestern CSS code 1565). Your audited list shows April 1 for the application, April 15 for FAFSA and CSS, and April 20 for tax forms. A search result cited March 15 and the admissions table lists aid on April 1, so verify before relying on any date.",
        vet="Yellow Ribbon was not confirmed in this search: ask the aid office.",
        note=""),
    abroad="Study abroad eligibility starts the summer after you finish your first year at Northwestern, and this applies to transfers too, with a 2.5 GPA. Need-based aid covers Northwestern, exchange and partner programs but not independent programs. Summer aid covers one summer. Study abroad credit is treated as transfer credit.",
    links=[["Application deadlines", "https://admissions.northwestern.edu/apply/application-deadlines.html"], ["Transfer FAQ", "https://admissions.northwestern.edu/faqs/transferring-to-northwestern/"], ["Fee waiver", "https://admissions.northwestern.edu/tuition-aid/fee-waiver.html"], ["Aid deadlines", "https://undergradaid.northwestern.edu/apply-for-aid/application-deadlines.html"], ["Study abroad aid", "https://undergradaid.northwestern.edu/types-of-aid/study-abroad-aid.html"], ["Apply to study abroad", "https://www.northwestern.edu/abroad/study-abroad/apply/"], ["School of Education and Social Policy", "https://www.sesp.northwestern.edu/"]])
M["gt"] = dict(
    fin=dict(
        waiver="Fee waiver requests are accepted from any applicant for whom the fee is a significant burden, using the NACAC or College Board form. The deadline does not move for waiver requests.",
        model="Need-based aid only. Georgetown meets 100% of demonstrated need for U.S. citizens and permanent residents. International transfers are not eligible for aid.",
        aid="Submit both the FAFSA and the CSS Profile. Application and aid March 1, with the junior Public Policy or Environment and Sustainability priority date January 15. Decisions by June 1.",
        vet="Dossier lists Yellow Ribbon with a full tuition match in the College. Confirm on Georgetown's military and veterans page.",
        note=""),
    abroad="All aid except Federal Work-Study applies to Georgetown-approved and independent petition study abroad programs, and students in Global Education programs stay matriculated. No study abroad while on probation. Summer aid needs 6 or more credits. Georgetown Qatar covers one semester. Transfer-specific rules were not found: ask the Office of Global Education.",
    links=[["Transfer applicants", "https://uadmissions.georgetown.edu/apply/transfer-applicants/"], ["Financial aid", "https://uadmissions.georgetown.edu/financial-aid/"], ["Study abroad costs and aid", "https://studyabroad.georgetown.edu/?p=238"], ["Aid for study abroad", "https://finaid.georgetown.edu/?p=219"]])
M["vandy"] = dict(
    fin=dict(
        waiver="$50 application fee or a fee waiver for qualified students, through the Common App or Coalition transfer application. Vanderbilt issues no CSS fee-waiver codes: the CSS Profile may waive its own fee based on your answers.",
        model="A secondary source says Vanderbilt meets 100% of demonstrated need for admitted transfers. Verify on Vanderbilt's own site.",
        aid="Your audited list shows February 1 for FAFSA and CSS priority and February 15 for the priority application.",
        vet="The registrar certifies VA benefits. Yellow Ribbon contributions vary by school, so get a written estimate from the VA School Certifying Official.",
        note=""),
    abroad="Transfer students can apply to study abroad after completing their first semester at Vanderbilt per the policies page, though another source says two semesters, so reconcile with the Study Abroad office. Semester and academic-year programs through Vanderbilt are eligible for federal and Vanderbilt aid, and the package can increase if a program costs more than a comparable term. Summer aid is limited.",
    links=[["Transfer process", "https://admissions.vanderbilt.edu/apply/transfer-process"], ["Financial aid deadlines", "https://www.vanderbilt.edu/financialaid/deadlines/"], ["Study abroad policies", "https://www.vanderbilt.edu/study-abroad/policies/"], ["Study abroad finances", "https://www.vanderbilt.edu/study-abroad/finances/"], ["Peabody College", "https://peabody.vanderbilt.edu/"]])
M["williams"] = dict(
    fin=dict(
        waiver="The $65 fee can be waived, and Williams says asking does not disadvantage you. Veterans can request a waiver on the Common App. The CSS Profile fee can also be waived, and the $200 enrollment deposit too.",
        model="Williams offers only need-based aid with no merit scholarships. Need-blind status for transfers was not stated. The CSS Profile is required for non-federal aid.",
        aid="Admission and aid applications are due together, with no extra materials for transfer aid. The official date is unclear (March 1 to 3).",
        vet="Williams encourages veterans to apply, as first-year or transfer depending on college coursework. Service to School VetLink guidebook has a Williams page.",
        note=""),
    abroad="Williams requires two years in residence and caps transfer credit at two years. A student who enrolls as a junior and wants to study away must give up a semester or year of transfer credit to meet residence. Aid recipients submit a budget proposal for study away. A new tuition model removes a $1,500 study away fee from the Class of 2029, except for Williams-Exeter and Williams-Mystic. Whether transfers can join Williams-Exeter was not stated.",
    links=[["Transfer admission", "https://www.williams.edu/admission-aid/apply/transfer/"], ["Transfer financial aid", "https://www.williams.edu/admission-aid/financial-aid/transfers/"], ["Apply for aid", "https://www.williams.edu/admission-aid/financial-aid/apply-for-aid/"], ["Study away", "https://williams.edu/sfs/study-abroad"], ["Williams-Exeter Programme", "https://exeter.williams.edu/the-program/"], ["VetLink guidebook: Williams", "https://service2school.gitbook.io/vetlink-guidebook/williams-college"]])
M["wesleyan"] = dict(
    fin=dict(
        waiver="The application fee is automatically waived for any student applying for financial aid.",
        model="Meets 100% of demonstrated need with loan-free packages for domestic students, but is need-aware for transfer admission. International transfers get very limited aid.",
        aid="Aid request due March 15. If you say you will not seek aid, you are not eligible for Wesleyan aid until after one year (two full semesters) enrolled.",
        vet="Veterans benefits and Yellow Ribbon were not researched: ask financial aid.",
        note=""),
    abroad="Semester and year study abroad for credit counts as Wesleyan enrollment, so Wesleyan tuition is charged and aid applies. The Office of Study Abroad prepares a budget sheet and aid is revised from it. Work-study is replaced by a grant. Wesleyan aid does not cover summer or winter programs. Transfer-specific rules were not found: ask the Office of Study Abroad.",
    links=[["Transfer applicants", "https://www.wesleyan.edu/admission/apply/transfer.html"], ["Study abroad rules", "https://catalog.wesleyan.edu/academic-regulations/study-abroad"], ["Study abroad and aid", "https://wesleyan.edu/finaid/current-students/non-resident-study.html"]])
M["amherst"] = dict(
    fin=dict(
        waiver="A $65 fee or a fee waiver request through the Common App, Coalition App or Quick Pass. The Common App lists a Veteran Fee Waiver.",
        model="A secondary source says Amherst aims to meet 100% of demonstrated need for transfers and is need-blind for U.S. applicants. Amherst's own transfer aid page was not retrieved.",
        aid="No transfer-specific aid deadlines could be verified. Confirm on the official page.",
        vet="Dossier lists a veterans program with Posse Veterans and VetLink. Unverified: ask admissions.",
        note=""),
    abroad="No official Amherst rule on study abroad or aid for transfer students was found. Ask admissions or the financial aid office.",
    links=[["Transfer admission", "https://www.amherst.edu/admission/apply/transfer"], ["Common App page", "https://www.commonapp.org/explore/amherst-college"]])
M["usc"] = dict(
    fin=dict(
        waiver="Veteran or service member waiver: select it under the school-specific question in the USC Questions section of the Common App. Hardship waivers are also available.",
        model="USC describes itself as need-blind for admission. Veterans should file the FAFSA and CSS Profile even when planning to use VA benefits, and can choose the GI Bill after seeing the aid package.",
        aid="Your audited list shows February 15 for the application and March 2 for FAFSA and CSS priority filing. Other USC pages cite earlier dates, so verify.",
        vet="Yellow Ribbon participant with an unlimited undergraduate program for eligible students. USC says eligible undergraduates with remaining GI Bill can graduate debt-free.",
        note=""),
    abroad="Iovine and Young BS students can fulfil up to 12 major units abroad with faculty approval, limited to major electives, with spring of junior year preferred. Whether aid applies to an Academy study abroad term was not found: ask. Outside-transfer eligibility for the Academy also needs written confirmation.",
    links=[["Transfer students", "https://admission.usc.edu/prospective-students/how-to-apply/transfer-students/"], ["Military and veterans", "https://military.usc.edu/"], ["Iovine and Young study abroad", "https://dornsife.usc.edu/overseas-studies/iovine-and-young-academy/"], ["Why USC does not track interest", "https://www.admissionblog.usc.edu/p/why-we-dont-track-demonstrated-and"]])
M["smu"] = dict(
    fin=dict(
        waiver="The veterans page says SMU automatically waives the application fee for all undergraduate U.S. military veteran applicants. A newer sheet says all undergraduates this cycle, so confirm.",
        model="Merit comes automatically with 24 transferable hours and a 3.30 GPA: the Founders Scholarship is $15,000 a year for up to six terms, the Transfer Honor Scholarship is half tuition at 3.5, and a full-tuition-and-fees award needs 3.7 (North Texas community college students). Your gate is a full, decent scholarship.",
        aid="FAFSA and CSS priority February 1. Priority application April 1. Final application August 1.",
        vet="Yellow Ribbon guarantees a 100% tuition benefit for eligible Post-9/11 veterans for the length of their entitlement. Veterans apply as transfer students.",
        note="Ask for a written net-cost estimate, with scholarship and benefits combined, before applying."),
    abroad="No transfer-specific study abroad award was found. Study abroad appears as an add-on in some first-year awards only.",
    links=[["Transfer scholarships", "https://www.smu.edu/admission/apply/transfer/scholarships"], ["Veterans", "https://smu.edu/admission/apply/veterans"], ["Yellow Ribbon", "https://www.smu.edu/EnrollmentServices/Registrar/VeteransAffairs/YellowRibbonProgram"], ["Transfer FAQs", "https://www.smu.edu/admission/apply/transfer/faqs"], ["Application process", "https://www.smu.edu/admission/apply/transfer/application-process"]])

# ---------------------------------------------------------------- assemble
order = ["brown", "cornell", "nd", "yale", "princeton", "tufts", "washu", "nu", "gt", "vandy",
         "williams", "wesleyan", "amherst", "usc", "smu"]
schools = []
for sid in order:
    s = S[sid]
    s["di"] = L[sid]["di"]
    s.update(M[sid])
    if sid in ("usc", "smu"):
        s["pri"] = "conditional"
    schools.append(s)
out = {"schools": schools, "bench": base["bench"], "lens": {k: L[k] for k in order}}
json.dump(out, open(os.path.join(HERE, "schools.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("schools:", len(schools), "| lens:", len(out["lens"]))
