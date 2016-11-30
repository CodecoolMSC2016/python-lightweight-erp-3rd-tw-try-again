# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# month: number
# day: number
# year: number
# type: string (in = income, out = outcome)
# amount: number (dollar)


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
    table = data_manager.get_table_from_file(r"accounting/items.csv")
    while True:
        handle_menu()
        inputs = ui.get_inputs("Please enter a number: ", "")
        option = inputs[0]
        if option == "1":
            show_table(table, title_str)
        elif option == "2":
            add(table, title_str)
        elif option == "3":
            id_ = ui.get_inputs("Enter a valid ID: ")
            remove(table, id_)
        elif option == "4":
            id_ = ui.get_inputs("Enter a valid ID: ")
            update(table, id_)
        elif option == "5":
            which_year_max(table)
        elif option == "6":
            year = ui.get_inputs("Enter a year: ")
            avg_amount(table, year)
        elif option == "0":
            break
        else:
            raise KeyError("There is no such option.")


def handle_menu():
    options = ["Show Table",
               "Add to Table",
               "Remove from Table",
               "Update Table",
               "Get max year",
               "Get avg amount"]

    ui.print_menu("Accounting", options, "Returning to Main Menu")


# print the default table of records from the file
#
# @table: list of lists
def show_table(table, title_str):
    ui.print_table(table, title_str)


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table, title_str):
    result = ui.get_inputs("Enter the records to be added (seperated by space): ", title_str)
    table.append((common.generate_random(table) + " " + result).split())
    data_manager.write_table_to_file("accounting/items.csv", table)
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    for line in table:
        if line[0] == id_:
            table.remove(line)
    data_manager.write_table_to_file("accounting/items.csv", table)
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
    data_manager.write_table_to_file("accounting/items.csv", table)
    return table


# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table):
    max = table[0]
    for line in table:
        if line[4] == 'in' and int(line[5]) > int(max[5]):
            max = line
    ui.print_result(max[3], "Year of highest profit: ")


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):
    result = 0
    amount_list = [line[5] for line in table if line[3] == year and line[4] == 'in']
    if not amount_list:
        return ui.print_result("Year not found. ")
    for amount in amount_list:
        result += int(amount)
    ui.print_result(result / len(amount_list), "Avarage profit in " + str(year))
