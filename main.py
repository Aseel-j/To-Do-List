from modules import add_task, get_tasks, sort_tasks, update_status, update_priority, delete_task, save_tasks

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
            while True:
                try:
                    priority =int(input('Task priority between 0 and 5:'))
                    if priority < 0 or priority > 5:
                        print("invalid priority Choose a number between 0 and 5 \n")
                    else:
                        break
                except ValueError:
                    print("invalid priority\n")
            add_task(title,description,priority)
        case 2:
            get_tasks()
        case 3:
            sort_tasks()
        case 4:
            update_status()
        case 5:
            update_priority()
        case 6:
            delete_task()
        case 7:
            exit()
        case 8:
            save_tasks()
