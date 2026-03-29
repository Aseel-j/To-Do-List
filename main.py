from modules import TaskManager
from validation import input_and_validate_priority

manager = TaskManager()
manager.load_tasks()

while True:
    print('1. Add Task\n',
          '2. View Tasks\n',
          '3. Sort Tasks\n',
          '4. Mark Task as Done\n',
          '5. Change Priority\n',
          '6. Delete Task\n',
          '7. Exit\n',
          '8. Save\n',)

    while True:
        try:
            input_number = int(input('Choose an option:'))
            if input_number > 8 or input_number < 1 :
                print("invalid option Choose a number between 1 and 8.\n")
            else:
                break
        except ValueError:
            print("invalid option\n")
    match input_number:
        case 1:
            title = input('Task title:')
            description = input('Task description:')
            priority= input_and_validate_priority()
            manager.add_task(title,description,priority)
        case 2:
            manager.print_tasks()
        case 3:
            manager.sort_tasks()
        case 4:
            manager.update_status()
        case 5:
            manager.update_priority()
        case 6:
            manager.delete_task()
        case 7:
            exit()
        case 8:
            manager.save_tasks()
