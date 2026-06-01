FILE_NAME = "tasks.txt"
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []
def save_tasks():
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")
def view_tasks():
    print("\n--- TO-DO LIST ---")
    if not tasks:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
def add_task():
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks()
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")
def remove_task():
    view_tasks()
    if not tasks:
        return
    try:
        number = int(input("Enter task number to remove: "))
        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            save_tasks()
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
tasks = load_tasks()
while True:
    print("\n--- MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
    choice = input("Choose an option (1-4): ")
    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("\nThank you for using To-Do List App!")
        break
    else:
        print("Invalid choice. Please select 1-4.")