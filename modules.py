import json

from validation import task_number_validation, priority_validation

tasks_list = []

def add_task (title,description,priority):
    task_number = len(tasks_list) + 1
    task ={'task_number':task_number,
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
            print(f"Task_number: {task['task_number']}\n",
                  f"Title: {task['title']}\n",
                  f"Description: {task['description']}\n",
                  f"Priority: {task['priority']}\n",
                  f"status: {'Done' if task['status'] else 'Not Done'}\n")


#sort tasks
def sort_tasks():
    sorted_task = sorted(tasks_list, key=lambda k: k['priority'])
    for task in sorted_task:
        print(f"Task_number: {task['task_number']}\n",
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
        task_number =task_number_validation(tasks_list)
        tasks_list[task_number-1]['status'] = True
        print("Task Status Updated\n")


#Change task priority
def update_priority():
    if len(tasks_list) == 0:
        print("No tasks found\n")
    else:
        get_tasks()
        task_number =task_number_validation(tasks_list)
        tasks_list[task_number-1]['priority'] = priority_validation()
        print("Task Priority Updated\n")


#Delet tasks
def delete_task():
    if len(tasks_list) == 0:
        print("No tasks found")
    else:
        get_tasks()
        task_number =task_number_validation(tasks_list)
        tasks_list.remove(tasks_list[task_number - 1])
        print("Task Deleted\n")


#save tasks list in to file
def save_tasks():
    if len(tasks_list) == 0:
        print("No tasks found")
    else:
        with open("tasks.json", "w") as f:
            json.dump(tasks_list, f, indent=4)
            print("Tasks Saved\n")
