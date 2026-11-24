
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


class TodoList:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    # Add a new task
    def add_task(self, task, priority):
        self.tasks.append({
            "id": self.next_id,
            "task": task,
            "priority": priority,
            "completed": False
        })
        self.next_id += 1

    # Delete a task
    def remove_task(self, task_id):
        self.tasks = [
            task for task in self.tasks
            if task["id"] != task_id
        ]

    # Mark task as completed or pending
    def toggle_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = not task["completed"]

    # Edit task
    def edit_task(self, task_id, new_task):
        for task in self.tasks:
            if task["id"] == task_id:
                task["task"] = new_task

    # Search tasks
    def search_tasks(self, keyword):
        return [
            task for task in self.tasks
            if keyword.lower() in task["task"].lower()
        ]


todo = TodoList()


@app.route('/')
def home():
    keyword = request.args.get('search', '')
    status = request.args.get('status', 'all')

    tasks = todo.search_tasks(keyword) if keyword else todo.tasks

    if status == 'completed':
        tasks = [t for t in tasks if t["completed"]]

    elif status == 'pending':
        tasks = [t for t in tasks if not t["completed"]]

    total = len(todo.tasks)
    completed = sum(1 for t in todo.tasks if t["completed"])
    pending = total - completed

    return render_template(
        'index.html',
        tasks=tasks,
        total=total,
        completed=completed,
        pending=pending,
        search=keyword,
        status=status
    )


# Add task
@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task', '').strip()
    priority = request.form.get('priority', 'Medium')

    if task:
        todo.add_task(task, priority)

    return redirect(url_for('home'))


# Delete task
@app.route('/delete/<int:task_id>', methods=['POST'])
def delete(task_id):
    todo.remove_task(task_id)
    return redirect(url_for('home'))


# Complete task
@app.route('/toggle/<int:task_id>', methods=['POST'])
def toggle(task_id):
    todo.toggle_task(task_id)
    return redirect(url_for('home'))


# Edit task
@app.route('/edit/<int:task_id>', methods=['POST'])
def edit(task_id):
    new_task = request.form.get('task', '').strip()

    if new_task:
        todo.edit_task(task_id, new_task)

    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
