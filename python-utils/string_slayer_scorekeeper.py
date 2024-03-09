"""
 * @Author: Douglas Kitagawa <dkitagawa>
 *
 * @Date: 02-22-2024
 *
 * @File: string_slayer_scorekeeper.py
 *
 * @Brief: A function to count the total number of strings entered by the user.
 *
 * @Last modified by: dkitagawa
 *
 * @Last modified time: 02-22-2024
 *
 * @return int: Total number of strings entered.
"""

def string_slayer_scorekeeper():

    string_list = [] # Creates a list to store the entered strings

    # Continue receiving input from the user until an empty string is entered
    while True:
        print("Welcome to the string counter system!\n\n")
        string_input = input("Please type your sentence [PRESS ENTER TO FINISH]: ").strip() # Using the strip() function to remove extra whitespaces characters.
        # If the entered string match a character
        if string_input:
            string_list.append(string_input)  # Then add the string to the list
        # If the entered string a whitespace
        else:
            break  # Exit the loop

    return len(string_input)  # Using len() function to return the number of items in the list

# How to use it
count_user_str = string_slayer_scorekeeper()
print("Total number of characters entered:", count_user_str)
