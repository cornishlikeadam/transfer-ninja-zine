"""Academic and service record, read line by line from Kendren's transcripts.

Sources (all unofficial copies, private):
- Broward College unofficial transcript, saved 2025-01-14 (coursework through Fall 2024).
- SCAD unofficial transcript, generated 2026-10-03 (Spring and Summer 2026 final, Fall 2026 in progress).
- SCAD student portal screenshots, 2026-11-11: Fall 2026 midterm grades and Winter 2027 registration.
- Joint Services Transcript (JST), unofficial, dated 2025-10-27.

Grades are copied exactly. Midterm grades are not final. Registered courses have no grade.
The page computes every GPA from this list, so fix a course here and every calculator follows.
"""

GP = {"A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7, "C+": 2.3, "C": 2.0, "C-": 1.7, "D+": 1.3, "D": 1.0, "F": 0.0}


def c(inst, term, code, title, credits, unit, grade, status="final", note=""):
    return {"inst": inst, "term": term, "code": code, "title": title, "cr": credits, "unit": unit,
            "grade": grade, "status": status, "note": note}


COURSES = [
    # Broward College, semester hours (SH)
    c("Broward", "Spring 2024", "ENC0017C", "Accelerated Literacy: Reading and Writing", 4, "SH", "A",
      note="Developmental course (0-level number). Counted in Broward's GPA; most four-year schools do not transfer it."),
    c("Broward", "Spring 2024", "MAC1105C", "Corequisite College Algebra", 5, "SH", "W", "withdrawn"),
    c("Broward", "Spring 2024", "SPC1608", "Public Speaking", 3, "SH", "B"),
    c("Broward", "Summer 2024", "COP1000C", "Introduction to Computer Programming", 3, "SH", "W", "withdrawn"),
    c("Broward", "Summer 2024", "REL2300", "World Religions", 3, "SH", "C", note="Writing credit."),
    c("Broward", "Summer 2024", "POS2041", "National Government", 3, "SH", "A", note="Writing credit."),
    c("Broward", "Summer 2024", "PSY2012", "General Psychology", 3, "SH", "B", note="Writing credit."),
    c("Broward", "Summer 2024", "CJL1100", "Criminal Law", 3, "SH", "A"),
    c("Broward", "Fall 2024", "BSC1005", "General Biology for Non-Majors", 3, "SH", "W", "withdrawn"),
    c("Broward", "Fall 2024", "CGS1060C", "Computer Literacy", 3, "SH", "D"),
    c("Broward", "Fall 2024", "GEB2112", "Entrepreneurship", 3, "SH", "W", "withdrawn"),
    c("Broward", "Fall 2024", "MUL2010", "Music Appreciation", 3, "SH", "W", "withdrawn"),
    c("Broward", "Fall 2024", "SLS1001", "Strategies for Success", 3, "SH", "W", "withdrawn"),
    # SCAD, quarter hours (QH)
    c("SCAD", "Spring 2026", "DIGI 130", "Digital Communication", 5, "QH", "B"),
    c("SCAD", "Spring 2026", "FOUN 111", "Sketching and Drawing", 5, "QH", "C", note="Studio course. Liberal-arts colleges may not transfer it."),
    c("SCAD", "Spring 2026", "MATH 140", "The Geometry of Physical Space", 5, "QH", "A"),
    c("SCAD", "Summer 2026", "BUSI 110", "Business I: Fundamentals", 5, "QH", "A"),
    c("SCAD", "Summer 2026", "ENGL 142", "Foundations of Story", 5, "QH", "A"),
    c("SCAD", "Summer 2026", "FOUN 110", "Design: Thinking and Process", 5, "QH", "B", note="Studio course."),
    c("SCAD", "Fall 2026", "AI 101", "Survey of AI Applications", 5, "QH", "A", "midterm", "Midterm grade from the portal, Nov 11. Not final."),
    c("SCAD", "Fall 2026", "DIGI 230", "Ethics of Emerging Technology", 5, "QH", "A", "midterm", "Midterm grade from the portal, Nov 11. Not final."),
    c("SCAD", "Fall 2026", "FOUN 112", "Color in Context", 5, "QH", "A", "midterm", "Midterm grade from the portal, Nov 11. Studio course."),
    c("SCAD", "Winter 2027", "PRO 560", "SCADpro Research: SCAD Entrepreneurial Ecosystem", 5, "QH", "", "registered",
      "Registered. Credit hours not shown in the screenshot; 5 assumed, the SCAD standard. 500-level number: ask SCAD how it posts for an undergraduate."),
    c("SCAD", "Winter 2027", "PRO 580", "SCADpro Collaboration: Deloitte, Control Interface for LA28 Olympics", 5, "QH", "", "registered",
      "Registered. 5 credit hours assumed. A real client brief with Deloitte."),
    c("SCAD", "Winter 2027", "PRO 580", "SCADpro Collaboration: Military World Games", 5, "QH", "", "registered",
      "Registered. 5 credit hours assumed. Directly connects to your service."),
]

ACE = [
    {"what": "Basic Combat Training (ACE AR-2201-0399), 1 Mar to 16 Apr 2021",
     "credit": "6 semester hours recommended, lower division: First Aid and CPR 2, Land Navigation 1, Marksmanship 1, Physical Fitness 1, Self-Defense 1.",
     "note": "Recommendations, not grades. Most selective schools grant none of it, or count it only as physical education elective credit."},
]

SERVICE = {
    "branch": "U.S. Army",
    "rank": "Private 2 (E-2), per the JST",
    "lines": [
        "MOS 12D10, Diver (Engineer branch), listed as primary from 1 Dec 2020.",
        "Reception Battalion record dated 15 Jan 2021 at the U.S. Army Training Center, Fort Leonard Wood, Missouri.",
        "Basic Combat Training completed 1 Mar to 16 Apr 2021.",
        "MOS 68W10, Health Care Specialist (combat medic), listed as primary from 9 Jun 2021.",
    ],
    "flags": [
        "Your resume says Combat Engineer training. The JST shows the Engineer-branch Diver specialty, then a change to Health Care Specialist. Use the wording your DD-214 supports, and keep it identical across every application.",
        "The JST shows status Active as of October 2025. Admissions offices will read your DD-214, not the JST, for separation date and characterization. Have the DD-214 in hand before you describe your service dates.",
        "ROTC eligibility depends on facts that are not on the JST: characterization of service, reentry (RE) code, separation reason and medical history. They are on the DD-214 and in your medical record.",
    ],
    "source": "Joint Services Transcript, unofficial, 2025-10-27.",
}

OTHER = {
    "highSchool": "Byron Nelson High School, graduated June 2019 (from the Broward record).",
    "placement": "Broward placement scores from 26 Nov 2023: English 251, Math 263, Reading 286.",
    "civics": "Florida Civic Literacy competency met.",
    "honors": ["Broward Honor Roll, Summer 2024", "Phi Theta Kappa (resume)", "SCAD Dean's List, Summer 2026"],
    "programs": "Broward lists the Associate in Arts program in Spring and Fall 2024 and the AS in Aviation Maintenance in Summer 2024. SCAD lists the Bachelor of Design with the major as Robotics, Interactive Design and Game Development and the minor as Applied AI, while the term rows show Applied AI and then Robotics. Ask SCAD's registrar which is official before you write it on an application.",
}

# Life timeline, back to high school and forward to graduation. Forward items are projections.
TIMELINE = [
    ["2019-06", "Byron Nelson High School diploma.", "record"],
    ["2020-12", "Army: Diver (12D) specialty assigned.", "record"],
    ["2021-01", "Reception Battalion, Fort Leonard Wood.", "record"],
    ["2021-04", "Basic Combat Training complete.", "record"],
    ["2021-06", "Specialty changes to Health Care Specialist (68W).", "record"],
    ["2022", "Security Officer II, GardaWorld, St. Louis Lambert airport (through 2023).", "resume"],
    ["2023-11", "Broward placement testing.", "record"],
    ["2024-01", "Broward College starts. Spring GPA 3.57.", "record"],
    ["2024-08", "Summer term GPA 3.25, Honor Roll. Cumulative 3.36.", "record"],
    ["2024-12", "Fall term: four withdrawals and a D. Broward closes at 3.04.", "record"],
    ["2025-01", "Nonprofit canvassing for CARE, AARP Foundation and World Vision (through November).", "resume"],
    ["2026-03", "SCAD starts. Spring GPA 3.00. Dining job begins.", "record"],
    ["2026-08", "SCAD Summer GPA 3.66, Dean's List. Cumulative 3.33.", "record"],
    ["2026-09", "SCADhome mentor, student government run, Service to School.", "resume"],
    ["2026-11", "Fall midterms A, A, A. Applications open.", "portal"],
    ["2027-01", "Winter: three SCADpro studios, including Deloitte and the Military World Games.", "registered"],
    ["2027-03", "Most transfer deadlines (Feb 15 to Apr 15).", "projection"],
    ["2027-06", "Spring grades post. Final transcripts go to the school you choose.", "projection"],
    ["2027-08", "Transfer entry, age 26.", "projection"],
    ["2029-05", "Earliest graduation if you enter as a junior, age 28.", "projection"],
    ["2030-05", "Graduation if you enter as a sophomore, age 29.", "projection"],
]

NOTES = [
    "SCAD uses quarter hours. One quarter hour is two thirds of a semester hour, so 30 quarter hours equal 20 semester hours.",
    "Withdrawals carry no grade points in Broward's GPA. Some schools still count them when they judge your record, and Yale's contact named them directly.",
    "Schools recompute GPA their own way. The scenarios here show the most common methods, not any school's official number.",
    "A school that drops developmental courses removes your A in ENC0017C, which lowers the Broward side.",
]


def record():
    return {"courses": COURSES, "gp": GP, "ace": ACE, "service": SERVICE, "other": OTHER,
            "timeline": TIMELINE, "notes": NOTES, "birthYear": 2001, "birthMonth": 3,
            "source": "Broward unofficial transcript 2025-01-14; SCAD unofficial transcript 2026-10-03; SCAD portal 2026-11-11; JST 2025-10-27."}


def gpa(courses, include=lambda x: True):
    pts = hrs = 0.0
    for x in courses:
        if x["grade"] not in GP or not include(x):
            continue
        h = x["cr"] * (2 / 3 if x["unit"] == "QH" else 1)
        pts += GP[x["grade"]] * h
        hrs += h
    return (pts / hrs if hrs else None), hrs


if __name__ == "__main__":
    fin = lambda x: x["status"] == "final"
    print("Broward", gpa(COURSES, lambda x: fin(x) and x["inst"] == "Broward"))
    print("SCAD", gpa(COURSES, lambda x: fin(x) and x["inst"] == "SCAD"))
    print("Pooled", gpa(COURSES, fin))
    print("Pooled, no developmental", gpa(COURSES, lambda x: fin(x) and not x["code"].startswith("ENC0")))
    mid = lambda x: x["status"] in ("final", "midterm")
    print("SCAD with midterms", gpa(COURSES, lambda x: mid(x) and x["inst"] == "SCAD"))
    print("Pooled with midterms", gpa(COURSES, mid))
