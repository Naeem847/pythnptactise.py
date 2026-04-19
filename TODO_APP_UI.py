from flask import Flask, render_template, request, redirect

app = Flask(__name__)

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 < index <= len(self.tasks):
            self.tasks.pop(index - 1)
            
todo = TodoList()

@app.route('/')
def home():
    return render_template('index.html', tasks=todo.tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    todo.add_task(task)
    return redirect('/')

@app.route('/delete/<int:index>')
def delete(index):
    todo.remove_task(index)
    return redirect('/')

app.run(debug=True)