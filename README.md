# 📝 Flask To-Do Application

## 📌 Project Overview

This project is a **Python Flask-based To-Do application** that allows users to manage tasks using a web interface.  
The application uses **SQLite3 (built-in database)** for data storage and includes **CRUD operations**, **automated testing with pytest**, and a **Continuous Integration (CI) pipeline**.

The system demonstrates core programming concepts such as variables, conditionals, loops, functions, database connectivity, and automated testing.

---

## 🎯 Features

- Add a new task
- View all tasks
- Update existing tasks
- Mark tasks as completed
- Delete tasks
- Simple and user-friendly interface
- Automated unit testing
- CI pipeline using GitHub Actions

---

## 🧱 Technologies Used

- **Python 3**
- **Flask**
- **SQLite3**
- **HTML & CSS**
- **Pytest**
- **GitHub Actions / Azure DevOps (CI)**

---

## 📂 Project Folder Structure

FLASK-TODO/
│
├── app.py
├── database.py
├── test_app.py
├── requirements.txt
├── README.md
│
├── static/
│ └── style.css
│
├── templates/
│ ├── base.html
│ └── index.html
│
└── venv/

---

## 🔗 Database Design

The application uses an **SQLite3 database** with a single table:

### `todos` Table

| Column    | Type    | Description                |
| --------- | ------- | -------------------------- |
| id        | INTEGER | Primary Key                |
| task      | TEXT    | Task description           |
| completed | INTEGER | 0 = Pending, 1 = Completed |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

### 2️⃣ Create and activate virtual environment

python -m venv venv
venv\Scripts\activate

### 3️⃣ Install dependencies

### ▶️ Running the Application

python app.py
Open your browser and visit: http://127.0.0.1:5000

### 🧪 Running Unit Tests

python -m pytest

### 🔁 Continuous Integration (CI)

A CI pipeline has been implemented using: GitHub Actions
CI Pipeline Steps:

Triggered on push or pull request

Sets up Python environment

Installs dependencies

Runs pytest

Fails build if any test fails

This ensures code quality and early detection of errors.
