"""
 * @Author: Douglas Kitagawa <dkitagawa>
 *
 * @Date: 02-22-2024
 *
 * @File: string_slayer_scorekeeper_space_edition.py
 *
 * @Brief: A function to count the total number of strings entered by the user (including spaces).
 *
 * @Last modified by: dkitagawa
 *
 * @Last modified time: 02-22-2024
 *
 * @return int: Total number of strings entered.
 *
 * @args string: The input string to count the characters.
"""

def string_slayer_scorekeeper(string):
    # Using len() function to read length of the list and return the number of items in this function
    return len(string)

# How to use it
count_user_str = str(input("Please type your sentence: "))
total_num_characters = string_slayer_scorekeeper(count_user_str)
print("Total number of characters entered (including spaces):", total_num_characters)
