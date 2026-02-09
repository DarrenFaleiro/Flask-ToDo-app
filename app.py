from flask import Flask, render_template, request, redirect, url_for
import database

app = Flask(__name__)

# Create DB table on startup
database.create_table()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form["task"]
        if task.strip():
            database.add_task(task)
        return redirect(url_for("index"))

    tasks = database.get_all_tasks()
    return render_template("index.html", tasks=tasks)


@app.route("/update/<int:task_id>", methods=["POST"])
def update(task_id):
    new_task = request.form["new_task"]
    if new_task.strip():
        database.update_task(task_id, new_task)
    return redirect(url_for("index"))


@app.route("/complete/<int:task_id>")
def complete(task_id):
    database.complete_task(task_id)
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>")
def delete(task_id):
    database.delete_task(task_id)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)

