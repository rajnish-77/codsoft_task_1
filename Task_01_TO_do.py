# ----------------------------------------
# CodSoft Python Internship
# Task 1 - To-Do List
# ----------------------------------------

tasks = []

while True:
    print("\n========== TO-DO LIST ==========")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        if len(tasks) == 0:
            print("\nNo tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "2":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available to update.")
        else:
            print("\nCurrent Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            try:
                task_no = int(input("Enter task number to update: "))
                if 1 <= task_no <= len(tasks):
                    new_task = input("Enter updated task: ")
                    tasks[task_no - 1] = new_task
                    print("Task updated successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available to delete.")
        else:
            print("\nCurrent Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            try:
                task_no = int(input("Enter task number to delete: "))
                if 1 <= task_no <= len(tasks):
                    removed = tasks.pop(task_no - 1)
                    print(f'"{removed}" deleted successfully!')
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "5":
        print("Thank you for using the To-Do List.")
        break

    else:
        print("Invalid choice! Please select between 1 and 5.")