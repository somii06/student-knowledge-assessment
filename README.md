# 📚 Student Knowledge Assessment and Career Skill Gap Recommendation System

A simple, rule-based Streamlit application that measures a student's knowledge
topic by topic, compares it with the requirements of a chosen career, calculates
the **skill gap** and **priority**, and recommends what to study first.

> **Note:** This is **not** an AI or Machine Learning project. Every result is
> produced by simple, transparent Python formulas that are explained in this
> README.

---

## 1. Project Title

**Student Knowledge Assessment and Career Skill Gap Recommendation System**

---

## 2. Project Overview

In very simple words:

1. The student enters their profile (name, branch, semester, CGPA).
2. The student selects one career (Data Analyst / Software Developer / Web Developer).
3. The system shows the topics that are important for that career and how much
   knowledge is required in each topic.
4. The student answers 15 multiple-choice questions.
5. The system calculates the **knowledge score** (in %) for every topic.
6. It compares the knowledge with the career requirement → **skill gap**.
7. It multiplies the gap with the topic's **importance** → **priority score**.
8. It shows a results dashboard, a final report and **study recommendations**
   (which topic to study first, and which concepts to study inside that topic).

Everything is done with basic Python: lists, dictionaries, loops, conditions
and simple arithmetic. No AI, no machine learning, no external API.

---

## 3. Problem Statement

Most college students do not know **which topics** they need to improve for
their dream job. They may study randomly, or focus on topics that are not
important for the career they want.

This project solves that problem by:

- giving a **clear percentage** of the student's knowledge in each topic,
- comparing it with a **fixed career requirement**,
- showing the **gap** and a **priority score**, and
- recommending **what to study first** and **what concepts to study**.

---

## 4. Objectives

1. To build a simple assessment system that measures topic-wise knowledge from
   multiple-choice questions.
2. To store the requirements (required level + importance) of 3 careers.
3. To calculate the **skill gap** between required level and student knowledge.
4. To calculate a **priority score** for every topic using
   `gap × importance`.
5. To generate **study recommendations** with a clear reason for each topic.
6. To show everything in a clean **Streamlit** interface with a final report.

---

## 5. Features

| # | Feature | Where it appears |
|---|---------|------------------|
| 1 | Student profile: name, branch, semester, CGPA (with validation) | Student Profile |
| 2 | Selection of exactly 3 careers | Career Selection |
| 3 | Career requirements table (required level + importance) | Career Selection |
| 4 | 15 MCQ assessment (5 topics × 3 questions) per career | Assessment |
| 5 | Answers must all be given before submission (validation) | Assessment |
| 6 | Knowledge score per topic (correct / total × 100) | Results |
| 7 | Knowledge level: Beginner / Intermediate / Strong with 🟢🟡🔴 icons | Results |
| 8 | Skill gap, importance and priority in one report table | Results |
| 9 | Career readiness percentage with a progress bar | Results |
| 10 | Answer review — correct answers shown only after submission | Results |
| 11 | Final summary (career, readiness, strong topics, first topic to study) | Results |
| 12 | Study recommendations with reason + concepts for every weak topic | Recommendations |
| 13 | Changing the career clears the old assessment results | Career Selection |

---

## 6. Technology Used

### Python
The entire logic (grading, gap, priority, readiness) is plain Python 3.

### Streamlit
Streamlit turns Python code into a web interface. We use only its simple
components: `st.title()`, `st.header()`, `st.text_input()`, `st.selectbox()`,
`st.number_input()`, `st.radio()`, `st.button()`, `st.form`, `st.metric()`,
`st.dataframe()`, `st.progress()`, `st.success()`, `st.warning()`,
`st.info()`, `st.expander()`, `st.columns()` and `st.sidebar`.

### Python concepts used (easy to explain in the viva)

| Concept | Where it is used |
|---|---|
| **Variables** | `gap`, `knowledge`, `readiness`, `career` store values |
| **Lists** | the question bank, the options of a question, the result rows |
| **Dictionaries** | `careers`, `recommendations`, each question, each result row |
| **Functions** | `knowledge_level()`, `calculate_gap()`, `calculate_readiness()`, `grade_assessment()` |
| **Loops** | iterating over questions while grading, over topics while building the table |
| **Conditions** | `if gap < 0 → 0`, level checks `if score < 40`, unanswered-question check |

No other library is used. `requirements.txt` contains only `streamlit`.

---

## 7. Project Architecture

```text
Student
   ↓
Career  (3 careers in a dictionary)
   ↓
Questions  (15 MCQs for the chosen career's topics)
   ↓
Knowledge Assessment  (correct / total × 100 per topic)
   ↓
Compare with Career Requirement
   ↓
Skill Gap  (required - knowledge, minimum 0)
   ↓
Priority  (gap × importance)
   ↓
Recommendation  (highest priority first + topics to study)
   ↓
Final Report  (metrics, table, summary)
```

In the app, this maps to 5 pages in the sidebar:
**Student Profile → Career Selection → Assessment → Results → Recommendations**.

---

## 8. File Structure

```text
student_skill_gap_project/
│
├── app.py            # Streamlit UI + all calculations (grading, gap, priority, readiness)
├── data.py           # careers, importance, question bank, correct answers, recommendations
├── requirements.txt  # only: streamlit
└── README.md         # this documentation
```

- **app.py** — contains the 5 pages and the 4 calculation functions.
- **data.py** — contains no logic, only data (dictionaries and lists), so the
  question bank and career requirements can be changed without touching the UI.
- **requirements.txt** — one line: `streamlit`.
- **README.md** — documentation, formulas and viva preparation.

---

## 9. Data Structures

### 1) Careers (`careers` in `data.py`)

A dictionary. The key is the career name, the value is another dictionary of
topics:

```python
careers = {
    "Data Analyst": {
        "Python":     {"required": 70, "importance": 3},
        "SQL":        {"required": 75, "importance": 4},
        "Statistics": {"required": 70, "importance": 4},
        "Excel":      {"required": 65, "importance": 2},
        "Power BI":   {"required": 60, "importance": 3},
    },
    ...
}
```

- **required** → the knowledge level (in %) the student should have.
- **importance** → `1 = Low, 2 = Medium, 3 = High, 4 = Very High`
  (converted to words by the `importance_labels` dictionary).

### 2) Question bank (`questions` in `data.py`)

A list of dictionaries. Each question has 5 fields:

```python
{
    "question": "Which keyword is used to define a function in Python?",
    "options":  ["function", "def", "define", "func"],
    "answer":   "def",
    "topic":    "Python"
}
```

There are **33 questions** in total: 11 topics × 3 questions.
Each career uses 5 topics → **15 questions per career**.

### 3) Recommendations (`recommendations` in `data.py`)

A dictionary that maps every topic to the concepts to study:

```python
recommendations = {
    "SQL": ["JOIN", "GROUP BY", "Subqueries", "Indexes"],
    ...
}
```

### 4) Result rows (built inside `app.py`)

While grading, one dictionary per topic is created:

```python
{"Topic": "SQL", "Required": 75, "Knowledge": 60, "Level": "🟡 Intermediate",
 "Gap": 15, "Importance": "Very High", "Priority": 60}
```

The list of these dictionaries is sorted by `Priority` (highest first) and is
displayed with `st.dataframe()`.

---

## 10. Algorithms (all formulas with examples)

### 10.1 Knowledge Score

```text
Knowledge Score = (Correct Answers / Total Questions) × 100
```

**Example:** 2 correct out of 3 → `(2 / 3) × 100 = 66.67` → rounded → **67%**
(rounding with `round()` gives a whole number).

### 10.2 Knowledge Level

```text
0 – 39   → 🔴 Beginner
40 – 69  → 🟡 Intermediate
70 – 100 → 🟢 Strong
```

**Example:** 67% → **Intermediate**. 39% → Beginner. 70% → Strong.

### 10.3 Skill Gap

```text
Skill Gap = Required Level - Knowledge Score
(If negative, it is set to 0.)
```

**Example 1:** SQL required 75, knowledge 60 → `75 - 60 = 15`
**Example 2:** Python required 70, knowledge 80 → `70 - 80 = -10` → set to **0**
(the student already knows more than required).

### 10.4 Topic Importance

```text
1 = Low   2 = Medium   3 = High   4 = Very High
```

Importance is a fixed number inside the career dictionary. It is shown in the
career table and in every recommendation.

### 10.5 Priority Score

```text
Priority Score = Skill Gap × Importance
```

**Example:** Statistics gap = 30, importance = 4 (Very High)
→ `30 × 4 = 120`.

All topics are then sorted from the highest priority to the lowest, so the
first row of the table is the topic to study first.

### 10.6 Career Readiness

```text
For every topic:  value = Knowledge / Required × 100   (capped at 100)
Career Readiness  = average of those values  (rounded, between 0 and 100)
```

**Example:**

| Topic | Knowledge | Required | Knowledge/Required × 100 |
|---|---|---|---|
| Python | 80 | 70 | 114.3 → capped to **100** |
| SQL | 60 | 75 | **80** |
| Statistics | 40 | 70 | **57.14** |
| Excel | 65 | 65 | **100** |
| Power BI | 30 | 60 | **50** |

Average = `(100 + 80 + 57.14 + 100 + 50) / 5 = 77.43` → **77%**

---

## 11. Code Explanation (important functions in `app.py`)

### Function: `knowledge_level(score)`

```text
Purpose:  Convert a knowledge score (0-100) into a readable level.
Input:    score (integer or float, 0-100)
Process:  if score < 40  → "Beginner"
          elif score < 70 → "Intermediate"
          else            → "Strong"
Output:   one of the three level names (string)
```

### Function: `calculate_gap(required, knowledge)`

```text
Purpose:  Calculate how far the student is from the career requirement.
Input:    required (career required level)
          knowledge (student's knowledge score)
Process:  gap = required - knowledge
          if gap < 0 → gap = 0
Output:   skill gap (whole number, never negative)
```

### Function: `calculate_readiness(rows)`

```text
Purpose:  Calculate the overall career readiness percentage.
Input:    rows — list of result dictionaries (each has Required and Knowledge)
Process:  for every row: value = Knowledge / Required × 100 (maximum 100)
          readiness = average of all values, rounded
Output:   readiness percentage between 0 and 100
```

### Function: `grade_assessment(career, career_questions)`

```text
Purpose:  Check all answers and build the complete result.
Input:    career name (string)
          career_questions (list of the 15 questions of that career)
Process:  1. compare every answer with the correct answer (stored in session)
          2. count correct/total for each topic
          3. knowledge = round(correct / total × 100)
          4. gap = required - knowledge (minimum 0)
          5. priority = gap × importance
          6. sort all rows by priority (highest first)
          7. readiness = average of Knowledge/Required × 100
Output:   dictionary: career, rows (table), readiness, review (answer check)
```

### Pages: `profile_page()`, `career_page()`, `assessment_page()`,
`results_page()`, `recommendations_page()`

```text
Purpose:  Each function draws one sidebar page with Streamlit.
Input:    values read from st.session_state (student, career, results)
Process:  render widgets → save input → call the calculation functions
Output:   nothing (they draw the page directly)
```

---

## 12. Running the Project

**Step 1 — requirements** (only Streamlit):

```bash
pip install -r requirements.txt
```

**Step 2 — start the app:**

```bash
streamlit run app.py
```

The browser opens automatically at `http://localhost:8501`.

**Step 3 — use it:**

1. Open **Student Profile** → fill your details → **💾 Save Profile**
2. Open **Career Selection** → choose a career → **✅ Select this career**
3. Open **Assessment** → answer all 15 questions → **✅ Submit Assessment**
4. Open **Results** → see your readiness, report table and summary
5. Open **Recommendations** → see which topic to study first

Python 3.9 or newer is required. No database, no internet, no API keys.

---

## 13. Testing

All five required tests were executed (automated script + manual UI walk-through).

### Test 1 — Student answers most questions correctly
**Action:** answer nearly all questions correctly for Data Analyst.
**Expected:** high knowledge, small gaps, high readiness.
**Result:** ✅ PASS — with knowledge ≥ 75% in every topic, all gaps ≤ 15 and
readiness = 100%.

### Test 2 — Student answers many incorrectly
**Action:** answer most questions wrongly.
**Expected:** low knowledge and high-priority recommendations.
**Result:** ✅ PASS — every topic has a gap, top priority = SQL with
`(75 − 30) × 4 = 180`, readiness dropped to 46%.

### Test 3 — Select Data Analyst
**Expected:** Data Analyst requirements shown (Python 70, SQL 75,
Statistics 70, Excel 65, Power BI 60) and 15 questions from those 5 topics.
**Result:** ✅ PASS

### Test 4 — Select Software Developer
**Expected:** Software Developer requirements (Python 70, Data Structures 75,
OOP 70, SQL 60, Git 60).
**Result:** ✅ PASS

### Test 5 — Select Web Developer
**Expected:** Web Developer requirements (HTML 75, CSS 70, JavaScript 75,
SQL 60, Git 55).
**Result:** ✅ PASS

### Additional automated checks (all ✅)
- data consistency: every topic has ≥ 2 questions, every answer is one of the
  four options, importance is 1–4, required level is 0–100,
  each career has 15 questions;
- formulas: gap `75−60=15`, negative gap → `0`, priority `30×4=120`,
  level 67 → Intermediate, readiness example → 77%;
- UI walk-through (26 checks): app starts without exception, 5 sidebar pages,
  profile saves, 3 careers, 15 questions, partial answers rejected
  (`Please answer all questions. 10 left.`), readiness `40%` for the designed
  answer set, report table sorted by priority, answer review expander,
  recommendations with reasons, empty name rejected, changing career clears old
  results, **no errors on any page**.

---


