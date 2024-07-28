tasks = []

def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" added!')

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("Your tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def update_task(index, new_task):
    if 0 <= index < len(tasks):
        tasks[index] = new_task
        print(f'Task updated to "{new_task}".')
    else:
        print("Invalid task index.")

def remove_task(index):
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        print(f'Task "{removed_task}" removed.')
    else:
        print("Invalid task index.")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Remove Task")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            index = int(input("Enter the task index to update: ")) - 1
            new_task = input("Enter the new task: ")
            update_task(index, new_task)
        elif choice == '4':
            index = int(input("Enter the task index to remove: ")) - 1
            remove_task(index)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
