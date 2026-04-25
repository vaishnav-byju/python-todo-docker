from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

# In-memory task list
tasks = []

# HTML template
template = """
<!DOCTYPE html>
<html>
<head>
    <title>Python To-Do App</title>
</head>
<body>
    <h1>My To-Do List</h1>
    <form method="POST" action="/add">
        <input type="text" name="task" placeholder="Enter new task" required>
        <button type="submit">Add Task</button>
    </form>
    <ul>
        {% for task in tasks %}
        <li>
            {{ task }}
            <a href="/delete/{{ loop.index0 }}">Delete</a>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(template, tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    if task:
        tasks.append(task)
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>")
def delete(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
