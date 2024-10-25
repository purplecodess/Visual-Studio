Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Define an empty list to store tasks
tasks = []
... 
... # Function to add a task
... def add_task(task):
...     tasks.append(task)
...     print("Task added successfully!")
... 
... # Function to view all tasks
... def view_tasks():
...     if tasks:
...         print("Tasks:")
...         for task in tasks:
...             print("- " + task)
...     else:
...         print("No tasks yet!")
... 
... # Main function
... def main():
...     while True:
...         print("\nMenu:")
...         print("1. Add a task")
...         print("2. View tasks")
...         print("3. Quit")
... 
...         choice = input("Enter your choice: ")
... 
...         if choice == "1":
...             task = input("Enter the task: ")
...             add_task(task)
...         elif choice == "2":
...             view_tasks()
...         elif choice == "3":
...             print("Goodbye!")
...             break
...         else:
...             print("Invalid choice!")
... 
... # Run the main function
... if __name__ == "__main__":
...     main()
