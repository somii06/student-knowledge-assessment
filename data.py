"""
data.py
-------
All data of the project is stored here (no database, no files, no API).

Contents:
  1. careers        -> topics required by each career (required level + importance)
  2. questions      -> question bank (question, 4 options, correct answer, topic)
  3. recommendations-> topics to study for every subject
  4. importance_labels -> converts importance number to a readable name
"""

# importance: 1 = Low, 2 = Medium, 3 = High, 4 = Very High
importance_labels = {1: "Low", 2: "Medium", 3: "High", 4: "Very High"}

# ----------------------------------------------------------------------
# 1. CAREER REQUIREMENTS
#    required  -> knowledge (in %) the student should have
#    importance-> how important the topic is for that career (1 to 4)
# ----------------------------------------------------------------------
careers = {
    "Data Analyst": {
        "Python":    {"required": 70, "importance": 3},
        "SQL":       {"required": 75, "importance": 4},
        "Statistics": {"required": 70, "importance": 4},
        "Excel":     {"required": 65, "importance": 2},
        "Power BI":  {"required": 60, "importance": 3},
    },
    "Software Developer": {
        "Python":          {"required": 70, "importance": 3},
        "Data Structures": {"required": 75, "importance": 4},
        "OOP":             {"required": 70, "importance": 3},
        "SQL":             {"required": 60, "importance": 2},
        "Git":             {"required": 60, "importance": 2},
    },
    "Web Developer": {
        "HTML":       {"required": 75, "importance": 2},
        "CSS":        {"required": 70, "importance": 3},
        "JavaScript": {"required": 75, "importance": 4},
        "SQL":        {"required": 60, "importance": 1},
        "Git":        {"required": 55, "importance": 3},
    },
}

# ----------------------------------------------------------------------
# 2. QUESTION BANK
#    11 topics x 3 questions = 33 questions
#    every career uses 5 topics -> 15 questions per career
# ----------------------------------------------------------------------
questions = [
    # ---------------- Python ----------------
    {"topic": "Python", "question": "Which keyword is used to define a function in Python?",
     "options": ["function", "def", "define", "func"], "answer": "def"},
    {"topic": "Python", "question": "Which of these is created using square brackets [ ]?",
     "options": ["list", "tuple", "set", "dictionary"], "answer": "list"},
    {"topic": "Python", "question": "What does the len() function return?",
     "options": ["The number of items in a collection", "The sum of all values",
                 "The largest value", "The type of a variable"],
     "answer": "The number of items in a collection"},

    # ---------------- SQL ----------------
    {"topic": "SQL", "question": "Which SQL clause is used to filter rows in a table?",
     "options": ["WHERE", "ORDER", "GROUP", "TABLE"], "answer": "WHERE"},
    {"topic": "SQL", "question": "Which function counts the number of rows?",
     "options": ["SUM()", "COUNT()", "AVG()", "MAX()"], "answer": "COUNT()"},
    {"topic": "SQL", "question": "Which keyword is used to combine rows from two related tables?",
     "options": ["JOIN", "MERGE", "APPEND", "STACK"], "answer": "JOIN"},

    # ---------------- Statistics ----------------
    {"topic": "Statistics", "question": "The average of a set of numbers is called:",
     "options": ["Mean", "Mode", "Range", "Sum"], "answer": "Mean"},
    {"topic": "Statistics", "question": "Which value appears most often in a data set?",
     "options": ["Mean", "Median", "Mode", "Range"], "answer": "Mode"},
    {"topic": "Statistics", "question": "Correlation measures:",
     "options": ["the strength of the relationship between two variables",
                 "the average of a data set",
                 "the difference between the highest and lowest values",
                 "the number of records"],
     "answer": "the strength of the relationship between two variables"},

    # ---------------- Excel ----------------
    {"topic": "Excel", "question": "Which function is used to add numbers in Excel?",
     "options": ["SUM", "AVERAGE", "COUNT", "MAX"], "answer": "SUM"},
    {"topic": "Excel", "question": "What does the cell reference B2 mean?",
     "options": ["Column B, Row 2", "Row B, Column 2", "Second column only",
                 "A named range"],
     "answer": "Column B, Row 2"},
    {"topic": "Excel", "question": "Which symbol must start a formula in Excel?",
     "options": ["=", "+", "#", "$"], "answer": "="},

    # ---------------- Power BI ----------------
    {"topic": "Power BI", "question": "What is Power BI mainly used for?",
     "options": ["Creating interactive reports and dashboards from data",
                 "Writing Python programs", "Sending emails", "Designing websites"],
     "answer": "Creating interactive reports and dashboards from data"},
    {"topic": "Power BI", "question": "Which chart is best to show a trend over time?",
     "options": ["Line chart", "Pie chart", "Gauge", "Card"], "answer": "Line chart"},
    {"topic": "Power BI", "question": "What does a filter do in Power BI?",
     "options": ["Shows only a selected part of the data", "Deletes the data",
                 "Calculates the average", "Exports data to PDF"],
     "answer": "Shows only a selected part of the data"},

    # ---------------- Data Structures ----------------
    {"topic": "Data Structures", "question": "Which data structure works on the LIFO (Last In First Out) principle?",
     "options": ["Stack", "Queue", "Tree", "Graph"], "answer": "Stack"},
    {"topic": "Data Structures", "question": "Which data structure works on the FIFO (First In First Out) principle?",
     "options": ["Queue", "Stack", "Array", "Tree"], "answer": "Queue"},
    {"topic": "Data Structures", "question": "What is the average time complexity of binary search on a sorted array?",
     "options": ["O(log n)", "O(1)", "O(n)", "O(n^2)"], "answer": "O(log n)"},

    # ---------------- OOP ----------------
    {"topic": "OOP", "question": "When a class acquires the properties of another class, it is called:",
     "options": ["Inheritance", "Polymorphism", "Encapsulation", "Abstraction"],
     "answer": "Inheritance"},
    {"topic": "OOP", "question": "Wrapping data and functions together inside a class is called:",
     "options": ["Encapsulation", "Inheritance", "Abstraction", "Compilation"],
     "answer": "Encapsulation"},
    {"topic": "OOP", "question": "When the same function name behaves differently in different classes, it is called:",
     "options": ["Polymorphism", "Inheritance", "Encapsulation", "Overloading"],
     "answer": "Polymorphism"},

    # ---------------- Git ----------------
    {"topic": "Git", "question": "Which command downloads a repository for the first time?",
     "options": ["git clone", "git push", "git commit", "git checkout"],
     "answer": "git clone"},
    {"topic": "Git", "question": "Which command saves changes to the local repository?",
     "options": ["git commit", "git push", "git fetch", "git remote"],
     "answer": "git commit"},
    {"topic": "Git", "question": "What does git push do?",
     "options": ["Uploads local commits to the remote repository",
                 "Downloads the latest code", "Shows the status",
                 "Creates a new folder"],
     "answer": "Uploads local commits to the remote repository"},

    # ---------------- HTML ----------------
    {"topic": "HTML", "question": "Which tag is used for the largest heading?",
     "options": ["<h1>", "<head>", "<title>", "<header>"], "answer": "<h1>"},
    {"topic": "HTML", "question": "Which tag is used to create a hyperlink?",
     "options": ["<a>", "<link>", "<href>", "<url>"], "answer": "<a>"},
    {"topic": "HTML", "question": "Which tag is used to display an image?",
     "options": ["<img>", "<picture>", "<src>", "<media>"], "answer": "<img>"},

    # ---------------- CSS ----------------
    {"topic": "CSS", "question": "Which property is used to change the text colour?",
     "options": ["color", "text-color", "font-color", "background"], "answer": "color"},
    {"topic": "CSS", "question": 'Which selector targets an element with id="header"?',
     "options": ["#header", ".header", "header", "*header"], "answer": "#header"},
    {"topic": "CSS", "question": "Which property is used to set the background colour?",
     "options": ["background-color", "bg-color", "fill", "back-color"],
     "answer": "background-color"},

    # ---------------- JavaScript ----------------
    {"topic": "JavaScript", "question": "Which keyword declares a constant that cannot be reassigned?",
     "options": ["const", "let", "var", "static"], "answer": "const"},
    {"topic": "JavaScript", "question": "What does document.getElementById() do?",
     "options": ["Finds an HTML element by its id", "Prints the document",
                 "Creates a new page", "Loads a CSS file"],
     "answer": "Finds an HTML element by its id"},
    {"topic": "JavaScript", "question": "Which function prints a message in the browser console?",
     "options": ["console.log()", "print()", "echo()", "show()"],
     "answer": "console.log()"},
]

# ----------------------------------------------------------------------
# 3. STUDY RECOMMENDATIONS (concepts to study for every topic)
# ----------------------------------------------------------------------
recommendations = {
    "Python": ["Functions", "OOP", "File Handling", "List Comprehension"],
    "SQL": ["JOIN", "GROUP BY", "Subqueries", "Indexes"],
    "Statistics": ["Probability", "Standard Deviation", "Correlation", "Regression"],
    "Excel": ["VLOOKUP", "Pivot Tables", "Charts", "Conditional Formatting"],
    "Power BI": ["Data Modelling", "DAX Basics", "Dashboards", "Data Cleaning"],
    "Data Structures": ["Arrays", "Linked Lists", "Stacks and Queues", "Trees"],
    "OOP": ["Classes and Objects", "Inheritance", "Polymorphism", "Encapsulation"],
    "Git": ["Commit and Push", "Branching", "Merge Conflicts", "Pull Requests"],
    "HTML": ["Forms", "Semantic Tags", "Tables", "Media Tags"],
    "CSS": ["Selectors", "Flexbox", "Grid", "Responsive Design"],
    "JavaScript": ["DOM Manipulation", "Events", "Functions", "ES6 Syntax"],
}
