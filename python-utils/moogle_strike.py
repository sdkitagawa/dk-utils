"""
 * @Author: Douglas Kitagawa <dkitagawa>
 *
 * @Date: 03-10-2024
 *
 * @File: moogle_strike.py
 *
 * @Brief: A function developed to find whitespace characters, replace them with underscores and lowercase characters.
 *
 * @Last modified by: dkitagawa
 *
 * @Last modified time: 03-10-2024
 *
 * @return str: The modified and lowered string.
 *
 * @args string: The input string to be modified and lowered.
"""

def moogle_strike(input_string):
    modified_string = ""
    for string_character in input_string:
        if string_character.isspace():
            modified_string += '_'
        else:
            modified_string += string_character
    return modified_string.lower()

# How to use it
input_string = input("Enter your string: ")
output_string = moogle_strike(input_string)
print("Here's your modified string: ", output_string)
