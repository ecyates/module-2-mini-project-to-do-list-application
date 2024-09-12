def add_task(task):
    '''This function takes a task and adds it to the to-do list. Tasks must be unique.'''
    
    # First check if the task is already in the to-do list
    proceed = True
    for t in to_do_list:
        if t[0] == task:
            proceed = False
    # If it's a unique task
    if proceed:
        to_do_list.insert(0, [task, "Incomplete", 8]) # Adds the task to the top of the list, with default color
        print(f"\nThe task '{task}' was added to the to-do list.") # Informs the user
    else: 
        print(f"\nThe task '{task}' already exists in the to-do list, please input a unique task.") # Informs the user if the task is not unique
    back_to_menu() # Back to the main menu

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
            print(f"\033[3{t[2]}m{prefix} {t[0]}\033[0m") # Use the color as provided in third position
    back_to_menu()  # Back to main menu   

def task_complete(task):
    '''This function changes the status of the task from 'Incomplete' to 'Complete' and moves the task 
    to the bottom of the list, so 'Incomplete' tasks are together and 'Complete' tasks are together.'''
    try:
        for t in to_do_list:
            if t[0] == task:
                t[1] = 'Complete' # Set the task as complete
                to_do_list.remove(t) # Removes the original task
                to_do_list.append(t) # Add the task back at the end
        print(f"\nThe task '{task}' was marked complete.") # Informs the user
    # If the user gives a task that's not on our list, informs user
    except ValueError:
        print(f"\nOops, looks like task '{task}' is not on our to-do list. Please select (1) to add the task and then (3) to mark it complete.")
        menu()
    else:
        back_to_menu() # Back to main menu

def delete_task(task):
    '''This function deletes the given task.'''
    try:
        list_check = False
        # Check that task is in the 
        for t in to_do_list:
            if t[0] == task:
                to_do_list.remove(t)
                list_check = True
                print(f"\nThe task '{task}' was removed from the to-do list.") # Informs the user
        if list_check == False:
            raise ValueError()
    # If the user gives a task that's not on our list, informs user
    except ValueError:
        print(f"\nOops, the task '{task}' cannot be found in the to-do list. Try again!")
        menu() # Back to main menu
    else: 
        back_to_menu() # Back to main menu

def color_task(task):
    try:
        color = int(input(
'''
Please choose a color:

1 - Red
2 - Green
3 - Yellow
4 - Blue
5 - Pink
6 - Turquoise
7 - Light Gray
8 - Default Black

'''
        ))
        if color > 8 or color <1: 
            raise ValueError()
        list_check = False
        for t in to_do_list:
            if t[0] == task:
                t[2] = color
                print(f"\033[3{color}m\nThe color of task '{task}' has been changed.\033[0m")
                list_check = True
        if list_check == False:
            raise ValueError()
    except ValueError:
        print("\nOops, you either input an invalid task or color (1-8). Please try again.")
        menu()
    else: 
        back_to_menu()

def back_to_menu():
    '''This function acts as a go-between from each action to the main menu. It allows the user to just type their next action
    if they have them memorized or to return to the main menu if they need to see the options again.'''
    try:
        # The user can hit any key and then 'enter' to return to the main menu or choose one of the menu items (1-5)
        next_move = int(input(f"\nTo return to main menu, hit any key and 'enter', or choose your next menu item: (1-6).\n\n"))
        # If they choose 1-5, take action
        if next_move <=6 and next_move > 0:
            take_action(next_move)
        # Otherwise, let's go back to the main menu
        else: 
            menu()
    # If the user doesn't choose an int, go back to the main menu
    except ValueError:
        menu()

def take_action(menu_item):
    '''This function takes the chosen action, prompts any necessary parameters, and runs the corresponding function.'''
    
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
    # If the user selects 5, prompt what task they'd like to delete and run that function
    elif menu_item == 5:
        color_task(input("\nWhat task would you like to color?\n\n"))
    # If the user selects 6, thank them and exit
    else:
        print("\nThank you for using the To-Do List App and have a productive day!\nGood bye!\n")

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
5 - Color a task
6 - Quit

'''
        ))
        # If the user inputs a number that's too high or low, raise error
        if menu_item > 6 or menu_item < 1: 
            raise ValueError()
    # If the user inputs a word, let them know and run menu again
    except ValueError:
        print("\nPlease try again and input a number between 1 and 6.")
        menu()
    else:
        take_action(menu_item)

# The app starts here
to_do_list = [] # Creates the to-do list
print('\nWelcome to the To-Do List App!\n') # Sends welcome message
menu() # Shows menu options & runs based on input