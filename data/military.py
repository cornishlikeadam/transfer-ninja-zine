"""Military, ROTC and veteran uniqueness for every school on the main list.

Researched by web search on 2026-11-11 (university ROTC pages, student newspapers, GAO's ROTC
dataset, Posse Foundation pages) plus Kendren's own research notes. ROTC hosting changes, so each
school carries a confidence label. Nothing here is a promise of eligibility: the DD-214 decides that.

Unit status values: "campus" (unit hosted on campus), "cross" (cross-town: you travel to a partner),
"none" (no arrangement found), "unclear" (sources conflict or are old).
"""

# Kendren: born March 2001. Entry Fall 2027 at 26. Commission at graduation: May 2029 (28) or May 2030 (29).
RULES = {
    "summary": ("Army ROTC and Air Force ROTC are realistic on age. Navy and Marine Corps ROTC almost certainly are not. "
                "The real gate for any branch is your DD-214: characterization of service, reentry code and separation reason."),
    "you": [
        "Age: 26 at entry in Fall 2027, 28 at a May 2029 commission (entering as a junior) or 29 at May 2030 (entering as a sophomore).",
        "Prior service: Basic Combat Training is complete (JST), which is what usually earns placement credit for the first two years of Army ROTC. You would likely start in the two-year advanced course as a junior.",
        "Record: JST shows Private 2 with two specialty codes. ROTC staff will ask for the DD-214 and your medical history before they can contract you.",
    ],
    "branches": [
        {"branch": "Army ROTC", "verdict": "Realistic",
         "age": "Scholarship cadets generally must commission before age 31. You would be 28 or 29. Age waivers exist beyond that.",
         "prior": "Veterans usually receive placement credit for the basic course and contract straight into the advanced course.",
         "gate": "University ROTC pages commonly require reentry code RE-1. Forum reports say RE-3 can be waived only at the Cadet Command level and RE-4 is generally disqualifying. Confirm with a battalion recruiter.",
         "extra": "The Simultaneous Membership Program lets a cadet drill in the Army Reserve or Guard while in ROTC, which adds pay and a unit."},
        {"branch": "Air Force ROTC (and Space Force)", "verdict": "Realistic, check the scholarship line",
         "age": "Scholarship cadets must be under 31 on December 31 of the commissioning year. Non-scholarship, non-flying cadets have a higher ceiling (sources say 39). Pilot and other flying slots have lower, non-waivable limits.",
         "prior": "Other-service veterans can apply. The detachment decides how much of the first two years you can skip.",
         "gate": "Same DD-214 questions: characterization, reentry code, separation reason, plus a DoDMERB medical review.",
         "extra": "Yale, Princeton (through Rutgers) and UChicago all point students to Space Force commissions through AFROTC."},
        {"branch": "Navy and Marine Corps ROTC", "verdict": "Likely closed by age",
         "age": "Generally under 27 at commissioning. Prior active duty earns a month-for-month waiver capped at 36 months, and several units cap the waived age near 29 or 30.",
         "prior": "Your active time on the JST is under a year, so the waiver would not cover a 28 or 29 commission.",
         "gate": "Ask only if a unit tells you in writing that a waiver fits your dates.",
         "extra": "Navy units still matter as community: Northwestern, Rice, Penn, Vanderbilt and Yale host one."},
    ],
    "money": [
        "A tuition scholarship from ROTC and the Post-9/11 GI Bill do not simply add together. When one pays tuition, the other usually pays less. Ask the school's VA certifying official to run both before you contract.",
        "Yellow Ribbon requires 100% Post-9/11 eligibility at most schools. Your eligibility tier depends on qualifying active days, which the VA Certificate of Eligibility states. Get the certificate early.",
        "Your notes say VR&E (Chapter 31) pays like the Post-9/11 GI Bill on your calls. VR&E and Yellow Ribbon do not combine the same way, so ask each aid office how they treat Chapter 31.",
        "A contracted cadet owes service after commissioning, typically several years on active duty or longer in the Reserve or Guard. Weigh that against law school timing.",
    ],
    "sources": [
        ["University of Portland Army ROTC, veterans", "https://www.up.edu/armyrotc/veterans/index.html"],
        ["Pacific Lutheran ROTC, prior service", "https://plu.edu/rotc/veterans"],
        ["NETC NROTC requirements", "https://www.netc.navy.mil/Commands/Naval-Service-Training-Command/NROTC/Requirements/Marine"],
        ["Marquette NROTC FAQ", "https://marquette.edu/navy-rotc/frequently-asked-questions.php"],
        ["Ole Miss AFROTC eligibility", "https://olemiss.edu/afrotc/eligibility/"],
        ["Posse Veterans Program", "https://www.possefoundation.org/veterans-program"],
    ],
}


def m(sid, army, navy, af, vets, unique, conf, src):
    return sid, {"army": army, "navy": navy, "af": af, "vets": vets, "unique": unique, "conf": conf, "src": src}


DATA = dict([
    m("brown", ["cross", "Providence College (Patriot Battalion), a short drive. Brown lists the classes as non-credit."],
      ["cross", "College of the Holy Cross, Worcester, about an hour away."],
      ["cross", "Worcester Polytechnic Institute, about an hour away."],
      "Separate Veterans Application with no fee, need-blind admission for veterans, unlimited Yellow Ribbon, and a VetLink partnership.",
      "Brown has the strongest veteran admission pathway on your list, but the weakest ROTC logistics: every unit is off campus and Worcester is a long commute.",
      "medium", "https://www.browndailyherald.com/article/2021/10/rotc-students-reflect-10-years-after-programs-return-to-brown"),
    m("cornell", ["campus", "Army ROTC on campus."], ["campus", "Naval ROTC on campus."], ["campus", "Air Force ROTC on campus."],
      "Yellow Ribbon, a veteran admissions pathway that can waive some documents, and the Veterans Summer Bridge (your research).",
      "One of the few Ivies with all three units on campus, and ILR studies the labor and organizational side of military life.",
      "medium", "https://www.militaryspot.com/news/rotc-making-a-comeback-at-ivy-league-schools"),
    m("nd", ["campus", "Army ROTC on campus."], ["campus", "Naval ROTC on campus."], ["campus", "Air Force ROTC on campus."],
      "Yellow Ribbon (about $30,000 a year with a 100% GI Bill, from your call), VetLink and Warrior-Scholar Project ties.",
      "The most ROTC-dense campus on your list, with a Catholic service culture. Your faith and service story fit here without translation.",
      "medium", "https://www.collegevine.com/faq/23370/universities-with-rotc-programs"),
    m("yale", ["unclear", "Yale cadets have commissioned into the Army recently, but the host battalion was not confirmed in this search."],
      ["campus", "Naval ROTC on campus since 2012."],
      ["campus", "Air Force ROTC Detachment 009 on campus, with a Space Force path."],
      "Eli Whitney program for nontraditional students. Your notes: about 60 Yale College veterans and more than 100 undergraduates in ROTC as of late 2025.",
      "The Warrior-Scholar Project began at Yale, and you are already a Warrior-Scholar. Eli Whitney plus AFROTC on campus is a rare pairing for an adult veteran.",
      "medium", "https://yalecollege.yale.edu/academics/special-academic-programs/reserve-officers-training-corps-rotc"),
    m("princeton", ["campus", "Army Tiger Battalion, on campus since 1919, the longest continuously running ROTC program in the country."],
      ["cross", "Naval ROTC through Rutgers, re-established for Princeton in 2014."],
      ["cross", "Air Force ROTC through Rutgers, including a Space Force option."],
      "Princeton's transfer program recruits veterans. Your notes: 66 students in ROTC in 2024-25 and the first two Space Force commissions in the Class of 2026.",
      "Army ROTC on campus at a school whose transfer program exists partly for veterans. ROTC here is a community, not a commute.",
      "high", "https://admission.princeton.edu/community/rotc"),
    m("tufts", ["cross", "MIT (Paul Revere Battalion)."], ["cross", "MIT."], ["cross", "MIT."],
      "REAL program for adult and veteran students, Yellow Ribbon $5,000 a year matched by the VA, and a Tufts ROTC Support Program.",
      "All three units are a subway ride away at MIT, but older reporting says Tufts gives no academic credit for ROTC classes.",
      "medium", "https://students.tufts.edu/specialized-academic-programs/tufts-rotc-support-program"),
    m("washu", ["campus", "Gateway Battalion, hosted by WashU. It won the first DoD ROTC partnership excellence award in 2021."],
      ["none", "No Navy unit found in St. Louis."],
      ["cross", "Detachment 207 at Saint Louis University, nearby."],
      "WashU's veterans site lists a Posse Veterans Program page: confirm whether WashU is a current partner.",
      "Gateway Battalion cadets train at Fort Leonard Wood, where you did basic training. St. Louis is also your family's ground.",
      "medium", "https://rotc.wustl.edu/about"),
    m("nu", ["cross", "Loyola University Chicago battalion."],
      ["campus", "Naval ROTC on campus (Northwestern's own unit)."],
      ["cross", "University of Chicago, Detachment 195."],
      "Veteran and ROTC admissions page and Yellow Ribbon (amount not confirmed in this search). GAO data show about 6 ROTC students a year.",
      "The on-campus unit is Navy, which your age likely rules out. Army and Air Force mean commuting into Chicago.",
      "high", "https://catalogs.northwestern.edu/undergraduate/special-programs-courses/military-programs/"),
    m("gt", ["campus", "Hoya Battalion, on campus since 1918. Cadet Command ranked it first of 272 in 2012."],
      ["cross", "George Washington University."],
      ["unclear", "Cross-town; the host detachment was not confirmed in this search."],
      "Yellow Ribbon with a full match in the College per your dossier, and a military and veteran resource office.",
      "A top Army battalion plus the School of Foreign Service in Washington: the closest link on your list between ROTC and policy careers.",
      "medium", "https://rotc.georgetown.edu/"),
    m("vandy", ["campus", "Army ROTC hosted at Vanderbilt."],
      ["campus", "Naval ROTC hosted at Vanderbilt, across from the Peabody campus."],
      ["cross", "Detachment 790 at Tennessee State, about 10 minutes away."],
      "The VA certifying official works through the registrar. Yellow Ribbon amounts vary by school, so get a written estimate.",
      "The Navy unit sits across the street from Peabody, where Human and Organizational Development lives, and commissions are joint with nearby schools.",
      "medium", "https://news.vanderbilt.edu/2024/06/04/vanderbilts-joint-commissioning-ceremony-celebrates-class-of-2024-with-fanfare-and-inspiration/"),
    m("williams", ["unclear", "No confirmed arrangement. Siena College hosts Army ROTC in the region but no Williams link was found."],
      ["none", "No Navy arrangement found."],
      ["cross", "GAO lists an Air Force cross-town unit; the host was not named."],
      "Williams encourages veterans to apply and has a page in the Service to School VetLink guidebook.",
      "A small residential college where ROTC would be mostly self-directed. Choose Williams for the classroom, not the corps.",
      "low", "https://files.gao.gov/interactive/data/105857/Williams_College.html"),
    m("wesleyan", ["cross", "University of Connecticut (older accounts)."],
      ["none", "No Navy arrangement found."],
      ["cross", "Yale's Detachment 009 in New Haven, with no extra tuition."],
      "Wesleyan was the second Posse Veterans Program partner (2014). Confirm it still enrolls a veterans posse.",
      "A history of bringing veterans in as a cohort, which matters more here than ROTC, since GAO counts almost no Wesleyan cadets.",
      "medium", "https://www.wesleyan.edu/registrar/ROTC/Index.html"),
    m("amherst", ["cross", "UMass Amherst, through the Five College area."],
      ["none", "No Navy arrangement found."],
      ["cross", "UMass Amherst, Detachment 370."],
      "Your dossier lists Posse Veterans and VetLink, unverified. GAO counts about half a cadet a year from Amherst.",
      "UMass is next door and hosts both Army and Air Force, so ROTC is practical even at a tiny college.",
      "medium", "https://files.gao.gov/interactive/data/105857/Amherst_College.html"),
    m("usc", ["campus", "Army ROTC on campus."], ["campus", "Naval ROTC on campus."], ["campus", "Air Force ROTC on campus."],
      "Unlimited undergraduate Yellow Ribbon, a Veterans Resource Center, and a certification office that handles Chapter 33, VR&E and Yellow Ribbon.",
      "One of about 60 universities hosting all three units. Iovine and Young plus on-campus ROTC is a rare mix of studio work and service.",
      "high", "https://military.usc.edu/students/rotc/"),
    m("smu", ["cross", "University of Texas at Arlington, or its extension at UNT."],
      ["none", "No Navy arrangement found."],
      ["cross", "University of North Texas, Denton, about 45 minutes away."],
      "Yellow Ribbon guarantees 100% tuition for eligible Post-9/11 veterans. SMU gives housing and dining to full-tuition ROTC scholarship holders.",
      "Your SMU fintech certificate gives you a history here, and the ROTC housing award could matter for the full-scholarship gate.",
      "high", "https://www.smu.edu/news/archives/2021/featured-news/smu-offers-full-room-and-board-scholarships-to-rotc-students"),
    m("unc", ["campus", "Army ROTC on campus."], ["campus", "Naval ROTC on campus."], ["campus", "Air Force ROTC on campus."],
      "In-state tuition by law for veterans using Post-9/11 or Chapter 30, plus Yellow Ribbon.",
      "Close to Fort Bragg and a large military community, with all three units and in-state pricing for you as a veteran.",
      "low", "https://admissions.unc.edu/apply/military-and-veterans/"),
    m("uva", ["campus", "Army ROTC on campus."], ["campus", "Naval ROTC on campus."], ["campus", "Air Force ROTC on campus."],
      "UVA appears on the current Posse Veterans partner list. Yellow Ribbon is first come, first served.",
      "The only school on your list with a current Posse Veterans listing, which brings a funded veteran cohort.",
      "medium", "https://www.possefoundation.org/veterans-program"),
    m("rice", ["cross", "University of Houston. Rice gives credit for the classes."],
      ["campus", "Naval ROTC hosted at Rice."],
      ["cross", "University of Houston."],
      "Rice Military Veterans association, VetLink and Yellow Ribbon per your dossier.",
      "Rice gives academic credit for military science taken at Houston, and aid can follow the ROTC courses.",
      "medium", "https://ga.rice.edu/programs-study/departments-programs/interdisciplinary/military-science/"),
    m("dartmouth", ["campus", "Delta Company, part of the Wildcat Battalion at UNH, staffed on campus."],
      ["none", "Not available. Navy and Marine Corps are not expanding to Dartmouth."],
      ["none", "Not available."],
      "Unlimited Yellow Ribbon, a veteran coordinator, VetLink, and Posse Veterans partner since 2016 (confirm current status).",
      "President Beilock announced an ROTC and veteran-support expansion on Veterans Day 2025, so you would arrive during a build-out.",
      "high", "https://student-affairs.dartmouth.edu/departments-programs/programs/rotc-dartmouth"),
    m("northeastern", ["campus", "Liberty Battalion, hosted at Northeastern."],
      ["cross", "Cross-town in Boston."],
      ["cross", "Boston University, Detachment 355."],
      "CAVS veteran center and automatic unlimited Yellow Ribbon for 100% Post-9/11 undergraduates (your research).",
      "Co-op plus an on-campus Army battalion: you could hold a paid co-op and stay in ROTC in the same city.",
      "medium", "https://rotc.northeastern.edu/prospective-and-current-college-students/"),
    m("uchicago", ["unclear", "UChicago has Army cadets; the host battalion was not confirmed in this search."],
      ["unclear", "Not confirmed."],
      ["campus", "Detachment 195, hosted at UChicago since its recent activation, with a Space Force path."],
      "Unlimited Yellow Ribbon and a fifth-partner listing with the Posse Veterans Program (confirm current status).",
      "A new Air Force detachment on campus means a small, young unit where a prior-service cadet would stand out.",
      "medium", "https://college.uchicago.edu/student-life/rotc-programs-offer-college-students-pathways-and-training-future-military-leadership"),
    m("penn", ["cross", "Drexel, which absorbed Penn's Army program in the 1990s."],
      ["campus", "Naval ROTC hosted at Penn with Temple and Drexel."],
      ["cross", "Cross-town; the host detachment was not confirmed in this search."],
      "Unlimited undergraduate Yellow Ribbon, and Penn pays tuition left after the GI Bill for 100% eligible veterans. A March 2026 report counted only five veterans in the traditional undergraduate college, alongside a new push to admit more.",
      "Penn is actively trying to grow its veteran undergraduate count, so a strong veteran file arrives at a useful moment.",
      "medium", "https://penntoday.upenn.edu/news/penn-expands-yellow-ribbon-program-veterans"),
])

SCORE = {"campus": 3, "cross": 2, "unclear": 1, "none": 0}


def projection(sid):
    d = DATA[sid]
    a, af, n = d["army"][0], d["af"][0], d["navy"][0]
    parts = []
    if a == "campus":
        parts.append("Best path: Army ROTC on campus, entering the advanced course as a prior-service junior.")
    elif af == "campus":
        parts.append("Best path: Air Force ROTC on campus, if the detachment accepts your prior service.")
    elif a == "cross":
        parts.append("Best path: Army ROTC cross-town, so plan the weekly travel before you contract.")
    elif af == "cross":
        parts.append("Best path: Air Force ROTC cross-town.")
    else:
        parts.append("No confirmed Army or Air Force path. Treat ROTC as unlikely here and lean on veteran programs.")
    if n == "campus":
        parts.append("The Navy unit here is community, not a commissioning route at your age.")
    parts.append("Commission at 28 (junior entry) or 29 (sophomore entry), subject to your DD-214.")
    return " ".join(parts)


def military():
    schools = {}
    for sid, d in DATA.items():
        x = dict(d)
        x["projection"] = projection(sid)
        x["access"] = SCORE[d["army"][0]] + SCORE[d["af"][0]]
        schools[sid] = x
    return {"rules": RULES, "schools": schools, "updated": "2026-11-11"}
