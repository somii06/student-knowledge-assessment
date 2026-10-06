"""
app.py
------
Student Knowledge Assessment and Career Skill Gap Recommendation System

Flow:
    Student Profile -> Career Selection -> Assessment -> Results -> Recommendations

Everything is rule based (simple Python calculations).
No AI and no Machine Learning is used anywhere.
"""

import streamlit as st

from data import careers, importance_labels, questions, recommendations

st.set_page_config(page_title="Student Skill Gap System", page_icon="🎓", layout="wide")

LEVEL_ICONS = {"Strong": "🟢", "Intermediate": "🟡", "Beginner": "🔴"}
PRIORITY_ICONS = {"Very High": "🔴", "High": "🟠", "Medium": "🟡", "Low": "🟢"}


# ======================================================================
# Helper functions (plain Python - easy to explain in the viva)
# ======================================================================
def knowledge_level(score):
    """Convert a knowledge score (0-100) into a level."""
    if score < 40:
        return "Beginner"
    if score < 70:
        return "Intermediate"
    return "Strong"


def calculate_gap(required, knowledge):
    """Skill gap = required - knowledge. Never negative."""
    gap = required - knowledge
    if gap < 0:
        gap = 0
    return gap


def calculate_readiness(rows):
    """
    Career Readiness = average of (knowledge / required x 100),
    every topic is capped at 100. Result is 0 - 100.
    """
    percentages = []
    for row in rows:
        value = row["Knowledge"] / row["Required"] * 100
        if value > 100:
            value = 100
        percentages.append(value)
    return round(sum(percentages) / len(percentages))


def grade_assessment(career, career_questions):
    """Check the answers and build one result row per topic."""
    # 1. count correct answers for every topic
    correct = {topic: 0 for topic in careers[career]}
    total = {topic: 0 for topic in careers[career]}
    review = []
    for index, question in enumerate(career_questions):
        given = st.session_state.get(f"answer_{index}")
        is_correct = given == question["answer"]
        topic = question["topic"]
        total[topic] += 1
        if is_correct:
            correct[topic] += 1
        review.append({
            "topic": topic,
            "question": question["question"],
            "given": given,
            "correct_answer": question["answer"],
            "is_correct": is_correct,
        })

    # 2. knowledge, gap and priority for every topic
    rows = []
    for topic, requirement in careers[career].items():
        knowledge = round(correct[topic] / total[topic] * 100)
        gap = calculate_gap(requirement["required"], knowledge)
        rows.append({
            "Topic": topic,
            "Required": requirement["required"],
            "Knowledge": knowledge,
            "Level": f"{LEVEL_ICONS[knowledge_level(knowledge)]} {knowledge_level(knowledge)}",
            "Gap": gap,
            "Importance": importance_labels[requirement["importance"]],
            "Priority": gap * requirement["importance"],
        })
    rows.sort(key=lambda row: row["Priority"], reverse=True)

    return {
        "career": career,
        "rows": rows,
        "readiness": calculate_readiness(rows),
        "review": review,
    }


# ======================================================================
# PAGE 1 - STUDENT PROFILE
# ======================================================================
def profile_page():
    st.header("👤 Student Profile")
    st.caption("Fill your basic details. No login or password is required.")

    student = st.session_state.get("student")
    with st.form("profile_form"):
        name = st.text_input("Student Name",
                             value=student["name"] if student else "")
        branch = st.selectbox(
            "Branch",
            ["Information Technology", "Computer Science", "Electronics & Communication",
             "Mechanical", "Civil", "Electrical"],
            index=["Information Technology", "Computer Science",
                   "Electronics & Communication", "Mechanical", "Civil",
                   "Electrical"].index(student["branch"]) if student else 0,
        )
        semester = st.number_input("Semester", min_value=1, max_value=8,
                                   value=student["semester"] if student else 6)
        cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0,
                               value=student["cgpa"] if student else 7.5, step=0.1)
        saved = st.form_submit_button("💾 Save Profile")

    if saved:
        if not name.strip():
            st.error("Please enter your name.")
        else:
            st.session_state["student"] = {
                "name": name.strip(), "branch": branch,
                "semester": int(semester), "cgpa": float(cgpa),
            }
            st.success(f"Profile saved for {name.strip()}.")

    if st.session_state.get("student"):
        student = st.session_state["student"]
        st.subheader("Saved Profile")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Name", student["name"])
        col2.metric("Branch", student["branch"])
        col3.metric("Semester", student["semester"])
        col4.metric("CGPA", f"{student['cgpa']:.1f}")


# ======================================================================
# PAGE 2 - CAREER SELECTION
# ======================================================================
def career_page():
    st.header("🧭 Career Selection")
    career = st.selectbox("Select Career", list(careers.keys()))

    if st.button("✅ Select this career"):
        st.session_state["career"] = career
        st.session_state["results"] = None       # old results belong to the old career
        for key in list(st.session_state.keys()):  # clear old answers
            if str(key).startswith("answer_"):
                del st.session_state[key]
        st.success(f"Career selected: {career}")

    selected = st.session_state.get("career")
    if selected:
        st.info(f"The following topics are important for **{selected}**.")
        rows = [
            {"Topic": topic,
             "Required Level": data["required"],
             "Importance": f"{PRIORITY_ICONS[importance_labels[data['importance']]]} "
                           f"{importance_labels[data['importance']]} ({data['importance']})"}
            for topic, data in careers[selected].items()
        ]
        st.dataframe(rows, hide_index=True)
        st.caption("Required Level = knowledge (%) you should have  •  "
                   "Importance = 1 Low, 2 Medium, 3 High, 4 Very High")


# ======================================================================
# PAGE 3 - ASSESSMENT
# ======================================================================
def assessment_page():
    st.header("📝 Assessment")
    career = st.session_state.get("career")
    if not career:
        st.warning("Please select a career first on the **Career Selection** page.")
        return

    topics = list(careers[career].keys())
    career_questions = [q for q in questions if q["topic"] in topics]
    st.info(f"Career: **{career}**  •  {len(career_questions)} questions "
            f"from {len(topics)} topics. The correct answers are shown "
            "only after you submit.")

    with st.form("assessment_form"):
        for index, question in enumerate(career_questions):
            st.markdown(f"**{index + 1}. [{question['topic']}] {question['question']}**")
            st.radio("Your answer", question["options"],
                     key=f"answer_{index}", index=None, horizontal=True,
                     label_visibility="collapsed")
        submitted = st.form_submit_button("✅ Submit Assessment")

    if submitted:
        unanswered = [i for i in range(len(career_questions))
                      if st.session_state.get(f"answer_{i}") is None]
        if unanswered:
            st.warning(f"Please answer all questions. {len(unanswered)} left.")
            return
        st.session_state["results"] = grade_assessment(career, career_questions)
        st.success("Assessment submitted! Open the **Results** page to see your report.")


# ======================================================================
# PAGE 4 - RESULTS
# ======================================================================
def results_page():
    st.header("📊 Results")
    results = st.session_state.get("results")
    if not results:
        st.info("No results yet. Complete the **Assessment** page first.")
        return

    rows = results["rows"]
    student = st.session_state.get("student")
    if student:
        st.caption(f"{student['name']}  •  {student['branch']}  •  "
                   f"Semester {student['semester']}  •  CGPA {student['cgpa']:.1f}  •  "
                   f"Career: **{results['career']}**")

    # ---- metric cards ------------------------------------------------------
    strongest = max(rows, key=lambda row: row["Knowledge"])
    top = rows[0]
    col1, col2, col3 = st.columns(3)
    col1.metric("Career Readiness", f"{results['readiness']}%")
    col2.metric("Strongest Topic", strongest["Topic"],
                f"{strongest['Knowledge']}% knowledge")
    col3.metric("Highest Priority", top["Topic"] if top["Gap"] > 0 else "None",
                f"Priority {top['Priority']}" if top["Gap"] > 0 else "All topics clear")
    st.progress(results["readiness"] / 100)

    # ---- topic-wise report -------------------------------------------------
    st.subheader("Topic-wise Report")
    st.dataframe(rows, hide_index=True)

    # ---- answer review (correct answers only after submission) -------------
    with st.expander("📋 Answer review (correct answers)"):
        for item in results["review"]:
            icon = "✅" if item["is_correct"] else "❌"
            st.markdown(f"{icon} **[{item['topic']}]** {item['question']}")
            st.markdown(f"    - Your answer: **{item['given']}**")
            if not item["is_correct"]:
                st.markdown(f"    - Correct answer: **{item['correct_answer']}**")

    # ---- final summary -----------------------------------------------------
    st.subheader("Final Summary")
    strong = [row["Topic"] for row in rows if row["Level"].endswith("Strong")]
    weak = [row["Topic"] for row in rows if row["Gap"] > 0]
    st.markdown(f"""
| | |
|---|---|
| **Your Selected Career** | {results['career']} |
| **Career Readiness** | {results['readiness']}% |
| **Strong Topics** | {", ".join(strong) if strong else "None yet"} |
| **Topics Needing Improvement** | {", ".join(weak) if weak else "None - all required levels met"} |
| **First Topic to Study** | {rows[0]['Topic'] if rows[0]['Gap'] > 0 else "Nothing pending"} |
""")


# ======================================================================
# PAGE 5 - RECOMMENDATIONS
# ======================================================================
def recommendations_page():
    st.header("💡 Study Recommendations")
    results = st.session_state.get("results")
    if not results:
        st.info("Complete the **Assessment** page first, then recommendations "
                "will appear here.")
        return

    weak_rows = [row for row in results["rows"] if row["Gap"] > 0]
    if not weak_rows:
        st.success("🎉 You already meet the required level for every topic of "
                   f"**{results['career']}**. Great job!")
        return

    st.caption("Rule used: Priority = Skill Gap × Importance. "
               "Topics are shown from highest priority to lowest.")

    for row in weak_rows:
        topic = row["Topic"]
        icon = PRIORITY_ICONS[row["Importance"]]
        with st.expander(
            f"{icon} {topic} — Priority {row['Priority']} "
            f"({row['Importance']} importance)"
        ):
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Your Knowledge", f"{row['Knowledge']}%")
            col2.metric("Required", f"{row['Required']}%")
            col3.metric("Skill Gap", row["Gap"])
            col4.metric("Importance", row["Importance"])

            st.markdown("**Recommended topics to study:**")
            for item in recommendations.get(topic, []):
                st.markdown(f"- {item}")

            st.info(
                f"**{topic}** is recommended because your knowledge level "
                f"({row['Knowledge']}%) is below the required career level "
                f"({row['Required']}%) and the topic has "
                f"{row['Importance'].lower()} importance."
            )


# ======================================================================
# SIDEBAR + MAIN
# ======================================================================
PAGES = {
    "Student Profile": profile_page,
    "Career Selection": career_page,
    "Assessment": assessment_page,
    "Results": results_page,
    "Recommendations": recommendations_page,
}


def main():
    st.sidebar.title("🎓 Student Assessment System")
    page = st.sidebar.radio("Go to", list(PAGES.keys()))
    st.sidebar.divider()

    student = st.session_state.get("student")
    if student:
        st.sidebar.caption(f"👤 {student['name']}")
    career = st.session_state.get("career")
    if career:
        st.sidebar.caption(f"🧭 {career}")

    st.title("Student Knowledge Assessment and Career Skill Gap Recommendation System")
    st.caption("Find out how ready you are for your career and which topics "
               "to study first.")

    try:
        PAGES[page]()
    except Exception as error:                     # the app must never crash
        st.error("Something went wrong on this page.")
        st.code(str(error))


main()
