my_tasks = []


def add_task():
    """Add a new task to the list."""

    task = input("Enter a new task: ")

    my_tasks.append(task)

    print("Task added successfully!\n")


def view_tasks():
    """Display all tasks."""

    if len(my_tasks) == 0:
        print("No tasks available.\n")
        return

    print("\n===== MY TO-DO LIST =====")

    for index, task in enumerate(my_tasks, start=1):
        print(f"{index}. {task}")

    print()


def main():

    while True:

        print("========== TO-DO LIST ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            print("\nThank you for using the To-Do List.")
            break

        else:
            print("\nInvalid choice. Please try again.\n")


if __name__ == "__main__":
    main()