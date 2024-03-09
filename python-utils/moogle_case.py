"""
 * @Author: Douglas Kitagawa <dkitagawa>
 *
 * @Date: 03-10-2024
 *
 * @File: string_slayer_scorekeeper_space_edition.py
 *
 * @Brief: A function to quickly lowercase characters.
 *
 * @Last modified by: dkitagawa
 *
 * @Last modified time: 03-10-2024
 *
 * @return str: The lowered string.
 *
 * @args string: The input string to be lowered.
"""

def moogle_case(string_input):
    return string_input.lower()

# How to use it
user_string = input("Enter your string: ")
lowercased_string = moogle_case(user_string)
print(lowercased_string)
