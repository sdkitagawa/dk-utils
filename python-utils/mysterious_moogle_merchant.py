"""
 * @Author: Douglas Kitagawa <dkitagawa>
 *
 * @Date: 05-22-2024
 *
 * @File: mysterious_moogle_merchant.py
 *
 * @Brief: A function developed to count characters (including spaces).
 *
 * @Last modified by: dkitagawa
 *
 * @Last modified time: 05-22-2024
 *
 * @return str: The length of a string.
 *
 * @args string: The input string that will be counted.
"""

def mysterious_moogle_merchant(moogle_medal):
    # Using len() function to read length of the list and return the number of items in this function
    return len(moogle_medal)

# How to use it
input_string = input("Please insert your Moogle Medals: ")
output_string = mysterious_moogle_merchant(input_string)
print(f"You have {output_string} Moogle Medals here!")
