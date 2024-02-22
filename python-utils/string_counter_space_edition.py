"""
 * @Author: Douglas Kitagawa <dkitagawa>
 *
 * @Date: 02-22-2024
 *
 * @File: string_counter_space_edition.py
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

def string_counter(string):
    # Using len() function to read length of the list and return the number of items in this function
    return len(string)

# How to use it
countUserStr = str(input("Please type your sentence: "))
totalNumChar = string_counter(countUserStr)
print("Total number of characters entered (including spaces):", totalNumChar)
