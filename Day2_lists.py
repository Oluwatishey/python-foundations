#-----------------------
# Exercise 1: Largest Number
"""
This program loops through a list and looks for the largest number
"""
#------------------------

numbers = [23, 73, 93, 13, 15, 25, 52]

biggest_num = numbers[0]

for num in numbers:
    if num > biggest_num:
        biggest_num = num

print(biggest_num)


#-----------------------
# Exercise 2: Remove duplicates
"""
This program loops through a list and removes duplicates
"""
#------------------------

numbers = [23, 73, 23, 13, 15, 73, 52]
new_number = []

for num in numbers:
    if num not in new_number:
        new_number.append(num)
        print(new_number)


# -------------------------
# Exercise 3: Word Counter
"""
This program receives input of strings from a user and counts how many words are there
"""
# -------------------------

words = str(input("Enter the word here: "))
new_words = words.split()

print(len(new_words))


# -------------------------
# Exercise 4: Word Counter
"""
This program receives a number of floats and saves them into a list then adds up all the floats in the list
"""
# -------------------------

cartlist = []

price1 = float(input("Enter the first price: "))
cartlist.append(price1)

price2 = float(input("Enter the second price: "))
cartlist.append(price2)

price3 = float(input("Enter the third price: "))
cartlist.append(price3)

price4 = float(input("Enter the fourth price: "))
cartlist.append(price4)

price5 = float(input("Enter the fifth price: "))
cartlist.append(price5)

total = 0

for i in cartlist:
    total += i

print(str(round(total)))