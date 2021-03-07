""" To create a do list  in file  """

list_to_do = []  # Empty list to add task
count_task = 0


def update_file():  # Erase the data of the file and write data from scratch
    with open("to do list.txt", "r+") as f:
        f.truncate(0)  # del contain in file
        for line in list_to_do:
            f.write(f"{line}\n")


def clear_list():  # clear all the data from file
    list_to_do.clear()
    update_file()
    print("List is Cleared")


def add_item():
    user = str((input("Enter the name of the task to do : ")))
    list_to_do.append(f"{count_task}. {user}")
    with open("to do list.txt", "a+") as f:
        f.truncate(0)
        for line in list_to_do:
            f.write(f"{line}\n")


def remove_item():
    del list_to_do[- 1]  # del last element in list
    update_file()
    print(" Last Item is removed for list ....")


def is_Complete():
    num = int(input("Enter which number of task is done "))
    list_to_do[num - 1] = list_to_do[num - 1] + "   Task Done   "
    update_file()


def task_remain():
    remain = 0
    print("Remaining Task \n")
    for line in list_to_do:
        if "Task Done" not in line:
            print(line + "\n")
            remain += 1
    print(f" Total Task Remain to do are {remain}")


def all_task():
    print(" To do  list  :\n")
    with open("to do list.txt", "r") as f:
        read_task = f.read()
        print(read_task)


print("Welcome To Do List")
while True:
    choice = int(input(" press 1 : to add item to list \n press 2 : to remove item \n press 3 : to check completed  \
    \n press 4: to see remain task \n press 5 : to see all task\n press 6 : to clear list \n press 7 : quit\n  "))
    if choice == 1:
        count_task = len(list_to_do) + 1
        add_item()
    elif choice == 2:
        remove_item()
    elif choice == 3:
        is_Complete()
    elif choice == 4:
        task_remain()
    elif choice == 5:
        all_task()
    elif choice == 6:
        clear_list()
    elif choice == 7:
        break
    else:
        print("Enter the valid range number ")
        continue
