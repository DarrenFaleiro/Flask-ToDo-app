# 📋 Flask To-Do List Application

## 📌 Project Overview

This project is a **Python Flask-based To-Do List application** for the web.
It allows users to manage tasks through a modern, desktop-friendly interface, with card-style task boards, colored status indicators, and a responsive layout.
The application uses **SQLite3 (built-in database)** for data storage and includes **CRUD operations**, **automated testing with pytest**, and a **Continuous Integration (CI) pipeline** via GitHub Actions..

The system demonstrates core programming concepts such as variables, conditionals, loops, functions, database connectivity, and automated testing.

---

## 🎯 Features

- Add a new task (centered, wide layout)
- View tasks in card-style board
- Update existing tasks inline
- Mark tasks as completed ✅
- Delete tasks 🗑
- Task statuses visually indicated (Pending / Completed)
- Responsive grid layout for desktop web
- Logo and modern navbar
- Automated unit testing with pytest
- CI pipeline using GitHub Actions

---

## 🧱 Technologies Used

- **Python 3**
- **Flask**
- **SQLite3**
- **HTML & CSS**
- **Pytest**
- **GitHub Actions**

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
│ ├── style.css
│ └── logo.png
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

- git clone https://github.com/darrenfaleiro/flask-todo.git
- cd flask-todo

### 2️⃣ Create and activate virtual environment

- python -m venv venv
- venv\Scripts\activate

### 3️⃣ Install dependencies

- pip install --upgrade pip
- pip install -r requirements.txt

### ▶️ Running the Application

- python app.py
- Open your browser and visit: http://127.0.0.1:5000

### 🧪 Running Unit Tests

- python -m pytest

### 🧪 Example output:
---
- collected 5 items
- test_app.py::test_home_page PASSED
- test_app.py::test_add_task PASSED
- test_app.py::test_update_task PASSED
- test_app.py::test_complete_task PASSED
- test_app.py::test_delete_task PASSED
- 5 passed in 0.85s
---
### 🔁 Continuous Integration (CI)

- A CI pipeline has been implemented using: GitHub Actions
- CI Pipeline Steps:
- Triggered on push or pull request
- Sets up Python environment
- Installs dependencies
- Runs pytest
- Fails build if any test fails
- This ensures code quality and early detection of errors.

### 🎨 UI / Design

- Desktop-first layout with grid-style task board
- Add Task form centered and wide
- Tasks are displayed in cards with colored borders for status
- Inline task editing and actions (Edit / Complete / Delete)
- Modern sticky navbar with logo and centered app title
