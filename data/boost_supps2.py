"""Supplement prompts and five guidance points each: Williams through UChicago, plus the reserve bench."""
from boost_supps1 import add, Q, SCREEN, OFFICIAL, MISSING, WORKBOOK

COMMON_PROMPTS = ("Choose one of the seven standard prompts (background or identity, a challenge, a belief you questioned, "
                  "gratitude, a period of growth, an engaging idea, or your own topic) and write on it.")

# ------------------------------------------------------------------ Williams
add("williams", "Personal essay", "4,000 characters, about 600 to 700 words", "Required",
    "Williams students thrive when engaged in academic and cocurricular life. Share how your prior experiences have informed your interests and how you hope to pursue them in and out of the classroom.",
    ["The prompt asks for both sides: in the classroom and outside it. Give each a clear section.",
     "Choose two or three experiences that led to an interest, such as mentoring leading to questions about institutions.",
     "Name the academic direction. Africana Studies and Cognitive Science are on file. Confirm which you want.",
     "For outside the classroom, name what you would join or start, such as the veteran community or lacrosse.",
     "Williams reads recent coursework most heavily, so mention the courses that show where you are now."])
add("williams", "Optional academic writing sample", "Up to 8,000 characters; include the assignment", "Optional",
    "If you write best in an academic essay, submit a paper on any topic. It need not be graded and may be handwritten in class. No lab reports. Include the assignment or prompt.",
    ["This is worth sending. Williams values analytical writing and your narrative essays lean personal.",
     "A humanities-style paper fits best. Check whether your business-course paper reads as analysis.",
     "Attach the assignment description, as the instructions require.",
     "Send it as written. Fix nothing after grading except obvious typing errors if the school allows.",
     "Upload it under Documents in the Williams application, not in the essay box."], kind="document")
add("williams", "Additional information", "4,000 characters, about 600 to 700 words", "Optional",
    "Provide details about circumstances or qualifications not reflected elsewhere in the application.",
    ["Williams says high school performance may not show your ability and that recent work counts most. Use that framing.",
     "Explain the Broward terms in dated, factual sentences.",
     "Note that SCAD uses quarter credits and that the military transcript carries ACE credit recommendations.",
     "Ask how the two-year residence rule affects you before deciding sophomore or junior entry.",
     "The College Report is sent by email from a college official. Arrange it early."], kind="context")

# ------------------------------------------------------------------ Wesleyan
add("wesleyan", "Reasons for transferring and objectives", "250 to 650 words", "Required",
    "Provide a statement that addresses your reasons for transferring and the objectives you hope to achieve.",
    ["Choose your area of academic interest first. The portal asks for it and the essay should match.",
     "Junior transfers can be shut out of Economics, Psychology, Film, the College of Letters and the College of Social Studies. Check before you name one.",
     "Give the academic reason for leaving a design school: you want critical and social study alongside making.",
     "List two or three objectives a reader could check later, such as a major, a thesis topic and a campus role.",
     "Answer yes to the financial aid question if you need aid. Skipping it blocks Wesleyan aid for your first year."])

# ------------------------------------------------------------------ Amherst
add("amherst", "Essay 1: educational journey and why Amherst", "250 to 650 words, 4,000 characters", "Required",
    "Tell us about your educational journey, including your objectives in transferring, and reflect on your reasons for considering Amherst as your next institution.",
    ["Cover three things in order: the journey, the objectives and why Amherst.",
     "Tell the journey with dates and one honest sentence on the interruption.",
     "For objectives, name what you want to study. Black Studies is on file. Confirm it.",
     "For Amherst, cite the open curriculum and something you learned in your conversation with admissions.",
     "Amherst says each essay should carry a distinct theme. Keep life circumstances for Essay 2."])
add("amherst", "Essay 2: experiences that shaped you", "250 to 650 words, 4,000 characters", "Required",
    "Describe the life experiences and personal circumstances that have most affected you as a student, community member and person. How have they influenced who you are today?",
    ["The prompt names three roles: student, community member and person. Touch each one.",
     "This is the right place for the hard period, told at the level of detail you choose.",
     "Pick two experiences at most. Your grandmother's ministry and your return to school after service pair well.",
     "Show the influence through present behavior, such as how you handle a resident in crisis.",
     "Do not repeat the timeline from Essay 1. This essay is about meaning, not sequence."])
add("amherst", "Optional analytical writing sample", "One recent course paper", "Optional",
    "You may upload a recent academic essay or paper prepared for a course under the Writing Sample tab.",
    ["Send one if you have a strong analytical paper. It supports readiness for a writing-heavy college.",
     "It must be written for a course, so an independent draft does not qualify.",
     "Choose the paper with the clearest argument, not the longest one.",
     "The College Report and Mid-Term Report go by email or the status portal, not on this page.",
     "Official transcripts from every college and your high school are required separately."], kind="document")

# ------------------------------------------------------------------ USC (Iovine and Young Academy)
add("usc", "How you will pursue your academic interests", "About 300 words, 2,000 characters", "Required",
    "Describe how you plan to pursue your academic interests. You may address your first- and second-choice majors.",
    ["Your portal lists Arts, Technology and the Business of Innovation first and Human Technology Interaction second. Address both.",
     "Say what you would study in each and how the second choice still serves the same question.",
     "Use one project as evidence, with your role and what you learned from revising it.",
     "Show you understand the Academy's sequential structure and the time it adds.",
     "Keep claims at the stage each project has reached: built, tested or proposed."])
add("usc", "Reasons for transferring and how USC supports your goals", "About 300 words, 2,000 characters", "Required",
    "Provide a statement addressing your reasons for transferring and how USC will support both your academic and personal goals.",
    ["The prompt asks about academic and personal goals. Give each its own paragraph.",
     "Academic: name what the Academy combines that SCAD separates.",
     "Personal: veteran community, mentoring and building things with other people.",
     "Cite one USC resource you have read about and what it does.",
     "Do not lean on reputation or location. Say what you would do there."])
add("usc", "A disagreement about something important", "About 250 words, 1,500 characters", "Optional",
    "Describe a time you disagreed with someone you know about something important to you. Did you change your mind or reach common ground?",
    ["Use only a disagreement that happened. Do not invent one.",
     "A dispute over how to run an event, train recruiters or handle a resident would work.",
     "Give the other person's view fairly before your own.",
     "Say clearly whether you changed your mind, they did, or you met in the middle.",
     "It is optional. If no real example fits, leave it out."], kind="optional")
add("usc", "Gaps in enrollment", "2,500 characters", "Required if you had a fall or spring term out of school",
    "Starting with the beginning of high school, if you had a gap where you were not enrolled during a fall or spring term, address it. Summers do not count.",
    ["Write a dated list from high school onward, term by term.",
     "Cover Army training in 2020 to 2021, the time after Broward, and 2025 before SCAD.",
     "Give a short factual reason for each gap.",
     "Match these dates to your Princeton and UVA gap answers exactly.",
     "USC requires transcripts from every college, including terms with only withdrawals. Send them all."], kind="context")
add("usc", "Terms below full-time", "About 250 words, 2,500 characters", "Required for each light term",
    "For each college term (not summer) in which you took fewer than four semester courses or three quarter courses, briefly explain why you could not enroll full time.",
    ["Go through both transcripts and list every term under the threshold.",
     "The Broward withdrawals probably created light terms. Explain each in one sentence.",
     "State facts and circumstances without blame.",
     "Note that your SCAD terms were full, at 15 quarter hours each.",
     "Do not guess. Use the transcripts to count courses per term."], kind="context")
add("usc", "Academy portfolio in SlideRoom", "Confirm current requirements", "Required for the Academy",
    "The Academy requires its own supplement and portfolio through SlideRoom in addition to the Common App.",
    ["Open SlideRoom and capture the current essay prompts, because the older workbook wording may have changed.",
     "Lead with one case study: the problem, your role, the process, what changed and what failed.",
     "Use work with real users, such as the residence-hall floor plans or the client platform.",
     "Up to four optional pieces is a ceiling. Two strong ones beat four uneven ones.",
     "Credit collaborators and label AI-assisted work honestly."], prov=OFFICIAL, kind="portfolio")
add("usc", "Academy essay: what you contribute to a team", "About 500 words in your older workbook", "Confirm in SlideRoom",
    "The Academy is a group of innovators, technologists, builders and designers who collaborate. Describe what you would contribute.",
    ["Use one real team: the canvassing crew, a residence-life staff or a SCAD project group.",
     "Name your usual role on a team and give an example of it.",
     "Include a time collaboration was hard and what you did.",
     "Your workbook says this needs one true mentoring example. Choose it before writing.",
     "Confirm the prompt and limit in the current application first."], prov=WORKBOOK)
add("usc", "Academy essay: areas of expertise", "About 300 words in your older workbook", "Confirm in SlideRoom",
    "Select the areas of expertise that interest you (options have included extended reality, transformative AI and the business of innovation) and explain why.",
    ["Choose areas you can back with work, such as transformative AI.",
     "Give one piece of evidence per area.",
     "Say what you do not know yet and want to learn.",
     "Keep it consistent with your two major choices.",
     "Confirm the current list of options, which may have changed."], prov=WORKBOOK)
add("usc", "Academy external-transfer essay", "About 600 words in your older workbook", "Confirm in SlideRoom",
    "An essay for external transfer applicants about why the Academy and why now.",
    ["Explain why you would start a sequential program that may take three to four years.",
     "Show the finish date and how benefits and aid cover it.",
     "Say what the cohort model offers that you cannot get by staying at SCAD.",
     "Confirm with the Academy that outside transfers are admitted to your chosen degree this cycle.",
     "Verify the prompt before drafting. This wording comes from an older workbook."], prov=WORKBOOK)
add("usc", "Academy introduction video", "60 seconds on the current official page", "Confirm in SlideRoom",
    "A short video introducing yourself to the Academy.",
    ["Plan three beats: who you are, what you make, what you want to learn.",
     "Show something you built on screen if the rules allow it.",
     "Record in one take with clear sound.",
     "Do not repeat your essays.",
     "Confirm the length and format in SlideRoom before recording."], prov=OFFICIAL, kind="video")
_quick = "Quick answer on the USC questions page."
def quick(title, prompt, g):
    add("usc", title, "A few words; check the field", "Required quick answer", prompt, g, kind="quick")
quick("Three words that describe you", "Describe yourself in three words.",
      ["Your portal shows Faithful and Happy as the second and third words. Confirm the first.",
       "Choose words your recommenders would also use about you.",
       "Make sure the three words are not near-synonyms.",
       "Each word should show up somewhere else in the application as an action.",
       "Ask someone who knows you whether the three sound like you."])
quick("Favorite snack", "What is your favorite snack?",
      ["Answer honestly and specifically. A brand or a place is better than a category.",
       "This is meant to be light. Do not try to make it impressive.",
       "A snack tied to St. Louis, Texas or family adds a little of your story.",
       "Keep it to a few words.",
       "It is blank in your portal now, so fill it before submitting."])
quick("Best movie of all time", "What is the best movie of all time?",
      ["Pick the movie you would defend in conversation, not the one that sounds smartest.",
       "Just the title is fine.",
       "It can echo your other answers, since you chose Miles Morales as a roommate.",
       "Avoid repeating a title you use for the TV or book answer.",
       "It is blank in your portal now."])
quick("Dream job", "What is your dream job?",
      ["Your portal says Tech Founder. Check that it sits well beside the law school goal in your other applications.",
       "A more specific version says what you would found and for whom.",
       "It should match the first-choice major.",
       "Keep it to a few words.",
       "Be ready to explain it in the video or essays."])
quick("Theme song", "If your life had a theme song, what would it be?",
      ["Your portal says Sweater Weather. The band spells its name The Neighbourhood.",
       "Your Princeton answer names a different song. That is fine as long as each is true.",
       "Give the title and artist only.",
       "Choose a song you would be glad to talk about.",
       "Check the spelling of the title and artist."])
quick("Dream trip", "What is your dream trip?",
      ["Name a real place and, if space allows, one reason.",
       "Your Princeton draft says travel brings you joy, so this can connect.",
       "SCAD's Lacoste campus came up in your Rice draft. Use it only if it is your real dream trip.",
       "Keep it to a few words.",
       "It is blank in your portal now."])
quick("Next show to binge", "What TV show will you binge watch next?",
      ["Your portal says How to Get Away with Murder, which fits an interest in law.",
       "Capitalize the title properly.",
       "Any honest answer works here.",
       "Do not overthink the signal it sends.",
       "Keep it different from the movie answer."])
quick("Ideal roommate", "Which well-known person or fictional character would be your ideal roommate?",
      ["Your portal says Miles Morales. It is specific and shows personality.",
       "If there is room, add a few words on why.",
       "Check the spelling of the name.",
       "A fictional character is allowed, so this works as written.",
       "Make sure the choice still feels true when you submit."])
quick("Favorite book", "What is your favorite book?",
      ["Your portal says Think and Grow Rich. The author is Napoleon Hill, so fix the spelling.",
       "For an arts and technology program, consider whether a book closer to your research interests is also true for you.",
       "Choose a book you have finished and can discuss.",
       "Title and author only.",
       "Use the same favorite across schools unless a prompt asks something different."])
quick("A class you would teach", "If you could teach a class on any topic, what would it be?",
      ["Your portal says the Many Worlds Interpretation, which shows real curiosity.",
       "Give it a course title a student would sign up for.",
       "Be ready to explain the idea in two plain sentences if asked.",
       "It pairs well with your UChicago application, where curiosity is the point.",
       "Check that the spelling of Interpretation and the abbreviation are right."])

# ------------------------------------------------------------------ SMU
add("smu", "Optional transfer essay", "Not captured", "Optional; no screenshot yet",
    "SMU says a personal essay, resume and recommendations are optional and encouraged for scholarship review. Capture the current wording before drafting.",
    ["Submit it. SMU says optional materials are considered for scholarships, and a scholarship is your condition for attending.",
     "Mention the SMU financial technology certificate you already completed.",
     "Name the degree, Creative Computing or an alternate, and why it fits.",
     "Ask your transfer counselor which materials affect merit awards.",
     "Take a screenshot of the essay prompt so this entry can be replaced with the real one."],
    prov=MISSING, kind="pending")

# ------------------------------------------------------------------ UNC
add("unc", "Personal statement", "1,250 to 3,250 characters, about 250 to 650 words", "Required; choose one Common App prompt",
    COMMON_PROMPTS,
    ["Your screenshot shows only the personal statement. UNC's official page also lists no extra short answers this cycle.",
     "Write one statement for UNC, Rice, WashU and UChicago, since all four use this prompt list.",
     "The limit is in characters. 3,250 characters is roughly 500 to 650 words.",
     "Choose a story that shows something the transcript cannot.",
     "UNC wants later updates through its applicant portal, not by email."])

# ------------------------------------------------------------------ UVA
add("uva", "Time not enrolled since high school", "800 characters", "Required if applicable",
    "Provide details about any period when you were not enrolled in college courses since you graduated from high school.",
    ["800 characters is about 130 words, so use a dated list.",
     "Cover Army training, the time after Broward and 2025.",
     "Give a reason of a few words for each period.",
     "Keep the dates identical to your USC and Princeton answers.",
     "Save explanation and reflection for the transfer statement."], kind="context")
add("uva", "Reasons for transferring and objectives", "4,000 characters, about 600 to 700 words", "Required",
    "Provide a statement that addresses your reasons for transferring and the objectives you hope to achieve.",
    ["Name the College of Arts and Sciences and a major: Media Studies, Sociology or Psychology.",
     "The BS in Data Science does not take outside transfers. Mention only the minor, and only if you qualify.",
     "Give the reason for leaving a design school in academic terms.",
     "State two or three objectives, including preparation for law school.",
     "UVA says it does not want extra materials. Put everything that matters in this statement."])

# ------------------------------------------------------------------ Rice
add("rice", "Personal statement", "1,250 to 3,250 characters, about 250 to 650 words", "Required; your draft has 23 words",
    COMMON_PROMPTS,
    ["Your portal shows the problem-you-would-like-to-solve option selected and a one-line start.",
     "If you keep that prompt, name one problem, say why it matters to you and list the steps you took or would take.",
     "The underserved-communities theme in your other Rice answers could be that problem. Make it one concrete case.",
     "The same statement can go to UNC, WashU and UChicago.",
     "Replace the opening line about the universe with a specific scene."])
add("rice", "Academic interests and long-term goals", "150 words; field allows about 1,000 characters", "Required; your draft is 42 words",
    "How do you hope to explore your selected academic interests, and in what ways will this academic journey shape and support your long-term goals?",
    ["Name the major you selected. Social Policy Analysis or Cognitive Sciences are your candidates.",
     "Your draft speaks of serving underserved people and preserving cultures. Add how: which courses or methods.",
     "State the long-term goal in one sentence, such as law and technology policy.",
     "You have room to grow this from 42 words toward 150.",
     "Fix spelling before you save. The current draft has several errors."], kind="short")
add("rice", "Beyond academics, why Rice", "150 words; field allows about 1,000 characters", "Required; your draft is 52 words",
    "In addition to academics, why are you interested in transferring to Rice?",
    ["Being closer to home and friends in Texas is a real reason. Keep it and say it plainly.",
     "Add one reason about Rice itself, such as the residential colleges or the veteran association.",
     "Your draft mentions alumni and customs. Replace general praise with one tradition you have read about.",
     "This answer is about life outside class, so leave majors out.",
     "Proofread. Words like opportunity and sought are misspelled in the draft."], kind="short")
add("rice", "Community option A: residential colleges", "500 words", "Choose this or option B",
    "The residential college system is shaped by the traditions and life experiences each student brings. What life experiences or perspectives are you looking forward to sharing with fellow students there?",
    ["This option fits you best: you already run residence-hall community as a mentor.",
     "Your draft mentions a four-floor hall, an offer connected to Lacoste, and 3D floor plans. Confirm each fact and title.",
     "Tell one story of a resident you helped, then say what you learned about living in community.",
     "Name what you would bring to a college: events, listening or design help.",
     "Check the website address in your draft. It reads as habitot and should be correct or removed."])
add("rice", "Community option B: change agents", "500 words", "Choose this or option A",
    "Rice produces leaders and change agents. What perspectives shaped by your background, experiences, upbringing or cultural identity inspire you to join that community?",
    ["Choose this only if your strongest story is about identity or upbringing more than residence life.",
     "Your grandmother's community work and your veteran service both shape a view of change.",
     "Give one example where you changed something small and real.",
     "Avoid describing yourself as a change agent. Show the change and let the reader conclude.",
     "You answer one option only. Do not split the essay across both."])
add("rice", "The Rice Box", "One image", "Required",
    "Share an image of something that appeals to you. Rice says the image speaks for itself.",
    ["Choose an image you made or took, if you have one you like.",
     "It should be something that appeals to you, not an advertisement for yourself.",
     "A photo from a place that matters, or a piece of your own design work, both fit.",
     "No caption is needed, so pick an image that makes sense alone.",
     "Check the file type and size the portal accepts."], kind="image")

# ------------------------------------------------------------------ Dartmouth
add("dartmouth", "Why transfer, and why Dartmouth", "About 500 words on the official essay page", "Provisional; application opens in January",
    "Explain your reasons for transferring and why Dartmouth. Wording comes from the official page, last updated for an earlier cycle.",
    ["Wait for the January application and capture the real prompts before drafting.",
     "Choose a major first. No major is on file for Dartmouth.",
     "Explain how the quarter-style calendar and small classes suit how you learn.",
     "Use what you learn from the veteran coordinator as knowledge, not as an endorsement.",
     "Plan for testing: request the veteran waiver or schedule a test."],
    prov=OFFICIAL, kind="pending")
add("dartmouth", "Your upbringing and who you are", "About 250 words on the older official page", "Provisional; choose one of two",
    "Describe the environment in which you were raised and how it shaped the person you are.",
    ["Your grandmother's ministry and community are a natural subject.",
     "Show one scene from that environment.",
     "Link it to one present habit or value.",
     "You would answer this or the introduce-yourself prompt, not both.",
     "Confirm the wording when the application opens."],
    prov=OFFICIAL, kind="pending")
add("dartmouth", "Introduce yourself", "About 250 words on the older official page", "Provisional; choose one of two",
    "Introduce yourself in your own way.",
    ["This is open. Lead with what a roommate would learn about you in the first week.",
     "Your quick answers elsewhere show humor and curiosity. Let that voice in.",
     "One or two details are better than a summary of your resume.",
     "Choose this option if your upbringing is already covered in another essay.",
     "Confirm the wording when the application opens."],
    prov=OFFICIAL, kind="pending")

# ------------------------------------------------------------------ Northeastern
add("northeastern", "Transfer personal statement", "Not captured", "No screenshot yet",
    "Northeastern's transfer application includes a personal statement through the Common or Coalition application. Capture the prompt before drafting.",
    ["Take a screenshot of the Northeastern questions so this entry can be replaced.",
     "Your transfer essay for Vanderbilt or UVA can be adapted once you know the limit.",
     "Name the college and degree: Interaction Design, Experience Design or Psychology and Design.",
     "Explain how co-op fits your plan and your timeline to graduate.",
     "Ask for a preliminary credit map first, because it shapes what you can promise."],
    prov=MISSING, kind="pending")
add("northeastern", "Design portfolio statement", "About 500 words on the official page", "Only if you submit a portfolio",
    "Applicants to design programs may submit a portfolio with a short statement about the work.",
    ["A portfolio is optional but recommended for design majors. Decide based on your strongest two or three pieces.",
     "Describe process: the problem, what you tried, what you changed and why.",
     "The floor-plan project and the client learning platform are your clearest cases.",
     "State your individual role on any team project.",
     "Confirm the current portfolio rules for your exact degree."],
    prov=OFFICIAL, kind="portfolio")

# ------------------------------------------------------------------ UChicago
UC = "Extended essay: one to two pages, uploaded with the prompt at the top"
add("uchicago", "Extended essay option 1: how do thoughts eat?", UC, "Choose exactly one of the six options",
    "Food for thought: how do thoughts eat?",
    ["Treat the question literally and build a small theory: what feeds a thought, what starves it.",
     "Your work on how AI systems consume and credit their sources is a natural example.",
     "Add one counterexample that complicates your theory.",
     "Keep your own voice. Wit helps, but an idea you actually believe matters more.",
     "Put the prompt at the top of the page, as the instructions require."], kind="extended")
add("uchicago", "Extended essay option 2: an artistic practice as a solution", UC, "Choose exactly one of the six options",
    "A space telescope used origami-style folding to store its sunshield. Choose an artistic practice and use its principles to propose an elegant solution to a problem.",
    ["This option suits you best: you are a design student who solves problems with making.",
     "Choose a practice you really know, such as storyboarding, sketching or interface layout.",
     "Pick one real problem, state it precisely, then apply two or three principles of the practice.",
     "Your older workbook sketched a storyboarding version. Use it only if storyboarding is truly your practice.",
     "Show where the analogy breaks down. That honesty is what the reader wants."], kind="extended")
add("uchicago", "Extended essay option 3: a mixed metaphor", UC, "Choose exactly one of the six options",
    "Invent your own mixed metaphor and explain how it could make sense, be understood or even be applied.",
    ["Write several candidates and choose the one that says something true by accident.",
     "Explain it in steps: what each half means and what the collision reveals.",
     "Apply it to a real situation from your life or work.",
     "This option rewards play. Pick it only if you enjoy the game.",
     "Keep it to two pages and include the prompt at the top."], kind="extended")
add("uchicago", "Extended essay option 4: a new Olympic event", UC, "Choose exactly one of the six options",
    "Imagine an Olympic event built around an everyday activity. How is it scored, officiated and judged, and why is it a worthy addition?",
    ["Choose an everyday activity you have done at volume, such as canvassing doors or resolving roommate disputes.",
     "Design real scoring rules. The humor comes from taking it seriously.",
     "Use the event to say something about skill that usually goes unseen.",
     "Your interest in unrecognized contribution connects naturally here.",
     "Answer all the parts: scoring, officiating, judging and why it belongs."], kind="extended")
add("uchicago", "Extended essay option 5: a mistaken acronym", UC, "Choose exactly one of the six options",
    "Share a confusing, funny or fascinating example of an acronym mistaken for another meaning, and tell its backstory.",
    ["Use a real mix-up if you have one. Military, college and technology acronyms offer many.",
     "ILR, RA and AI are all acronyms from your own applications.",
     "Tell the story of the confusion, then what it reveals.",
     "Keep it short and specific.",
     "Choose it only if you have a good example, since the prompt depends on it."], kind="extended")
add("uchicago", "Extended essay option 6: a past prompt or your own", UC, "Choose exactly one of the six options",
    "Choose one of UChicago's past prompts or create a question of your own, and answer it with originality.",
    ["If you write your own question, make it one you already argue about, such as who owns intelligence.",
     "Your water-law argument about AI ownership could become a strong answer.",
     "Include the full prompt you chose or wrote at the top of the page.",
     "Take a real position and defend it against the best objection.",
     "Do not reuse another school's essay unchanged. This reader expects something made for them."], kind="extended")
add("uchicago", "Transfer essay", "About 500 words", "Required",
    "Tell us why you plan to leave your current college and how UChicago will satisfy your desire for a particular kind of learning, community and future. Be specific about your own wishes.",
    ["The prompt names three things: learning, community and future. Give each a few sentences.",
     "For learning, be specific about the Core and what you want from it.",
     "Name a real major. Sociology is the candidate on file.",
     "Write it in a separate document and paste it in, as the portal instructs.",
     "Decide about the binding early option separately, after you compare aid."])
add("uchicago", "Personal statement", "1,250 to 3,250 characters", "Optional",
    COMMON_PROMPTS,
    ["UChicago marks this optional. Submit the statement you write for UNC, Rice and WashU if it is strong.",
     "It should cover different ground from the transfer essay.",
     "The portal asks for writing fit for a wide audience, not addressed to one school.",
     "If it repeats the transfer essay, leave it out.",
     "UChicago also accepts self-uploaded transcripts from every college you attended."], kind="optional")

# ------------------------------------------------------------------ reserve bench
BENCH_SUPP = {
    "school": "Columbia General Studies", "title": "Autobiography", "limit": "1,500 to 2,000 words",
    "status": "Reserve school. Submitted through a form that appears after you submit the application.",
    "prompt": ("Write an autobiography covering your educational history, work experience, present situation, plans for the future, "
               "why you consider yourself a nontraditional student, why you chose General Studies, and which parts of the program meet your needs."),
    "guidance": [
        "Columbia requires you to affirm that no generative AI tool wrote or edited this essay. Write and edit it entirely yourself.",
        "Cover all seven listed items. Use them as an outline so none is missed.",
        "The prompt invites turning points, including health, family or justice-system events. Decide what you want on record.",
        "Build an exact timeline of school and work first, then write from it.",
        "The form appears on your status page about 15 minutes after you submit. Do not use the general upload section.",
    ],
}
