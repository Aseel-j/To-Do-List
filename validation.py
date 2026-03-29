def input_and_validate_task_number(tasks):
    while True:
        try:
            task_number = int(input("Enter task number: "))
            if any(t.task_number == task_number for t in tasks):
                return task_number
            else:
                print("Task not found\n")
        except ValueError:
            print("Invalid task number\n")


def input_and_validate_priority():
    while True:
        try:
            priority = int(input("Enter priority between 0 and 5: "))
            if 0 <= priority <= 5:
                return priority
            else:
                print("Invalid priority. Choose a number between 0 and 5\n")
        except ValueError:
            print("Invalid priority\n")