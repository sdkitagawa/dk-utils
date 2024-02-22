"""
 * @Author: Douglas Kitagawa <dkitagawa>
 *
 * @Date: 02-22-2024
 *
 * @File: string_counter.py
 *
 * @Brief: A function to count the total number of strings entered by the user.
 *
 * @Last modified by: dkitagawa
 *
 * @Last modified time: 02-22-2024
 *
 * @return int: Total number of strings entered.
"""

def string_counter():

    stringList = [] # Creates a list to store the entered strings

    # Continue receiving input from the user until an empty string is entered
    while True:
        print("Welcome to the string counter system!\n\n")
        stringInput = input("Please type your sentence [PRESS ENTER TO FINISH]: ").strip() # Using the strip() function to remove extra whitespaces characters.
        # If the entered string match a character
        if stringInput:
            stringList.append(stringInput)  # Then add the string to the list
        # If the entered string a whitespace
        else:
            break  # Exit the loop

    return len(stringInput)  # Using len() function to return the number of items in the list

# How to use it
countUserStr = string_counter()
print("Total number of characters entered:", countUserStr)
