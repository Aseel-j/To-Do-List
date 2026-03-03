import json


tasks_list = []

def add_task (title,description,priority):
    tasks_number = len(tasks_list)+1
    task ={'tasks_number':tasks_number,
            'title':title,
            'description':description,
            'priority':priority,
            'status':False}
    tasks_list.append(task)
    print("Task Added\n")


#Get tasks function
def get_tasks():
    if len(tasks_list) == 0:
        print("No tasks found")
    else:
        for task in tasks_list:
            print(f"Task_number: {task['tasks_number']}\n",
                  f"Title: {task['title']}\n",
                  f"Description: {task['description']}\n",
                  f"Priority: {task['priority']}\n",
                  f"status: {'Done' if task['status'] else 'Not Done'}\n")


#sort tasks
def sort_tasks():
    sorted_task = sorted(tasks_list, key=lambda k: k['priority'])
    for task in sorted_task:
        print(f"Task_number: {task['tasks_number']}\n",
              f"Title: {task['title']}\n",
              f"Description: {task['description']}\n",
              f"Priority: {task['priority']}\n",
              f"status: {'Done' if task['status'] else 'Not Done'}\n")


# Mark Task as Done
def update_status():
    if len(tasks_list) == 0:
        print("No tasks found")
    else:
        get_tasks()
        while True :
            try:
                tasks_number =int(input("Enter task number: "))
                if tasks_number > len(tasks_list) :
                    print("Task not found \n")
                else:
                    tasks_list[tasks_number-1]['status'] = True
                    print("Task Updated\n")
                    break
            except ValueError:
                print("invalid task number\n")


#Change task priority
def update_priority():
    if len(tasks_list) == 0:
        print("No tasks found\n")
    else:
        get_tasks()
        while True:
            try:
                tasks_number =int(input("Enter task number: "))
                if tasks_number > len(tasks_list) :
                    print("Task not found \n")
                else:
                    while True:
                        try:
                            priority = int(input('Task priority between 0 and 5:'))
                            if priority < 0 or priority > 5:
                                print("invalid priority Choose a number between 0 and 5 \n")
                            else:
                                break
                        except ValueError:
                            print("invalid priority\n")
                    break
            except ValueError :
                print("invalid task number\n")



#Delet tasks
def delete_task():
    if len(tasks_list) == 0:
        print("No tasks found")
    else:
        get_tasks()
        while True:
            try:
                tasks_number =int(input("Enter task number: "))
                if tasks_number > len(tasks_list) :
                    print("Task not found \n")
                else:
                    tasks_list.remove(tasks_list[tasks_number - 1])
                    print("Task Deleted\n")
                    break
            except ValueError:
                print("invalid task number\n")


#save tasks list in to file
def save_tasks():
    with open("tasks.json", "w") as f:
        json.dump(tasks_list, f, indent=4)
        print("Tasks Saved\n")