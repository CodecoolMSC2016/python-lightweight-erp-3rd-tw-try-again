# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# manufacturer: string
# purchase_date: number (year)
# durability: number (year)


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
    title_str = "<id> <month> <day> <year> <type> <amount>"
    table = data_manager.get_table_from_file(r"tool_manager/tools.csv")
    while True:
        handle_menu()   
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
                show_table(table, title_str)
        elif option == "2":
            add(table, title_str)
        elif option == "3":
            id_ = ui.get_inputs("Enter a valid ID: ", "")
            remove(table, id_)
        elif option == "4":
            id_ = ui.get_inputs("Enter a valid ID: ", "")
            update(table, id_)
        elif option == "6":
            get_available_tools(table)
        elif option == "6":
            get_average_durability_by_manufacturers(table)
        elif option == "0":
            break
        else:
            raise KeyError("There is no such option.")

def handle_menu():
    options = ["Show Table",
               "Add",
               "Remove",
               "Update",
               "Get Available Tools",
               "Get Average Durability",]

    ui.print_menu("Tool Manager", options, "Back To Main Menu")


# print the default table of records from the file
#
# @table: list of lists
def show_table(table,title_str):

    ui.print_table(table, title_str)


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table, title_str):
    result = ui.get_inputs("Enter the records to be added (seperated by space): ", title_str)
    table.append((common.generate_random(table) + " " + result).split())
    data_manager.write_table_to_file("tool_manager/tools.csv", table)
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    for line in table:
        id_ = title_str[0]
        if line[0] == id_:
            table.remove(line)
    data_manager.write_table_to_file("tool_manager/tools.csv", table)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):
    for line_index in range(len(table)):
        if table[line_index][0] == id_:
            new_datas = ui.get_inputs("Enter new data(seperated by space): ").split()
            table[line_index] = [id_]
            for data in new_datas:
                table[line_index].append(data)
    data_manager.write_table_to_file("tool_manager/tools.csv", table)
    return table


# special functions:
# ------------------

# the question: Which items has not yet exceeded their durability ?
# return type: list of lists (the inner list contains the whole row with their actual data types)
#
# @table: list of lists
def get_available_tools(table):

    # your code

    pass


# the question: What are the average durability time for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
#
# @table: list of lists
def get_average_durability_by_manufacturers(table):

    # your code

    pass
