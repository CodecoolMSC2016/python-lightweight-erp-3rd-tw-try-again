# implement commonly used functions here

import random


# generate and return a unique and random string
# other expectation:
# - at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of list
# @generated: string - generated random string (unique in the @table)
def generate_random(table):
    while True:
        lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        specialchar = ['+', '!', '%', '/', '=', '$', 'ß', '×', '¤', '~', '-', '_']
        pickedchars = []
        randomized = []
        pickedchars.append(random.sample(set(lowercase), 2))
        pickedchars.append(random.sample(set(uppercase), 2))
        pickedchars.append(random.sample(set(number), 2))
        pickedchars.append(random.sample(set(specialchar), 2))
        for items in pickedchars:
            for chars in items:
                randomized.append(chars)
                result = "" .join(set(randomized))
        for elements in table:
            if elements[0] == result:
                break
            else:
                return result



   

