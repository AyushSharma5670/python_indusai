# To-Do List Application
# Define the to-do list
todo_list = []

# Function to add a task to the to-do list
def add_task(task):
    todo_list.append(task)
    print(f'Task "{task}" has been added.')

# Function to view all tasks in the to-do list
def view_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for idx, task in enumerate(todo_list, start=1):
    #Enumerate is a built-in function in python that allows you to keep track of the number of iterations(loops) in a loop.
            print(f"{idx}. {task}")

# Function to delete a task from the to-do list
def delete_task(task_number):
    try:
        task = todo_list.pop(task_number - 1)
        print(f'Task "{task}" has been deleted.')
    except IndexError:
        print("Invalid task number. Please try again.")

# Main function to run the to-do list manager
def todo_list_manager():
    print("Welcome to the To-Do List Manager!")

    while True:
        print("\nOptions:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Delete a task")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            task = input("Enter your task: ")
            add_task(task)
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            try:
                task_number = int(input("Enter the task number to delete: "))
                delete_task(task_number)
            except ValueError:
                print("Invalid input!!! Please enter a valid task number.")
        elif choice == 4:
            print("Thank you")
            break
        else:
            print("Invalid choice!!! Please enter a number between 1 & 4.")

# Start the to-do list manager
todo_list_manager()
