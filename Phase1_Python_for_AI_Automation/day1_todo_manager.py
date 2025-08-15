import os 
import msvcrt 

while True: 
    print("Welcome to the Todo Manager!") 
    print("Please select an option:") 
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Delete a task") 
    print("4. Exit") 

    option = int(input("Enter your choice (1-4): ")) 
    total_tasks = 0 

    if os.path.exists("total_tasks.txt"): 
        with open("total_tasks.txt", "r") as file:
            total_tasks = int(file.read().strip()) 

    if option == 1: 
        task = input("Enter the task: ") 
        total_tasks += 1 
        with open("tasks.txt", "a") as file: 
            file.write(f"Task : {task}\n") 
        with open("total_tasks.txt", "w") as file: 
            file.write(str(total_tasks)) 
        print(f"Task {total_tasks} added successfully!\n") 
    elif option == 2: 
        if os.path.exists("tasks.txt"): 
            with open("tasks.txt", "r") as file: 
                print(file.read())
        else: 
            print("No tasks found.\n") 
    elif option == 3: 
        if os.path.exists("tasks.txt"): 
            task_number = int(input("Enter the task number to delete: ")) 
            if task_number < 1 or task_number > total_tasks: 
                print("Invalid task number.\n") 
            with open("tasks.txt", "r") as file: 
                lines = file.readlines() 
            with open("tasks.txt", "w") as file:
                for (index, line) in enumerate(lines, start=1): 
                    if index != task_number: 
                        file.write(line) 
            total_tasks -= 1
            with open("total_tasks.txt", "w") as file: 
                file.write(str(total_tasks)) 
            print(f"Task {task_number} deleted successfully!\n") 
        else: 
            print(f"No tasks found to delete.\n")
    else: 
        print("Exiting the Todo Manager. Goodbye!\n")
        break

    print("press any key to continue..")
    msvcrt.getch() 
    os.system("cls")

