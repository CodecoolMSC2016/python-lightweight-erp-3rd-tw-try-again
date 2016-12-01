# This function needs to print outputs like this:
# /-----------------------------------\
# |   id   |      title     |  type   |
# |--------|----------------|---------|
# |   0    | Counter strike |    fps  |
# |--------|----------------|---------|
# |   1    |       fo       |    fps  |
# \-----------------------------------/
#
# @table: list of lists - the table to print out
# @title_list: list of strings - the head of the table


def print_table(table, title_list):
    padding_length = {}
    max = 0
    print(title_list)
    table.append(title_list.split())
    table[-1], table[0] = table[0], table[-1]
    for column_index in range(len(table[0])):
        for line in table:
            if len(line[column_index]) > max:
                max = len(line[column_index])
        padding_length[column_index] = max
        max = 0
    length_list = [padding_length[key] for key in padding_length]
    line_length = len(table[0]) + len(table[0]) - 1
    for length in length_list:
        line_length += length

    print("/" + "-" * line_length + "\\")
    print("|" + "-" * line_length + "|")
    for line in table:
        for data_index in range(len(line)):
            print("|" + line[data_index].rjust(padding_length[data_index] + 1), end='')
        print("|")
        print("|" + "-" * line_length + "|")
    print("\\" + "-" * line_length + "/")


# This function needs to print result of the special functions
#
# @result: string or list or dictionary - result of the special function
# @label: string - label of the result
def print_result(result, label=""):
    if label:
        print(label + ": ", end="")
    print(result)


# This function needs to generate outputs like this:
# Main menu:
# (1) Store manager
# (2) Human resources manager
# (3) Inventory manager
# (4) Accounting manager
# (5) Selling manager
# (6) Customer relationship management (CRM)
# (0) Exit program
#
# @title: string - title of the menu
# @list_options: list of strings - the options in the menu
# @exit_message: string - the last option with (0) (example: "Back to main menu")
def print_menu(title, list_options, exit_message):
    print(title)
    for option_index in range(len(list_options)):
        print("({}) {}" .format(option_index + 1, list_options[option_index]))
    print("(0) {}" .format(exit_message))


# This function gets a list of inputs from the user by the terminal
#
# @list_labels: list of strings - the labels of the inputs
# @title: string - title of the "input section"
# @inputs: list of string - list of the received values from the user
def get_inputs(list_labels='', title=''):
    print(title)
    print("".join(list_labels))
    return input()


# This function needs to print an error message. (example: Error: @message)
#
# @message: string - the error message
def print_error_message(message):
    print(message)
