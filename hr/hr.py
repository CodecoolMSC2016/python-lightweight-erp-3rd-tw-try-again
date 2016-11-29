# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


# importing everything you need
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader("data_manager", current_file_path + "/../data_manager.py").load_module()
# common module
common = SourceFileLoader("common", current_file_path + "/../common.py").load_module()


# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu
#
def start_module():

    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        choose.start_module()
    elif option == "2":
        show_table.start_module()
    elif option == "3":
        add.start_module()
    elif option == "4":
        remove.start_module()
    elif option == "5":
        update.start_module()
    elif option == "6":
        get_oldest_person.start_module()
    elif option == "6":
        get_persons_closest_to_average.start_module()
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")

def handle_menu():
    options = ["Show Table",
               "Add",
               "Remove",
               "Update",
               "Get Oldest Person",
               "Get Person Closest To Average",]

    ui.print_menu("Main menu", options, "Exit program")


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):

    from ui import print_table

    pass


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    x = input("Give me what you want to add: ")
    append.table(x)

    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    y = input("Give me what you want to remove: ")
    remove.table(y)

    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):

    # your code

    return table


# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):

    # your code

    pass


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):

    # your code

    pass
