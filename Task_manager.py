tasks = []
tasks_history = []


def display_options():
    print("\n=== TASK MANAGER ===")
    print("1. Add Task")
    print("2. View Task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("0. Exit")
    print("=====================")


def add_task():
    task = input("Enter task title: ").title()
    tasks.append(task)
    tasks_history.append(0)
    print(f"Task '{task}'added Successfully")


def display_tasks():

    if len(tasks) == 0:
        print("\nNo tasks found")
        return

    print("\n=== My Tasks ===")
    for i, task in enumerate(tasks):
        print(f"{i+1} {'[]' if tasks_history[i] == 0 else '[✅]' } {task}")
    print("==================")


def complete_task():

    while True:
        try:
            task_no = int(input("\nEnter task number to mark as completed: "))
            if task_no > len(tasks):
                if len(tasks) == 0:
                    print("Please add tasks")
                else:
                    print("Enter Task Number Carefully ")
                return
            tasks_history[task_no-1] = 1
            print(f"Task '{tasks[task_no - 1]}' marked as completed!")
            return
        except ValueError:
            print("Please enter a number")
        except IndexError:
            print("Please enter a number that task has to completed")


def delete_task():
    while True:
        try:
            task_no = int(input("\nEnter task number to be delete: "))
            if task_no > len(tasks):
                if len(tasks) == 0:
                    print("Please add tasks")
                else:
                    print("Enter Task Number Carefully ")
                return
            task = tasks[task_no - 1]
            del tasks[task_no - 1]
            del tasks_history[task_no - 1]
            print(f"Task '{task}' Deleted!")
            return
        except ValueError:
            print("Please enter a number")
        except IndexError:
            print("Please enter a number that task has to deleted")


def main():
    while True:
        display_options()
        try:
            choice = int(input("Enter your choice (0-4): "))

            if choice == 1:
                add_task()
            elif choice == 2:
                display_tasks()
            elif choice == 3:
                display_tasks()
                complete_task()
            elif choice == 4:
                display_tasks()
                delete_task()
            elif choice == 0:
                print("\nThank you GoodBye")
                break
            else:
                print("Please enter a number(0 - 1)")

        except ValueError:
            print("Please enter a number")


main()
