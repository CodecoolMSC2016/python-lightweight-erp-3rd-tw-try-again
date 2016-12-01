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
    title_str = "<id> <month> <day> <year> <type> <amount>"
    table = data_manager.get_table_from_file(r"hr/persons.csv")
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
        elif option == "5":
            get_oldest_person(table)
        elif option == "6":
            names=get_persons_closest_to_average(table)
            ui.print_result(names, "The people closest to the average:")
        elif option == "0":
            break
        else:
            raise KeyError("There is no such option.")

def handle_menu():
    options = ["Show Table",
               "Add",
               "Remove",
               "Update",
               "Get Oldest Person",
               "Get Person Closest To Average",]

    ui.print_menu("Human Resources", options, "Back To Main Menu")


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
    data_manager.write_table_to_file("hr/persons.csv", table)
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
    data_manager.write_table_to_file("hr/persons.csv", table)
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
    data_manager.write_table_to_file("hr/persons.csv", table)
    return table


# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):

    #min = table[0]
    #for line in table:
        #if int(line[2]) < int(min[2]):
           # min += line
    min=999999999999
    for i in range(len(table)):
        if int(table[i][2])<min:
            min=int(table[i][2])
    for i in table:
        if int(i[2]) == min:
            ui.print_result(i[1], "The oldest person is: ")



# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):

    #import csv
    #with open('persons.csv', 'r') as csvfile:
        #for lines in csvfile:
            #parts=lines.split(";")
            #average=0
            #for n in int(parts[2]):
                #pass

    result = 0
    for line in table:
        amount = line[2]
        result += int(amount)
    average=result / len(table)
    min_diff=None
    min_names=[]
    for line in table:
         diff=abs(int(line[2])-average)
         if min_diff==None or min_diff>diff:
             min_diff=diff
             min_names.clear()
             min_names.append(line[1])
         elif min_diff==None or min_diff==diff:
             min_diff=diff
             min_names.append(line[1])
    return min_names
         

                