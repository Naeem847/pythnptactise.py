class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Your Tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(i, "-", task)

    def remove_task(self, index):
        if 0 < index <= len(self.tasks):
            removed = self.tasks.pop(index - 1)
            print("Removed:", removed)
        else:
            print("Invalid task number")

# Create object
todo = TodoList()

# Using methods
todo.add_task("Study Python")
todo.add_task("Do Homework")
todo.view_tasks()

todo.remove_task(1)
todo.view_tasks()