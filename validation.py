#validation
def task_number_validation(tasks_list):
    while True:
        try:
            task_number =int(input("Enter task number: "))
            if task_number > len(tasks_list) or task_number < 1 :
                print("Task not found \n")
            else:
               return task_number
        except ValueError:
            print("invalid task number\n")


def priority_validation():
    while True:
        try:
            priority =int(input("Enter priority between 0 and 5:"))
            if priority < 0 or priority > 5:
                print("invalid priority Choose a number between 0 and 5 \n")
            else:
                return priority
        except ValueError:
            print("invalid priority\n")