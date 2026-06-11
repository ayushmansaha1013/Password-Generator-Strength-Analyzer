# 🔐 Password Generator & Strength Analyzer

A robust, command-line Python application that generates secure, customizable passwords and evaluates their strength using a feature-based scoring algorithm. Built to practice core Python programming, data validation, and file persistence.

## 🚀 Features

### Core (MVP)
- **Custom Generation:** Generate random passwords of user-specified lengths.
- **Strength Analyzer:** Evaluates passwords based on length, uppercase, lowercase, digits, and special characters.
- **Scoring System:** Outputs a clear strength score (0-10) with actionable feedback.

### Advanced
- **Input Validation:** Robust `try/except` blocks to handle invalid user inputs gracefully (e.g., typing letters instead of numbers).
- **Persistent History:** Automatically logs generated passwords and their scores to a local `history.csv` file.
- **History Viewer:** Retrieves and displays the last 5 generated passwords from the log.

## 🛠️ Tech Stack & Topics Covered
- **Language:** Python 3.x
- **Core Concepts:** Functions, Loops, Conditionals, String Manipulation, Dictionaries
- **Modules:** `random`, `string`, `csv` (or `os`)
- **Advanced Topics:** Exception Handling, File I/O, Virtual Environments

## 📂 Project Structure
```text
password_analyzer/
├── venv                   # Virtual environment
├── main.py                # Main application logic and CLI menu
├── requirements.txt       # (Optional, if any external packages are added)
└── README.md              # Project documentation

git clone https://github.com/[Your-Username]/password-analyzer.git
cd password-analyzer

python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
