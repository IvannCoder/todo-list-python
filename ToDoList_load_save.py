#  Load tasks from a file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

#  Save tasks to a file
def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

tasks = load_tasks()

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        new_task = input("Enter a new task: ")
        tasks.append(new_task)
        save_tasks(tasks)
        print("Task added!")

    elif choice == "2":
        print("\nYour Tasks:")
        if not tasks:
            print("No tasks yet.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        print("\nTasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        try:
            task_num = int(input("Enter the task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                save_tasks(tasks)
                print(f"Removed task: {removed}")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "4":
        print("Goodbye! Your tasks have been saved.")
        break

    else:
        print("Invalid choice! Please enter 1–4.")
