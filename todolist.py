to_do_list = []

def display_menu():
    print()
    print("1. View tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")
    print()

def view_tasks():
    if not to_do_list:
        print("You dont have any tasks to complete")
        return
    for i,task in enumerate(to_do_list,start=1):
        print("\n Your tasks")
        print(f"{i}. {task}")

def add_task():
    task = input("Enter your task to add: ")
    to_do_list.append(task)
    print(f"Your {task} is added successfully")


def delete_task():
    view_tasks()
    if not to_do_list:
        return
    try:
        task = int(input("Eneter your task number to delete: "))
        if 1 <= task <= len(to_do_list):
            to_do_list.pop(task-1)
            print(f"Your task {task} is deleted successfull")
        else:
            print("Enter a avalid task number")
    except ValueError:
        print("Eneter a valid number")

while True:
    display_menu()
    choice = int(input("choose an option from 1-4: "))
     
    if choice == 1:
        view_tasks()
    elif choice == 2:
        add_task()
    elif choice == 3:
        delete_task()
    elif choice == 4:
        print("Your are exiting from to_do-list")
        break

    else:
        print("Eneter a valid number")


    
