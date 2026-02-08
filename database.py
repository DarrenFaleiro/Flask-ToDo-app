import sqlite3

DATABASE_NAME = "todo.db"


# Create a connection to the database
def get_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn


# Create table
def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        completed INTEGER DEFAULT 0
    )
    """)

    conn.commit()
    conn.close()


# CREATE
def add_task(task):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO todos (task) VALUES (?)", (task,))
    conn.commit()
    conn.close()


# READ
def get_all_tasks():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM todos ORDER BY id DESC")
    tasks = cursor.fetchall()

    conn.close()
    return tasks


# UPDATE
def update_task(task_id, new_task):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE todos SET task = ? WHERE id = ?",
        (new_task, task_id)
    )

    conn.commit()
    conn.close()


# COMPLETE
def complete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE todos SET completed = 1 WHERE id = ?",
        (task_id,)
    )

    conn.commit()
    conn.close()


# DELETE
def delete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM todos WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
