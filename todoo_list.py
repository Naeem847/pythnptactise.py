def display_menu():
    print("To_do list display menu:")
    print("1.view_task")
    print("2.Add_task")
    print("3.Delete_task")
    print("4.Exit")

def view_task(tasks):
        if not tasks:
            print("No tasks available!!!")
        else:
            print("your tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
def add_task(tasks):
    task=input("enter your task you want  to add!!!")
    tasks.append(task)
    print("task added successfully!!!")
def delete_task(tasks):
    view_task(tasks)
    try:
           if 1<=task_num<=len(tasks):
                removed_task=tasks.pop(task_num-1)
                print(f"task '{removed_task}' deleted successfully!!!")
            else:
               print("invalid task number!!!")
    except ValueError:
            print("please enter a valid number!!!")    
               
def to_do_list_app():
    tasks=[]
    while True:
        display_menu()
        choice=input("Enter your choice: ")
        if choice=="1":
            view_task(tasks)
        elif choice=="2":
            add_task(tasks)
        elif choice=="3":
            delete_task(tasks) 
        elif choice=="4":
            print("exiting the app good bye!!!")
            break
        else:
            print("invalid chice please try again!!!")
to_do_list_app()
        
    
