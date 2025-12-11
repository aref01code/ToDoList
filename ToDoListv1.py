import os
tasks = []

def clr_screen():
    os.system('cls')
    

def load_history():  
    # Get the path ...
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "ToDoList.txt")

    with open(file_path, "r") as file:
        global tasks    
        tasks =  tasks + file.readlines()
    
def save_history(task):
    # Get the path ...
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "ToDoList.txt")

    with open(file_path, "a") as file:
        file.write(task + "\n")
        
def delete_history(num):
    # Get the path ...
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "ToDoList.txt")

    with open(file_path, "r") as fr:
        lines = fr.readlines()    
    
    x = 1 
    with open(file_path,"w") as fw :
        for line in lines :
            if x != num :
                fw.write(line)
            x += 1
        
        
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    save_history(task)
    print("Task added!\n")
    

def view_tasks():
    if not tasks:
        print("No tasks yet!\n")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def delete_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter the task number to delete: "))
            removed = tasks.pop(task_num - 1)
            delete_history(task_num)
            print(f"Deleted: {removed}\n")
        except (ValueError, IndexError):
            print("Invalid task number!\n")
     
            
load_history()

while True:
    print("=== To-Do List ===")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
        input("Press Enter to continiue ...")
        clr_screen()
    elif choice == "2":
        view_tasks()
        input("Press Enter to continiue ...")
        clr_screen()
    elif choice == "3":
        delete_task()
        input("Press Enter to continiue ...")
        clr_screen()
    elif choice == "4":
        clr_screen()
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.\n")
        input("Press Enter to continiue ...")
        clr_screen()