def add_task(task):
    '''This function takes a task and adds it to the to-do list. Tasks must be unique.'''
    
    if [task, "Incomplete"] not in to_do_list and [task, "Complete"] not in to_do_list:
        to_do_list.insert(0, [task, "Incomplete"]) # Adds the task to the top of the list
        print(f"\nThe task '{task}' was added to the to-do list.") # Informs the user
    else: 
        print(f"\nThe task '{task}' already exists in the to-do list, please input a unique task.") # Informs the user if the task is not unique
    menu() # Back to the main menu

def view_tasks():
    '''This function displays the to-do list in a bulleted list form, 
    where [ ] means the task is incomplete and [X] means the task is complete.'''
    
    # If the to-do list is empty, informs the user and brings them back to main menu
    if to_do_list == []:
        print("\nThe to-do list is currently empty. Please select (1) to add tasks.")
    else:
        print("\nTo-Do List:\n")
        # Iterates over the to-do list and adds the appropriate [ ] or [X] at the beginning of each line
        for t in to_do_list:
            prefix = "[ ]"
            if t[1] == "Complete":
                prefix = "[X]"
            print(prefix, t[0])
    menu()  # Back to main menu   

def task_complete(task):
    '''This function changes the status of the task from 'Incomplete' to 'Complete' and moves the task 
    to the bottom of the list, so 'Incomplete' tasks are together and 'Complete' tasks are together.'''
    try:
        to_do_list.remove([task, 'Incomplete']) # Removes the original task
        to_do_list.append([task, 'Complete']) # Adds the task at the end with the 'Complete' status
        print(f"\nThe task '{task}' was marked complete.") # Informs the user
    # If the user gives a task that's not on our list, informs user
    except ValueError:
        print(f"\nOops, looks like task '{task}' is not on our to-do list. Please select (1) to add the task and then (3) to mark it complete.")
    finally:
        menu() # Back to main menu

def delete_task(task):
    '''This function deletes the given task.'''
    try:
        # Task status may be 'Incomplete' or 'Complete', so we run that check
        status = 'Incomplete'
        if [task, 'Complete'] in to_do_list:
            status = 'Complete'
        to_do_list.remove([task, status]) # Removes the task
        print(f"\nThe task '{task}' was removed from the to-do list.") # Informs the user
    # If the user gives a task that's not on our list, informs user
    except ValueError:
        print(f"\nOops, the task '{task}' cannot be found in the to-do list. Try again!")
    finally: 
        menu() # Back to main menu

def menu():
    ''' This function shows the main menu options and then 
    runs the option as selected by the user.'''

    try: 
        # Present the menu options to the user
        menu_item = int(input(
'''
Menu:

1 - Add a task
2 - View tasks
3 - Mark a task as complete
4 - Delete a task
5 - Quit

'''
        ))
        # If the user inputs a number that's too high or low, raise error
        if menu_item > 5 or menu_item < 1: 
            raise ValueError()
    # If the user inputs a word, let them know and run menu again
    except ValueError:
        print("\nPlease try again and input a number between 1 and 5.")
        menu()
    else:
        # If the user selects 1, prompt what task they'd like to add and run that function.
        if menu_item == 1:
            add_task(input("\nWhat task would you like to add?\n\n"))
        # If th user selects 2, run the function to view all tasks.
        elif menu_item == 2:
            view_tasks()
        # If the user selects 3, prompt what task they'd like to mark complete and run that function
        elif menu_item == 3:
            task_complete(input("\nWhat task would you like to mark complete?\n\n"))
        # If the user selects 4, prompt what task they'd like to delete and run that function
        elif menu_item == 4:
            delete_task(input("\nWhat task would you like to delete?\n\n"))
        # If the user selects 5, thank them and exit
        else:
            print("\nThank you for using the To-Do List App and have a productive day!\nGood bye!\n")

# The app starts here
to_do_list = [] # Creates the to-do list
print('\nWelcome to the To-Do List App!\n') # Sends welcome message
menu() # Shows menu options & runs based on input