"""Supplement prompts and five guidance points each: Brown through Vanderbilt.

Prompts are paraphrased from Kendren's November 10 screenshots unless marked otherwise.
Guidance organizes material and checks facts. It is never draft prose.
"""
SCREEN = "From your November 10 screenshot, paraphrased. Confirm wording in the live application."
OFFICIAL = "From the school's official page, not from a screenshot. Confirm in the live application."
MISSING = "Not captured: no screenshot was supplied and no wording is verified."
WORKBOOK = "From your older workbook. Confirm that the current application still asks this."

Q = {}

def add(sid, title, limit, status, prompt, guidance, prov=SCREEN, kind="essay"):
    assert len(guidance) == 5, (sid, title, len(guidance))
    Q.setdefault(sid, []).append({"title": title, "limit": limit, "status": status, "kind": kind,
                                  "prompt": prompt, "guidance": guidance, "provenance": prov})

# ------------------------------------------------------------------ Brown (Veterans Application)
add("brown", "Academic interests", "50 to 150 words", "Required",
    "Why are you drawn to the areas of study you listed, and how do your personal or professional experiences relate to them?",
    ["Your portal lists Science, Technology, and Society first and Social Analysis and Research second, so write to those two, not to computer science.",
     "Pick one experience that created the interest, such as a floor conflict or a canvassing conversation, and name it in one line.",
     "State the question you want to study in plain words: who is responsible when a system fails a person.",
     "At 150 words there is room for one experience and one question. Leave projects for the other answers.",
     "Check that the two interests you name here match the concentration plan in your Why Brown answer."])
add("brown", "Why Brown, and activities", "100 to 250 words", "Required",
    "Why are you considering Brown for the next step in your education? Beyond academics, which activities would you continue, expand or start at Brown?",
    ["Give one academic reason that only the Open Curriculum makes possible, such as pairing technology study with Africana or policy courses.",
     "Name the Center for Technological Responsibility only if you have read one piece of its work and can say what it found.",
     "The prompt asks about activities, so name what you would continue: residence mentoring, lacrosse, veteran community or a campus event like the Murph.",
     "Mention your conversation with Brown's veteran admissions contact only as how you learned something, not as an endorsement.",
     "Keep the binding option out of this answer. It is a decision for after you compare aid."])
add("brown", "Growing up and what you bring", "200 to 250 words; the field shows a 100-word minimum", "Required; limit conflict to resolve",
    "Share how one aspect of your growing up inspired or challenged you, and what unique contributions it might let you make to the Brown community.",
    ["Choose one aspect only. Your grandmother's conference for Black Christian women in St. Louis is a strong, specific candidate.",
     "Show a scene from it: what you saw adults organize, and what it taught you about institutions without walls.",
     "Link that to one thing you do now, such as running a floor or organizing an event, so the contribution is visible.",
     "The label says 200 to 250 words but the field shows 100 required. Write to 200 to 250 and ask Brown which is correct.",
     "Leave out the family-history claim about a president unless you hold proof."])
add("brown", "Military experience", "300 to 500 words", "Required",
    "How has your military experience contributed to your personal growth and future plans? You may reuse your Service to School VetLink Addendum response in whole or part.",
    ["State the facts exactly as your record shows: Army combat engineer training at Fort Leonard Wood, 2020 to 2021, about eight months.",
     "Your portal drafts mention entering as the pandemic began. Use that timing as the scene, and be exact about dates.",
     "Name two or three habits the training built, such as procedure, safety and accountability to teammates, with one example each.",
     "Connect service to your plan: protecting people from harmful technology, law school and possibly military legal work.",
     "Brown allows reuse of the VetLink Addendum, so write that addendum first with your Service to School mentor and adapt it here."])
add("brown", "Additional information", "150 words", "Optional",
    "Use this space for anything else you would like Brown to know.",
    ["Use it for the academic record: the Broward withdrawals and what was happening, in two or three factual sentences.",
     "State what changed: stable housing, a full course load at SCAD and the Dean's List.",
     "Decide in advance how much personal history you want to disclose. You can explain the record without every detail.",
     "Do not repeat anything already said in the other four answers.",
     "If the record is fully explained elsewhere, leaving this blank is acceptable."])
add("brown", "Video introduction", "90 seconds", "Optional and strongly encouraged",
    "A short video introduction submitted through the applicant portal.",
    ["It is an introduction, not a film project. One clean take in good light is enough.",
     "Say one thing the written answers cannot carry: how you sound, what you find funny, what you are curious about.",
     "Do not read your resume aloud or repeat an essay.",
     "Plan three beats and speak from notes instead of a script, so it sounds like you.",
     "Check the upload format and deadline in the portal before recording."],
    prov=OFFICIAL, kind="video")

# ------------------------------------------------------------------ Cornell ILR
add("cornell", "Educational path statement", "1,250 to 3,250 characters, about 250 to 650 words", "Required",
    "Discuss your educational path. How does continuing your education at a new institution help you achieve your future goals?",
    ["Lay out the path in order: Army, Broward, the interruption, nonprofit work, SCAD. One or two sentences each.",
     "Address the Broward withdrawals directly and briefly, then show the rising SCAD record as evidence of change.",
     "Name the future goal plainly: labor and technology policy, then law school.",
     "Say what a design school cannot give you: economics, labor law, statistics and policy study in one degree.",
     "Kyle told you a third of ILR graduates go to law school. Use what you learned on the call as knowledge, without quoting him as support."])
add("cornell", "ILR writing supplement", "650 words on the current ILR guidelines", "Required for ILR; confirm in portal",
    "Using your own experiences, explain the issues about work, employment or labor that you care about and how ILR's curriculum fits your interests.",
    ["Choose one work issue you have lived: canvassing pay and quotas, unrecognized residence-hall labor, or AI changing hiring.",
     "Describe one decision you made about people's work, such as how you trained newer recruiters, and its result.",
     "Connect it to a field ILR teaches: labor relations, organizational behavior, labor economics or law.",
     "Your resume describes resume.ai and COMMONS. Mention a tool only at the stage it has actually reached.",
     "ILR advisers asked for composition, statistics and microeconomics. Say which you are taking and when."],
    prov=OFFICIAL)

# ------------------------------------------------------------------ Notre Dame
add("nd", "Postgraduate goals and your Notre Dame journey", "500 words", "Required",
    "Knowing you are early in your college career, what are your current postgraduate goals, and what do you envision your academic journey at Notre Dame will look like as you pursue them?",
    ["Lead with the goal you told Notre Dame's veteran liaison: law school and work on veteran or technology policy.",
     "Name the college and major. Africana Studies in Arts and Letters is on file, with the Tech Ethics minor.",
     "Lay out a believable sequence: core courses, the major, the minor, then one experience such as the veterans law clinic.",
     "The IDEA Center is a resource, not a degree. Do not present it as your academic home.",
     "Notre Dame requires a syllabus for every college course, so keep the plan consistent with the courses you can document."])
add("nd", "Why are you seeking to transfer?", "50 to 100 words", "Required", "Why are you seeking to transfer?",
    ["Give one academic reason: you want liberal-arts study of ethics, society and law that a design school does not offer.",
     "Speak well of SCAD. Say what it gave you and what you now need next.",
     "One reason, stated once. There is no room for a list.",
     "Avoid prestige language. Name the kind of learning you want.",
     "Count the words. The field stops at 100."], kind="short")
add("nd", "Notre Dame's mission", "50 to 100 words", "Required", "What aspect of Notre Dame's mission most resonates with you?",
    ["Read the mission statement first and pick one phrase you can connect to something you did.",
     "Service to the common good fits your canvassing for child welfare, senior services and relief campaigns.",
     "Faith is part of your story through your grandmother's ministry. Mention it only if it is true to you now.",
     "Give one concrete example in a sentence, not a general statement about values.",
     "Do not restate the mission back to them. Show where it already appears in your life."], kind="short")
add("nd", "Challenge: initiative, humility and resilience", "50 to 100 words", "Required",
    "A transfer student needs initiative, humility and resilience. Share a time you faced a challenge and how you overcame it.",
    ["Choose one challenge. Losing the student government election and continuing to organize is specific and checkable.",
     "Returning to college after the Broward period is the larger story. Use it here only if it is not your main essay.",
     "Show humility with a fact: what you got wrong or had to learn.",
     "End on what you did next, not on how you felt.",
     "At 100 words, one situation, one action and one result is the whole answer."], kind="short")
add("nd", "Community", "50 to 100 words", "Required",
    "Community is the cornerstone of Notre Dame. Tell us about a time you created or contributed to a community.",
    ["The Murph challenge with Club SCAD that grew into a residence-hall event is a clear case of creating community.",
     "Give a number or a visible result: how many took part, or what happened the following term.",
     "Name your exact role. Say organized or helped organize, whichever is true.",
     "Use a different example from the challenge answer so the four short answers cover four sides of you.",
     "Confirm the hall name and dates against your records before you submit."], kind="short")
add("nd", "Additional information", "300 words", "Optional; answer yes or no first",
    "Describe circumstances or qualifications not reflected elsewhere, including disruptions or hardships that affected your education, health, safety or family.",
    ["This prompt names hardship directly, so it is the right place for the Broward withdrawals and the housing instability behind them.",
     "Write it as facts with dates: what happened, which terms were affected, what you did about it.",
     "Share only what you are comfortable having in your file. Treatment details are optional.",
     "Close with evidence of stability: full-time enrollment, Dean's List and a residence mentor role.",
     "Keep the tone informational. The essays carry the reflection."], kind="context")

# ------------------------------------------------------------------ Yale (Eli Whitney)
add("yale", "Eli Whitney essays", "Not captured", "Application not opened yet",
    "Yale's Eli Whitney application has its own essay questions. Open the application and capture them before drafting.",
    ["Open the Eli Whitney application and screenshot every question. Yale lists personal statements, recommendations and transcripts, with a March 1 deadline for the application.",
     "Yale's contact asked for recent English and math coursework. Plan the essays around a record that includes them.",
     "Prepare a dated education timeline, because Eli Whitney asks you to account for time away from school.",
     "Choose one analytical paper to anchor your academic case, and keep the instructor's comments.",
     "Decide whether 2027 or 2028 is the right cycle before you invest in these essays."],
    prov=MISSING, kind="pending")

# ------------------------------------------------------------------ Princeton
add("princeton", "Academic areas and Princeton programs", "About 250 words", "Required; your draft is in progress",
    "Princeton lets students explore across the humanities, arts, sciences and social sciences. Which academic areas most spark your curiosity, and how do Princeton's programs suit those interests?",
    ["Your portal lists African American Studies, Sociology and Entrepreneurship. Write to those, and settle where ORFE stands before you submit.",
     "Your draft starts from identity and ancestry. Add the academic side: a question, a method and two named Princeton offerings.",
     "Name specific things you have read about, such as a course, the Center for Information Technology Policy, or the senior thesis.",
     "Connect one piece of your own writing, such as the Ownership of Intelligence argument, to what you would study.",
     "Proofread closely. The current draft has many typing errors that would distract a reader."])
add("princeton", "Lived experience and campus conversations", "400 to 500 words", "Required; your draft is about 300 words",
    "Reflect on how your lived experiences will shape the conversations you have in class, the dining hall and other spaces. What lessons have you learned so far, and what will classmates learn from you?",
    ["The prompt has three parts: your experience, the lessons, and what classmates will learn. Answer each one explicitly.",
     "Your draft has strong feeling about not giving up. Anchor it in one real event with a date and place.",
     "Pick two lessons at most and show how each came from something that happened.",
     "For what classmates will learn, name something concrete: how a veteran, a mentor or a first-contact resident assistant sees a problem.",
     "You are at about 300 of 400 to 500 words. Use the remaining space for the event and the classmates part, not for more reflection."])
add("princeton", "Service and civic engagement", "About 250 words", "Required; your draft is about 240 words",
    "Princeton has a longstanding commitment to service and civic engagement. How does your own story intersect with these ideals?",
    ["Lead with service you can document: Army training, eleven months of nonprofit canvassing and residence mentoring.",
     "Your draft says you joined wanting to save the world as the pandemic began. Keep that and make the dates exact.",
     "Remove or prove the claim about descending from the eighth president. Standard histories list only sons for Martin Van Buren.",
     "Show one act of service at human scale: one person you helped and what changed for them.",
     "End with what civic work you would do at Princeton or after, tied to law or policy."])
add("princeton", "A new skill you want to learn", "About 50 words", "Required; your draft is about 60 words",
    "What is a new skill you would like to learn in college?",
    ["Name one concrete skill in the first sentence, such as archival research, statistics or a language.",
     "Your draft describes holding many humanities in view. Turn that into a skill someone could teach you.",
     "Say why in one sentence, linked to something you want to make or study.",
     "Trim to about 50 words. You are slightly over.",
     "It can be light. A real, specific skill reads better than a grand one."], kind="short")
add("princeton", "What brings you joy", "About 50 words", "Required; draft in progress",
    "What brings you joy?",
    ["Your draft names experiences, travel, good energy and family security. Pick one and show it.",
     "The line about sitting with people who believed in you is the most specific. Build on that.",
     "Use a detail a reader can picture, such as a place, a meal or a game.",
     "Keep it to about 50 words and one idea.",
     "This answer should sound relaxed. It is where your personality comes through."], kind="short")
add("princeton", "Soundtrack of your life right now", "About 50 words", "Required; your draft is about 91 words",
    "What song represents the soundtrack of your life at this moment?",
    ["Check the artist credit. The well-known recording of Tek It is by Cafune.",
     "Give the song and artist first, then one sentence on why it fits this moment.",
     "Your draft runs about 91 words. Cut it to about 50.",
     "Your USC answer names Sweater Weather. The two schools can differ, but make sure each is true.",
     "Tie the song to a present feeling, such as ambition you are learning to pace."], kind="short")
add("princeton", "Gaps and timeline", "About 150 words", "Required if you had interruptions",
    "If you have had interruptions or gaps in your education, or left a school voluntarily, explain the timeline of your post-secondary career. A resume is also welcome.",
    ["Answer yes. Then give a dated list: high school graduation, Army 2020 to 2021, Broward, the gap, nonprofit work in 2025, SCAD from spring 2026.",
     "Use month and year for each entry and check them against transcripts and service records.",
     "State reasons in a few neutral words per gap. The detail belongs in the personal essay if you want it there.",
     "Princeton also lets you upload a resume or timeline. Make sure it matches this answer exactly.",
     "Include the withdrawn Broward terms. Leaving them out would look worse than explaining them."], kind="context")
add("princeton", "Plans during and after college", "About 150 words", "Required",
    "What are your plans during and after your higher education experience?",
    ["During: the major, a thesis question and one or two commitments such as the veteran community or lacrosse.",
     "After: law school, and the kind of work you want, such as technology policy or military legal service.",
     "Keep it consistent with the majors in your portal. Entrepreneurship can appear as the minor.",
     "One plan stated clearly is stronger than four possibilities.",
     "Avoid promising outcomes. Say what you intend to study and attempt."], kind="short")
add("princeton", "Graded written paper", "One paper, with the prompt, grade and comments", "Required",
    "Submit a graded academic paper from a course, uploaded as the Writing Sample or sent before the March 1 deadline.",
    ["The New Digital Toll was graded in a business class. Ask Princeton in writing whether a business-course paper qualifies.",
     "Princeton prefers expository, thesis-driven writing. Check your paper against that before choosing it.",
     "Include the assignment prompt, the grade and the instructor's comments, as the requirement asks.",
     "If no current paper fits, plan a writing-intensive course whose graded paper you can use.",
     "Submit the paper as it was graded. Do not revise it afterward."], kind="document")
add("princeton", "Transfer personal essay", "About 650 words", "Required",
    "Write an essay addressing your reasons for transferring and your desired objectives.",
    ["Structure it in three parts: where you have been, why SCAD is no longer enough, what you would do at Princeton.",
     "Give academic reasons for leaving: you want research, writing and social science that a design degree does not include.",
     "Name two or three Princeton specifics tied to your majors, including independent work.",
     "This is the place for your full path, including the interruption, told once and plainly.",
     "Princeton also accepts military papers and an optional information upload. Use those for documents, not for more essay."])

# ------------------------------------------------------------------ Tufts (REAL)
add("tufts", "How you learned about and engaged with Tufts", "450 to 650 characters", "Required",
    "Describe how you have learned about and engaged with Tufts during your college search.",
    ["List only engagement that happened. Do not claim a visit, event or conversation that did not.",
     "Before writing, attend one REAL information session and send one real question to the REAL office.",
     "Say what you learned from each step that changed your plan.",
     "This is characters, not words. 650 characters is about 100 words.",
     "Tufts records legitimate contact, so what you write should match what their records show."], kind="short")
add("tufts", "Academic path, REAL and goals", "2,500 to 3,500 characters", "Required",
    "Address three things: your academic path from high school to today, your interest in Tufts and the REAL program, and your academic interests and goals.",
    ["Use the three parts as three sections so nothing is missed.",
     "Path: give the sequence with dates, including the Broward period, and what changed by the time you reached SCAD.",
     "REAL: say why an adult pathway with its own advising fits you, using what you learned from the information session.",
     "Goals: name an Arts and Sciences major such as sociology or Science, Technology and Society. REAL does not cover the BFA.",
     "The application also asks about disciplinary and criminal history. Answer those questions accurately and separately."])

# ------------------------------------------------------------------ WashU
add("washu", "What you want to study and why", "About 250 words, 1,750 characters", "Required",
    "Tell us what you are interested in studying at college and why.",
    ["Name the major: Sociology or Philosophy-Neuroscience-Psychology in Arts and Sciences.",
     "Start from one design decision that taught you something about how people actually behave.",
     "Say which questions the major would let you ask that design alone cannot.",
     "Mention the computational AI minor only if you have checked that transfers can take it.",
     "Keep computer science out of the first line. It is a tool here, not the subject."])
add("washu", "Why transfer to WashU", "About 250 words, 1,750 characters", "Required",
    "Tell us why you would like to transfer to WashU.",
    ["Your family tie to St. Louis through your grandmother's conference is specific and true. Use it in a sentence or two.",
     "Give two academic reasons tied to named WashU offerings you have read about.",
     "Explain what SCAD gave you and what you need that it does not offer.",
     "Location supports the case. Academics should carry it.",
     "Check that this answer does not repeat the study answer above."])
add("washu", "Personal statement", "Up to 650 words, 3,250 characters", "Required; choose one Common App prompt",
    "Choose one of the seven standard prompts (background or identity, a challenge, a belief you questioned, gratitude, a period of growth, an engaging idea, or your own topic) and write on it.",
    ["Pick the prompt after choosing the story, not before.",
     "The same statement can serve UNC, Rice and UChicago, which use the same prompt list. Write it once and write it well.",
     "A challenge or growth prompt fits your return to college. An engaging-idea prompt fits your ownership-of-AI argument.",
     "Use one scene, one turning point and one changed understanding.",
     "WashU says 650 words is a limit, not a goal. Stop when the story is told."])

# ------------------------------------------------------------------ Northwestern
add("nu", "Background and how you will engage", "Fewer than 300 words", "Required",
    "What aspects of your background (identity, school setting, community, household) have most shaped how you see yourself engaging in Northwestern's community?",
    ["Choose one or two aspects. Veteran, residence mentor and grandson of a community organizer are each enough alone.",
     "Show the background through something you did, such as handling a floor conflict before it reached staff.",
     "The prompt asks how you would engage. Name where: a residential community, a student group or a civic project.",
     "Keep it under 300 words and avoid repeating the transfer answer.",
     "Northwestern says essays may be repurposed, so a strong paragraph from another school can be adapted."])
add("nu", "Why transfer to Northwestern", "Fewer than 300 words", "Required",
    "Share why you would like to transfer to Northwestern.",
    ["Choose the school first: Education and Social Policy or Weinberg. The reason depends on it.",
     "Name the major and one or two courses or programs you have actually looked at.",
     "Segal Design Institute and The Garage are resources. Cite them as resources, not as your degree.",
     "Explain the academic step from design practice to studying people, organizations and policy.",
     "Do not mention the binding transfer option unless you have decided to use it."])
add("nu", "Optional personal essay or extra information", "Optional upload; confirm limit", "Optional",
    "Northwestern welcomes, but does not expect, a personal essay or other information not covered by its two questions.",
    ["Northwestern says it does not expect this. Submit only if it adds something new.",
     "Your Common App personal statement is the natural piece to include.",
     "It is also a reasonable place for a short, factual note on the Broward record.",
     "Do not send a portfolio or research paper here unless the portal asks.",
     "If the two required answers already tell the story, skip it."], kind="optional")

# ------------------------------------------------------------------ Georgetown
SCREEN11 = "From your November 11 Georgetown screenshots, paraphrased. Confirm wording in the live application."
add("gt", "Short answer: a different viewpoint", "250 words", "Required for all applicants",
    "Everyone deals with people who hold viewpoints different from their own. Describe one such experience and what you learned from it.",
    ["Pick one real exchange with a named setting: a canvassing door, a floor conflict as mentor, or a debate in Ethics of Emerging Technology.",
     "The learning is the point. Spend about half the words on what changed in how you think or act, not on who was right.",
     "Show you can state the other person's view fairly in one sentence before you give yours.",
     "Avoid a political hot-button unless the lesson is about listening. Georgetown reads this as a test of civil disagreement.",
     "At 250 words there is room for one scene and one lesson. Cut background that does not serve either."],
    prov=SCREEN11, kind="short")
add("gt", "Essay One: who you are, and why you are transferring", "About one page, single-spaced, uploaded", "Required for all applicants",
    "Georgetown is a diverse community and wants to know you in your own words. Write a brief personal or creative essay that best describes you and reflects your background, experiences, skills and talents. Because you are transferring from a four-year school, include your reasons for transferring.",
    ["SCAD is a four-year school, so the transfer reasons are required here, not optional.",
     "One page single-spaced is roughly 500 to 600 words. Draft to that length and check it in the upload format.",
     "Give the move a reason Georgetown answers: the School of Foreign Service joins technology with policy and law, which a design degree does not.",
     "Background, skills and talents can come from one thread: service, the shift to combat medic, canvassing, mentoring, then design and AI ethics.",
     "Personal or creative form is allowed. A creative form still needs the transfer reasons stated plainly somewhere."],
    prov=SCREEN11, kind="essay")
add("gt", "Essay Two: why international affairs and global service", "About one page, single-spaced, uploaded", "Required for School of Foreign Service applicants",
    "The Walsh School of Foreign Service was founded more than a century ago to prepare leaders with the skills to address global issues. Describe your main motivations for studying international affairs at Georgetown and for dedicating your undergraduate study to a future in global service.",
    ["This essay exists only for the School of Foreign Service. Confirm SFS, and Science, Technology and International Affairs, is your choice before writing it.",
     "Name a global problem you already work on in miniature: AI pricing and access, technology governance, or veteran resources.",
     "Your Winter Military World Games studio is a live international example. Mention it only after it starts, and only what you actually did.",
     "Say what global service means for you concretely, such as military legal work or technology policy, and keep it consistent with your law-school goal.",
     "Show you know the degree asks for economics, statistics and a language, and state your plan for each."],
    prov=SCREEN11, kind="essay")
add("gt", "Attended more than one college", "Upload; no limit shown", "Applies to you: Broward and SCAD",
    "If you attended more than one college before applying to Georgetown, explain.",
    ["Keep it factual and short: dates, schools, why you moved, and what changed.",
     "Broward: Spring 2024 to Fall 2024, 22 credits, 3.04. SCAD: from Spring 2026, 3.33 with Fall midterms of A, A and A.",
     "Address the Fall 2024 withdrawals in one or two sentences, with the context you choose to share.",
     "End on the upward trend, since the record already shows it.",
     "Do not repeat Essay One here. This is an explanation, not a story."],
    prov=SCREEN11, kind="context")
add("gt", "Coursework, aid and disciplinary questions", "Form fields", "Required",
    "List the courses you will take this year at your current school, with course numbers, titles and credits; say whether you will apply for financial aid and who is responsible for your costs; mark any aid you receive now; and answer the disciplinary questions.",
    ["Fall 2026: AI 101 Survey of AI Applications, DIGI 230 Ethics of Emerging Technology, FOUN 112 Color in Context, 5 quarter hours each.",
     "Winter 2027: PRO 560 SCADpro Research, PRO 580 SCADpro Deloitte LA28, PRO 580 SCADpro Military World Games. Confirm credit hours on your registration.",
     "The form label says Spring 2027 entry. Ask Georgetown whether fall applicants list the same terms, and note the quarter system.",
     "Mark current aid exactly as SCAD and the VA pay it now, such as government funded, grant or loan.",
     "Answer the disciplinary questions truthfully and keep the wording identical across every application."],
    prov=SCREEN11, kind="form")
add("gt", "Not currently in school", "Upload", "Does not apply: you are enrolled",
    "Applicants not attending college now describe their activities since their last academic work.",
    ["You are enrolled at SCAD, so leave this blank.",
     "If you take a term off before applying, this becomes required.",
     "The gap between the Army and Broward is covered by your timeline elsewhere, not here.",
     "Keep the 2022 to 2023 security job and 2025 canvassing on the activities and employment pages.",
     "Recheck this before submitting in case your enrollment changes."],
    prov=SCREEN11, kind="context")

# ------------------------------------------------------------------ Vanderbilt
add("vandy", "Dare to grow: identity and community", "About 250 words, 2,000 characters", "Required",
    "Reflect on how one or more aspects of your identity, culture or background has shaped your personal growth, and how it will contribute to the campus community as you dare to grow at Vanderbilt.",
    ["Choose one aspect and one period of growth. Veteran identity or your family's community work both fit.",
     "Show growth with a before and an after: what you believed, what happened, what you do differently.",
     "The prompt asks what you will contribute. Name something specific, such as peer mentoring or organizing.",
     "Tie the growth to people and organizations, since that is what your intended major studies.",
     "Keep this distinct from the transfer essay. This one is about you. That one is about the move."])
add("vandy", "Transfer personal essay", "250 to 650 words, uploaded as a document", "Required",
    "Provide a personal essay addressing your reasons for transferring and the objectives you hope to achieve.",
    ["Write to Peabody and Human and Organizational Development by name. This is not a computer science application.",
     "Give the reason for moving: you want to study how organizations work, which a design degree does not teach.",
     "List two or three objectives, such as specific coursework, a research question and preparation for law school.",
     "Use one experience of leading peers as evidence that the interest is real.",
     "The same core essay serves UVA and Wesleyan, which ask nearly the same question. Adjust the school details for each."])
add("vandy", "Additional information", "6,500 characters", "Optional",
    "Provide details of circumstances or qualifications not reflected elsewhere in the application.",
    ["Use it for a short, dated explanation of the Broward withdrawals.",
     "Add anything a reader needs to understand quarter credits or the military transcript.",
     "The limit is large. A few clear sentences are better than filling it.",
     "Do not paste a second essay here.",
     "The College Report must come from a college official. Request it early."], kind="context")
