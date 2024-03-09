"""
 * @Author: Douglas Kitagawa <dkitagawa>
 *
 * @Date: 03-10-2024
 *
 * @File: whitespace-warrior.py
 *
 * @Brief: A function developed to find whitespace characters and replace them with underscores.
 *
 * @Last modified by: dkitagawa
 *
 * @Last modified time: 03-10-2024
 *
 * @return str: The modified string.
 *
 * @args string: The input string to be modified.
"""

def whitespace_warrior(input_string):
    modified_string = ""
    for string_character in input_string:
        if string_character.isspace():
            modified_string += '_'
        else:
            modified_string += string_character
    return modified_string

# How to use it
input_string = input("Enter your string: ")
finalString = whitespace_warrior(input_string)
print("Here's your modified string: ", finalString)
