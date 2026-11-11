"""Profile, per-school summaries, standouts, reasons and the stats-only ranking.

Applied on top of data/strategy.json by data/apply_boost.py.
Sources: Kendren's fact sheet, profile memory, resume, call transcripts, raw notes and the
November 10 application screenshots. Benchmarks come from official pages where they exist and
are labeled third-party where they do not. Nothing here is final essay prose.
"""

METHOD = ("This order ignores acceptance rates, as if every school admitted the same share of applicants. "
          "It ranks how your current numbers and preparation compare with what each school publishes: a stated GPA line, "
          "required credits or courses, testing, and whether the route is built to read a veteran or adult record in context. "
          "Your numbers are SCAD 3.33 (most recent college) and about 3.18 pooled with Broward. "
          "It is an advising order, not a probability. Neighbors can swap, and one strong graded quarter changes it.")

INVENTORY = ("Supplement prompts were read from your 37 screenshots dated November 10, which cover 16 active schools plus "
             "Columbia General Studies, and from three Georgetown screenshots dated November 11. Prompts are paraphrased with every required part kept. "
             "You have not opened the Yale, Dartmouth or Penn applications yet, and Northeastern and SMU have no screenshots, "
             "so those entries are marked not captured or official page only. "
             "Always confirm wording and limits in the live application before drafting.")

WHAT_MOVES = [
    "Your Fall 2026 midterms are A, A and A. If they hold as final grades, SCAD rises from 3.33 to 3.55 and pooled from 3.18 to 3.33, cut to two decimals the way registrars report.",
    "Three more A grades in the Winter SCADpro courses would put SCAD at 3.66 and pooled at 3.44. Winter grades post in March, so they reach only the later deadlines.",
    "At 3.55 recent GPA you clear the Cornell ILR 3.4 line and reach the 3.5 line that WashU, UVA and Williams use.",
    "Graded composition, statistics and economics courses matter more than any new project, because five schools name them.",
    "An official credit evaluation from SMU, UVA, Amherst and Notre Dame replaces estimates with real counts.",
    "Choosing the major at Northwestern, Wesleyan, Dartmouth, Williams and UChicago removes the largest unknown at each.",
]

PROFILE = [
    {"title": "Life story in order",
     "text": "High school diploma from Byron Nelson High School in 2019. Army service from December 2020: Reception Battalion at Fort Leonard Wood, Basic Combat Training finished in April 2021, an Engineer-branch Diver specialty and then Health Care Specialist (combat medic) from June 2021. "
             "Security officer at St. Louis Lambert airport in 2022 and 2023. "
             "Broward College followed during a period of severe housing instability, then treatment and transitional housing. "
             "From January to November 2025 you canvassed for CARE, AARP Foundation and World Vision campaigns and moved into mentoring newer recruiters. "
             "You started at SCAD in spring 2026, made the Dean's List in summer 2026, became a residence mentor, ran for student government president, and joined Service to School in October 2026.",
     "source": "Joint Services Transcript (October 2025), Broward transcript, fact sheet, profile memory and resume. Treatment and housing details are yours to disclose or not."},
    {"title": "What drives you",
     "text": "You told Brown that the military part of you is coming back: you want to protect people from the harmful effects of technology. "
             "Your Rice draft says you want to serve underserved people and preserve cultures left out of global and intellectual history. "
             "The common thread is accountability: who a system serves, who owns it, and who is responsible when it fails a person.",
     "source": "Brown call transcript and Rice portal draft, November 2026."},
    {"title": "Academic interests",
     "text": "People, organizations and labor (Cornell ILR, Vanderbilt Human and Organizational Development), Black and Africana studies, "
             "technology ethics and policy, and law. Robotics and AI are your methods, not your major. "
             "Your written work argues that water law and commons theory can guide who owns AI models and data, and that AI pricing shapes educational access.",
     "source": "Your corrections in this project, the Ownership of Intelligence thesis and The New Digital Toll paper."},
    {"title": "Long-term goals",
     "text": "Law school is the stated aim, and you told Brown you would go back to the military as a lawyer. "
             "Your USC portal lists Tech Founder as the dream job and your Princeton portal lists Entrepreneurship as the minor. "
             "These fit together as building tools and then helping write the rules for them, but each application should lead with one.",
     "source": "Brown, Cornell and Notre Dame call transcripts; USC and Princeton screenshots."},
    {"title": "Personality, in your own signals",
     "text": "Your USC answers include Faithful and Happy as two of your three words. You picked Miles Morales as a roommate, Think and Grow Rich as a favorite book, "
             "Sweater Weather as a theme song, and a class on the Many Worlds Interpretation. Your Princeton draft says joy comes from experiences, travel, good energy and family security. "
             "Across drafts you describe yourself as optimistic, persistent after setbacks, and someone who thinks in generations.",
     "source": "USC and Princeton screenshots. These are cues for your own writing, not a diagnosis."},
    {"title": "Faith, family and roots",
     "text": "You grew up around your grandmother's nonprofit, a St. Louis based conference for African American Christian women, and scripture shows up in your drafts. "
             "St. Louis and Texas both count as home ground: you named friends in Texas in your Rice draft, and both places sit in your scorecard weights.",
     "source": "Raw field notes, Rice portal draft and your scorecard."},
    {"title": "Standouts you can prove or nearly prove",
     "text": "Residence mentor at Victory Village and first contact for floor conflict. A faculty-endorsed run for student government president. "
             "A Murph fitness event with Club SCAD that grew into a residence-hall event. 3D interactive floor plans for residence life. "
             "GlowOS, a 21-lesson learning platform shipped for a paying client. An SMU financial technology certificate. "
             "As in National Government, Criminal Law, Geometry of Physical Space, Business Fundamentals and Foundations of Story. Honor Roll and Phi Theta Kappa at Broward.",
     "source": "Fact sheet and resume. Keep the ballot, endorsements, event photos, client deliverables and certificate as proof."},
    {"title": "Projects and writing",
     "text": "KEEPER-0 (an AI agent that records where its output came from), COMMONS (making informal campus contribution visible), BOOK.NOTE (document retrieval), "
             "the Great Books Semantic Engine and the NYC systems case study. Label each feature as built, tested or proposed. "
             "The New Digital Toll was graded in a business class, which matters for Princeton's graded paper.",
     "source": "Resume, portfolio audit and proof inventory."},
    {"title": "Military record and what it opens",
     "text": "The JST lists Private 2, the Diver specialty from December 2020, Basic Combat Training in March and April 2021 (6 recommended lower-division credits), and Health Care Specialist from June 2021. "
             "At 28 or 29 at graduation, Army and Air Force ROTC are realistic on age, while Navy and Marine Corps ROTC almost certainly are not. "
             "Whether any branch can contract you depends on your DD-214: characterization, reentry code and separation reason. Your Winter SCADpro studio for the Military World Games keeps service in your current work.",
     "source": "Joint Services Transcript (October 2025), ROTC eligibility pages researched November 11, 2026, and your SCAD registration."},
    {"title": "Academic record and gaps",
     "text": "Broward 3.04 over 22 GPA hours: term GPAs 3.57, 3.25 and 1.00, with six withdrawals (20 attempted hours), one C and one D. Its A in ENC0017C is a developmental course many schools drop, which would make Broward about 2.83. "
             "SCAD 3.33 over 30 quarter hours, rising from 3.00 to 3.66, and Fall 2026 midterms of A, A and A in Survey of AI Applications, Ethics of Emerging Technology and Color in Context. Pooled 3.18 today, 3.33 if the midterms hold. "
             "Winter 2027 is three SCADpro studios: SCAD Entrepreneurial Ecosystem research, a Deloitte control interface for the LA28 Olympics, and the Military World Games. "
             "No graded college composition, statistics, economics or lab science appears yet, and several schools name exactly those courses. "
             "Yale's contact said the withdrawals and thin recent liberal-arts and quantitative coursework are the obstacle.",
     "source": "Broward transcript (January 2025), SCAD transcript (October 2026), SCAD portal (November 11, 2026) and the Yale call debrief. Update when final grades post."},
    {"title": "How you sound at your best",
     "text": "Direct, reflective and plain. The pattern that works is a concrete fact, an honest complication, what you now understand, and what you did next. "
             "Your portal drafts have real voice and real feeling. They need order, proof and proofreading more than they need bigger language.",
     "source": "Profile memory and the November portal drafts."},
    {"title": "Facts to settle before you submit",
     "text": "Your Princeton draft says you descend from the eighth president through a daughter named Irene: standard histories list only sons for Martin Van Buren, so prove it or cut it. "
             "The song Tek It is usually credited to Cafune, and Sweater Weather to The Neighbourhood. Your resume says Combat Engineer, while the JST lists the Engineer-branch Diver specialty and then Health Care Specialist: match the DD-214 wording everywhere. "
             "SCAD's transcript lists your major as Robotics, Interactive Design and Game Development with an Applied AI minor, while your resume says Applied Artificial Intelligence: confirm which is official. "
             "The 900-plus nonprofit hours, the four-floor responsibility, the Lacoste offer and the 1540 SAT all need a record behind them.",
     "source": "Your own integrity rule: every date, record and outcome stays true and backed by proof."},
    {"title": "Boundaries",
     "text": "You write every essay yourself. Columbia General Studies requires a signed statement that no generative AI wrote or edited the autobiography. "
             "Guidance here organizes material, asks questions and checks facts. It does not supply sentences to paste.",
     "source": "Your intent statement and the Columbia screenshot."},
]

# id: path, summary (two sentences), best approach, standout, reason, portal note, rank, rankReason, stat
S = {}

def school(sid, path, summary, best, standout, reason, rank, why, stat, portal=""):
    S[sid] = {"path": path, "summary": summary,
              "bullets": ["Best approach: " + best, "Standout: " + standout, "Your reason: " + reason],
              "rank": rank, "rankReason": why, "stat": stat, "portal": portal}

school("smu", "Meadows BA in Creative Computing; Film and Media Arts or Public Relations as alternates",
  "SMU is the school where your numbers already clear the published line, and you hold an SMU financial technology certificate. "
  "It stays on your list only if scholarship and veterans benefits together make it close to free.",
  "Show one small project with its revision history and ask for a written net-cost estimate before you apply.",
  "You have already completed SMU coursework through the financial technology certificate, which no other applicant file on your list can say about its school.",
  "Texas is home ground, Yellow Ribbon covers tuition for eligible veterans, and it balances a list full of reaches.",
  1, "Published minimum is 2.7 with 24 transferable hours, and automatic merit starts at 3.3. Your pooled 3.18 clears the minimum.",
  "Line: 2.7 minimum, 3.3 for merit. You: pooled 3.18 clears the minimum by about 0.5; merit depends on SMU's own recalculation.")

school("nu", "Not computer science; School of Education and Social Policy or Weinberg, major still to choose",
  "Northwestern's stated academic expectation is the most reachable on your list after SMU: a B average, a full year of credit and broad coursework. "
  "The open question is which school and major carry your interest in people, organizations and policy.",
  "Pick the school first, then tie one residence-life system you tested and revised to that degree.",
  "You ran a floor, noticed unrecognized contribution, and designed COMMONS in response: a people-and-organizations problem you found yourself.",
  "Design, learning and social policy sit close together there, and the regular route keeps Brown available as first choice.",
  2, "Northwestern says successful transfers usually have a full year of credit, breadth across liberal arts and sciences, and a B average. Both of your numbers clear a B average.",
  "Line: B average and about 36 quarter hours. You: SCAD 3.33 and pooled 3.18 both clear it; breadth in writing, science and social science is the gap.")

school("northeastern", "College of Arts, Media and Design: Interaction or Experience Design, or Psychology and Design",
  "Northeastern suits the part of you that learns by building with other people, and its usual transfer GPA sits right at your SCAD number. "
  "The decision turns on credit transfer and co-op timing, because both change the cost and the finish date.",
  "Use the interactive floor-plan work as a case study with your role, the feedback you got and what you changed.",
  "A shipped client product (GlowOS) plus residence-life design work shows you can deliver for real users, which is what co-op employers look for.",
  "Co-op puts design work in front of real organizations, and veterans at full Post-9/11 eligibility are in the unlimited Yellow Ribbon program.",
  3, "Northeastern says successful transfers generally hold about a 3.3 cumulative. Your SCAD 3.33 sits at that level and your pooled 3.18 is just under.",
  "Line: about 3.3 typical, not a minimum. You: SCAD 3.33 at the line; pooled 3.18 is 0.12 under.")

school("rice", "Social Policy Analysis or Cognitive Sciences",
  "Rice sets a hard floor of 3.2 in your most recent college work, and your SCAD record clears it. "
  "Your portal draft already points at the right material: residence-hall leadership and a wish to serve people left out.",
  "Build the community essay on one listening moment from the residence hall, then name what you would study about it.",
  "You were trusted with a multi-floor residence hall and then joined the design team to document floor plans in 3D for incoming students.",
  "Texas is close to home and friends, and the residential college system rewards the kind of floor-level community work you already do.",
  4, "Rice requires at least 3.2 in the most recent college work, which SCAD 3.33 clears. Admitted transfers typically hold 3.5 or higher.",
  "Line: 3.2 minimum on recent work, 3.5 typical. You: SCAD 3.33 clears the floor by 0.13 and is 0.17 under the typical profile.",
  "Your portal already holds short draft answers for academic interests, why Rice and the community essay.")

school("brown", "Veterans Application; Science, Technology and Society first, Social Analysis and Research second",
  "Brown's Veterans Application reads your record in the context of service, and the Open Curriculum lets you build a plan around technology, institutions and the people they affect. "
  "Your case is strongest when the instinct to protect people, which you described on your Brown call, becomes a focused plan of study.",
  "Lead with one mentoring or residence-life decision, then show the question it raised about who is responsible when a system fails someone.",
  "A veteran who builds working AI tools and also writes about who should own them, through KEEPER-0 and the Ownership of Intelligence thesis.",
  "It is your stated first choice: the Open Curriculum pairs technology with policy and Africana study, and the veteran route is need-blind.",
  5, "The veteran route reads context, tests are not expected and no GPA line is published. Recent grades still carry the file.",
  "Line: none published for the Veterans Application. You: SCAD 3.33, pooled 3.18; a clear concentration plan and recent grades matter most.",
  "Your portal lists Science, Technology, and Society as the primary interest and Social Analysis and Research as the secondary.")

school("tufts", "REAL program; Arts and Sciences social science or cognitive path",
  "Tufts REAL is built for adults and veterans returning to college, so your path reads as a choice instead of a gap. "
  "Tufts is also the one school on your list that says it records real engagement, and its supplement asks you to describe it.",
  "Complete two true engagement steps first: a REAL information session and one direct question to the REAL office.",
  "You returned to college after service and hardship and reached the Dean's List within two terms, which is the story REAL exists to read.",
  "An adult pathway with advising from admission to graduation, need-based aid that meets full need, and civic technology study.",
  6, "REAL reads an adult or veteran record in context and publishes no GPA line. Two academic recommendations and recent coursework carry the weight.",
  "Line: none published for REAL. You: SCAD 3.33, pooled 3.18; eligibility, recent coursework and two instructor letters decide it.")

school("gt", "School of Foreign Service: Science, Technology and International Affairs",
  "Georgetown recommends a B+ average, which your SCAD record meets, and its technology-policy degree matches your interest in who governs systems. "
  "The gap is preparation: that degree expects economics, statistics or calculus, and a language.",
  "Frame veteran resource access or AI pricing as a policy problem, and show the coursework plan that closes the economics gap.",
  "As in National Government and Criminal Law, plus a research paper on how AI pricing shapes educational opportunity.",
  "It joins technology with law and public service, which fits a path toward law school and military legal work.",
  7, "Georgetown recommends B+ or better. SCAD 3.33 meets that and pooled 3.18 is slightly under. The technology-policy degree also expects economics, quantitative work and a language.",
  "Line: B+ recommended, about 3.3. You: SCAD 3.33 meets it; pooled 3.18 is 0.12 under; economics, statistics and language are missing.")

school("vandy", "Peabody College: Human and Organizational Development",
  "Vanderbilt's Human and Organizational Development degree is your ILR equivalent: it studies how people, teams and institutions work or fail. "
  "Your own experience of rebuilding structure and then mentoring others is the subject matter of the major.",
  "Describe one process you improved for newer people, in the nonprofit or on your floor, and what it taught you about organizations.",
  "You have led peers in three settings: a canvassing team, a residence floor and a student government campaign.",
  "It studies exactly what you care about, admitted transfers get full-need aid, and it is not a computer science application.",
  8, "No current official transfer GPA line was found. Older Vanderbilt guidance cited about 3.3 or above at a competitive four-year school, so treat this placement as low confidence.",
  "Line: none verified; a dated admissions answer cited about 3.3. You: SCAD 3.33, pooled 3.18.")

school("cornell", "ILR School, BS in Industrial and Labor Relations",
  "Cornell ILR gives your interest in work, organizations and technology a single degree home, and a third of its graduates go on to law school. "
  "You are just under its stated GPA level and still need the composition, statistics and economics courses its advisers named.",
  "Send ILR your exact course titles, descriptions and grades, then build the essay on one work or mentoring decision and its consequence.",
  "You have seen labor from the ground: field canvassing with daily conversion tracking, and study of how AI may change the workforce.",
  "ILR joins labor, policy and law in one school, and Kyle told you it is among the best preparations for law school.",
  9, "ILR says most admitted transfers hold 3.4 or higher. SCAD 3.33 is 0.07 under and pooled 3.18 is 0.22 under, and three named prerequisites are missing.",
  "Line: 3.4 for most admits. You: SCAD 3.33 is 0.07 under; pooled 3.18 is 0.22 under; composition, statistics and microeconomics still needed.")

school("yale", "Eli Whitney Students Program; Ethnicity, Race and Migration",
  "Yale's Eli Whitney program is designed for students whose education was interrupted, and it has no GPA floor. "
  "Yale's own contact told you what stands in the way: the withdrawals and too little recent liberal-arts and quantitative work.",
  "Follow the advice you were given: add graded English and math, then return with an updated record and one strong analytical paper.",
  "An adult veteran with a rising recent record and community leadership, which is the profile Eli Whitney was created for.",
  "Full-need aid, an adult and veteran community, and room to study race, migration and technology together.",
  10, "Eli Whitney has no GPA floor and weighs recent work, but Yale's contact said the withdrawals and thin recent coursework are the obstacle and raised 2028 as an option.",
  "Line: none; recent broad coursework is the test. You: one strong SCAD term so far; English and math are the stated gaps.")

school("washu", "Arts and Sciences: Sociology, Philosophy-Neuroscience-Psychology or anthropology",
  "WashU would let you study the human side of the systems you already build, in the city where your family roots are. "
  "Its strongest transfer candidates usually hold a 3.5 across broad coursework with composition, so recent grades are the lever.",
  "Tie one design decision that changed your view of users to a question in sociology or cognition, and name the degree.",
  "St. Louis is part of your family story through your grandmother's conference, so your reason for the city is real and specific.",
  "Family roots in St. Louis, a strong social-science college, and a new AI minor open across schools.",
  11, "WashU says the strongest transfer candidates usually hold 3.5 or higher across a broad curriculum with composition. SCAD 3.33 is 0.17 under.",
  "Line: 3.5 for strongest candidates. You: SCAD 3.33 is 0.17 under; pooled 3.18 is 0.32 under; composition not yet shown.")

school("uva", "College of Arts and Sciences: Media Studies, Sociology or Psychology",
  "UVA fits your wish to study how communities use and govern systems, through a liberal-arts major and an optional data science minor. "
  "It needs 24 transferable semester hours plus a full year of college, and its admitted transfers average about 3.5.",
  "Pair one residence-life decision that changed after listening to a student with a precise Arts and Sciences plan and a credit map.",
  "Top grades in government and law courses, and a record of listening before deciding as a residence mentor.",
  "A public university with a strong honor culture and veteran community, and a route into policy and law.",
  12, "Guides attribute an admitted transfer average near 3.5 to UVA, and UVA requires 24 transferable semester hours plus one full year. You are about 0.2 to 0.3 under on GPA.",
  "Line: about 3.5 average (third-party), 24 transferable hours. You: SCAD 3.33, pooled 3.18; transferable count needs UVA's evaluation.")

school("williams", "Africana Studies or Cognitive Science, target still to confirm",
  "Williams would turn your wide curiosity into close, sustained reading and writing in very small classes. "
  "Its usual expectation is about a 3.5 in a strong program, and its two-year residence rule affects when you could study away.",
  "Send a strong graded essay with its prompt, and write the personal essay about one experience that changed the question you ask.",
  "Williams says it especially encourages transfers who started in the military or the workforce, which is your path.",
  "Small seminars, need-based aid without merit games, and a college that actively recruits veterans.",
  13, "A 3.5 average in a strong program is the commonly cited expectation for successful transfers (third-party profile). You are about 0.2 to 0.3 under.",
  "Line: about 3.5 (third-party). You: SCAD 3.33, pooled 3.18; two-year residence rule shapes entry level.")

school("unc", "College of Arts and Sciences: sociology, public policy or media and journalism",
  "UNC gives your service and technology interests a public-facing question about access and institutions. "
  "Its incoming transfers average a 3.7, and veterans using Post-9/11 benefits are charged in-state tuition.",
  "Use a resource-navigation or community-information example to show how designing for people led you to policy questions.",
  "A veteran exemption from testing, in-state tuition by law, and a record of public-facing service work.",
  "A strong public university with real veteran benefits and a path into public policy.",
  14, "UNC reports an average college GPA of 3.7 for incoming transfers. You are about 0.4 to 0.5 under.",
  "Line: 3.7 average for incoming transfers. You: SCAD 3.33 is 0.37 under; pooled 3.18 is 0.52 under.")

school("wesleyan", "Liberal arts; major not chosen",
  "Wesleyan could hold both your creative practice and your questions about society, and it meets full need with loan-free aid. "
  "You have not named a major, and its entry rules limit some majors for junior transfers.",
  "Choose the academic interest first, then write about what sustained study would add to work you already make.",
  "Creative work paired with a written argument about ownership and access, which suits a college that mixes art and critique.",
  "Open, interdisciplinary study and loan-free aid. Apply for aid with the application, because skipping it limits aid for a year.",
  15, "No official GPA line was found. A dated third-party estimate puts competitive transfers near 3.7, so this placement is low confidence.",
  "Line: none official; about 3.7 in a 2019 third-party estimate. You: SCAD 3.33, pooled 3.18.",
  "The portal asks for an area of academic interest and an additional one, and whether you intend to pursue financial aid.")

school("dartmouth", "Liberal arts; major not chosen",
  "Dartmouth could connect your hands-on design habits to sustained liberal-arts study in a small, close community. "
  "Most admitted transfers hold above a 3.7 and testing is required unless your veteran waiver is approved.",
  "Complete Service to School first, choose a major, and ask the veteran coordinator one question the website does not answer.",
  "A veteran builder with a faculty-endorsed campaign and design work that other students actually use.",
  "A tight residential community, unlimited Yellow Ribbon, and a veteran coordinator who works with applicants directly.",
  16, "Dartmouth says most admitted transfers hold above 3.7, and testing is required unless a veteran waiver is approved. You are about 0.4 to 0.5 under.",
  "Line: above 3.7 for most admits; testing required or waived. You: SCAD 3.33, pooled 3.18.")

school("amherst", "Black Studies within the Open Curriculum, target still to confirm",
  "Amherst's second essay asks directly for the life experiences that shaped you, which is material you have in depth. "
  "It expects 32 transferable liberal-arts credits and about an A-minus record, so credit classification and grades are the risk.",
  "Ask Amherst how many of your credits count as liberal arts, then write Essay 1 on your path and Essay 2 on one shaping experience.",
  "You have already spoken with Amherst admissions, and your story of service, setback and return fits its stated interest in personal context.",
  "An open curriculum with Black Studies, need-based aid, and a history of enrolling veterans.",
  17, "Amherst asks for 32 transferable liberal-arts credits and describes competitive transfers at about an A-minus average. Design studio credits may not count as liberal arts.",
  "Line: about A-minus, with 3.5 listed as a minimum in one profile, and 32 liberal-arts credits. You: SCAD 3.33, pooled 3.18.")

school("uchicago", "Sociology, the study of knowledge, or ethics; target still to confirm",
  "UChicago fits your appetite for big questions about how people decide what counts as knowledge. "
  "It publishes no GPA figure, advisers point to about 3.75, and every transfer must complete the Core.",
  "Pick the one extended-essay option you would enjoy arguing, and use the semantic-engine work as an example of interpretation going wrong.",
  "You would teach a class on the Many Worlds Interpretation and built a tool to compare ideas across traditions: real curiosity on record.",
  "Rigorous debate, a strong sociology tradition, unlimited Yellow Ribbon and loan-free aid for admitted transfers.",
  18, "UChicago publishes no transfer GPA. Advisory sources point to about 3.75 and transfers must complete the Core. You are roughly 0.4 to 0.6 under that estimate.",
  "Line: none official; about 3.75 in advisory sources. You: SCAD 3.33, pooled 3.18.")

school("nd", "College of Arts and Letters: Africana Studies, with the Tech Ethics minor",
  "Notre Dame matches your faith, service and veteran commitments more closely than any school on the list. "
  "Its recent admitted transfers averaged 3.75 or higher, which is the largest stated gap from your current record.",
  "Ground every short answer in one ordinary, checkable scene, and gather a syllabus for every college course now.",
  "Faith, service and veteran identity together, plus a stated aim of law school and veteran legal work.",
  "A mission built on service and the common good, a veterans law clinic, and aid that can cover full cost at your income level.",
  19, "Notre Dame says recent admitted transfers averaged 3.75 or higher. You are 0.42 under on SCAD and 0.57 under pooled.",
  "Line: 3.75 average for recent admits, 24 transferable credits. You: SCAD 3.33 is 0.42 under; pooled 3.18 is 0.57 under.")

school("usc", "Iovine and Young Academy: Arts, Technology and the Business of Innovation; Human Technology Interaction second",
  "The Iovine and Young Academy is the closest match to how you actually work: design, technology and enterprise together. "
  "USC's admitted transfers sit between 3.70 and 3.97, and the Academy's sequential degree can take three to four more years.",
  "Show one project with your role, the revision process and its limits, and work out the full time and cost before investing.",
  "A shipped client platform, 34 public repositories and an SMU financial technology certificate: evidence that you build and finish.",
  "It is the degree that looks most like your practice, with unlimited Yellow Ribbon for eligible veterans.",
  20, "USC's admitted transfer GPA range was 3.70 to 3.97 school-wide, not Academy-specific. You are below the bottom of that range and the degree is sequential.",
  "Line: 3.70 to 3.97 for admitted transfers. You: SCAD 3.33 is 0.37 under the bottom of the range.",
  "Your portal lists Arts, Technology and the Business of Innovation first and Human Technology Interaction second, and requires a portfolio.")

school("penn", "College of Arts and Sciences: Africana Studies or Philosophy, Politics and Economics; Science, Technology and Society third",
  "Penn makes you apply to one of its four undergraduate schools, and the College of Arts and Sciences is the one that fits Africana Studies, PPE or Science, Technology and Society. "
  "You have not opened the application yet, and its transfer essay asks why you are leaving SCAD and what you would gain at Penn.",
  "Pick the College and one major first, then build all three Penn essays on one question: who owns the value people create, studied through history and economics.",
  "A veteran with a fintech certificate and a written thesis on who owns AI, which gives PPE or Africana Studies a concrete research question.",
  "Unlimited Yellow Ribbon with Penn covering leftover tuition, a push to admit more veterans, and Philadelphia's civic and startup life.",
  21, "No GPA line is published, testing was required last cycle with no score on file for you, and Penn expects one to two years of transferable work with half the degree at Penn. On numbers alone it sits just above Princeton.",
  "Line: none published; testing required in 2025-26 with a hardship waiver. You: SCAD 3.33, pooled 3.18, no test score on file.",
  "Not opened yet.")

school("princeton", "African American Studies first and Sociology second in your portal, Entrepreneurship as the minor; ORFE and Computer Science also on your list",
  "Princeton recruits veterans into its transfer program and requires a graded paper, so the application rests on academic writing. "
  "Your portal now lists African American Studies and Sociology, which fits your record better than engineering or ORFE would.",
  "Settle the major order, secure a graded paper with its prompt and comments, and confirm your transferable credit count in writing.",
  "A veteran whose research questions about ownership, access and Black intellectual history already exist on paper.",
  "A transfer program built around veterans, independent research through the senior thesis, and aid that can replace benefits.",
  22, "No GPA line is published, but the academic bar is the highest on your list. Your contact questioned the transferable-credit count, and ORFE or engineering would need far more math and science than the record shows.",
  "Line: none published. You: SCAD 3.33, pooled 3.18; credit threshold and graded paper are the gates.",
  "Your portal shows African American Studies and Sociology as majors, Entrepreneurship as the minor, and drafts in progress for several answers.")
