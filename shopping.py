lists_dict = {}

def user_input():
    answer = raw_input("")
    return answer

def show_lists():
    print lists_dict

def show_specific():
    print "What list do you want to show?"
    reveal = user_input()
    print lists_dict[reveal]

def add_list():
    print "Where are you going shopping?"
    key = user_input()
    lists_dict[key] = []

def add_item():
    print "What list do you want to add to:", lists_dict
    key = user_input()
    print "What do you want to add to this list?"
    value = user_input()
    lists_dict[key].append(value)
    print lists_dict

def remove_item():
    print "What list do you want to edit?", lists_dict
    edit = user_input()
    print lists_dict[edit]
    print "What would you like to remove?"
    item = user_input()
    if item in edit:
        edit.remove(item)
    print lists_dict[edit]

def print_menu():
    print """
0 - Main Menu
1 - Show all lists.
2 - Show a specific list.
3 - Add a new shopping list.
4 - Add an item to a shopping list.
5 - Remove an item from a shopping list.
6 - Remove a list by nickname.
7 - Exit when you are done.
"""

def menu():
    while True:
        choice = user_input()
        if choice == "0":
            print_menu()
        elif choice == "1":
            show_lists()
        elif choice == "2":
            show_specific()
        elif choice == "3":
            add_list()
        elif choice == "4":
            add_item()
        elif choice == "5":
            remove_item()
        elif choice == "6":
            remove_list()
        elif choice == "7":
            exit()
        else:
            print "Please select 0-7"
         


print_menu()
menu()
