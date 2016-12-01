# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# price: number (the actual selling price in $)
# month: number
# day: number
# year: number
# month,year and day combined gives the date the purchase was made


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
    title_list = "<id> <title> <price> <month> <day> <year>"
    table = data_manager.get_table_from_file(r"selling/sellings.csv")
    while True:
        handle_menu()
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
                show_table(table, title_list)
        elif option == "2":
            add(table, title_list)
        elif option == "3":
            id_ = ui.get_inputs("Enter a valid ID: ", "")
            remove(table, id_)
        elif option == "4":
            id_ = ui.get_inputs("Enter a valid ID: ", "")
            update(table, id_)
        elif option == "5":
            get_lowest_price_item_id(table)
        elif option == "6":
            get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to)
        elif option == "0":
            break
        else:
            raise KeyError("There is no such option.")

def handle_menu():
    options = ["Show Table",
               "Add",
               "Remove",
               "Update",
               "Get Lowest Price Item",
               "Items Sold Between",]

    ui.print_menu("Selling", options, "Back To Main Menu")


# print the default table of records from the file
#
# @table: list of lists
def show_table(table, title_list):

    ui.print_table(table, title_list)


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table, title_list):
    result = ui.get_inputs("Enter the records to be added (seperated by space): ", title_list)
    table.append((common.generate_random(table) + " " + result).split())
    data_manager.write_table_to_file("selling/sellings.csv", table)
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    for line in table:
        id_ = title_list[0]
        if line[0] == id_:
            table.remove(line)
    data_manager.write_table_to_file("selling/sellings.csv", table)
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
    data_manager.write_table_to_file("selling/sellings.csv", table)
    return table


# special functions:
# ------------------

# the question: What is the id of the item that sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first of descending alphabetical order
def get_lowest_price_item_id(table):

    min=999999999999
    for line in range(len(table)):
        if int(table[line][2])<min:
            min=int(table[line][2])
    for line in table:
        if int(line[2]) == min:
            ui.print_result(line[1], "The lowest price game is: ")


# the question: Which items are sold between two given dates ? (from_date < birth_date < to_date)
# return type: list of lists (the filtered table)
def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):

    # your code

    pass
