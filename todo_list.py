print("Test")

def menu(): 
    mode = input("""1. Add item to your to do list, 2. Review your to do list, 3. Exit""")
    return mode

def item_add():
    while True:
        task_input = input("Enter a task or type end: ").strip() 
        if task_input == "end":
            break
        else:
            todo_list.append(task_input)

def review():
    for task in todo_list:
        print("-{}".format(task))

todo_list = []

while True:
    user_input = menu()
    if user_input == 1:
        item_add() 
    elif user_input == 2:
        review() 
    elif user_input == 3:
        break
    else: 
        print("Please enter item for your to do list or type end")
        
menu()
   
