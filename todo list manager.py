class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True

    def view_list(self):
        for i, task in enumerate(self.tasks):
            status = "Completed" if task.completed else "Not Completed"
            print(f"{i+1}. {task.description} - {status}")

    def remove_completed_tasks(self):
        self.tasks = [task for task in self.tasks if not task.completed]


# Create a TodoList object
todo_list = TodoList()

# User interaction loop
while True:
    print("Todo List Menu:")
    print("1. Add a task")
    print("2. Mark a task as complete")
    print("3. View current tasks")
    print("4. Remove completed tasks")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        description = input("Enter task description: ")
        todo_list.add_task(description)
    elif choice == '2':
        index = int(input("Enter the index of the task to mark as complete: ")) - 1
        todo_list.mark_task_complete(index)
    elif choice == '3':
        print("Current Tasks:")
        todo_list.view_list()
    elif choice == '4':
        todo_list.remove_completed_tasks()
        print("Completed tasks have been removed.")
    elif choice == '0':
        print("Exiting the todo list.")
        break
    else:
        print("Invalid choice. Please try again.")