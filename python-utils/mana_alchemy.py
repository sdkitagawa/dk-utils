"""
 * @Author: Douglas Kitagawa <dkitagawa>
 *
 * @Date: 04-30-2024
 *
 * @File: mana_alchemy.py
 *
 * @Brief: A function to convert UTF-8 characters into Windows 1252 (Western) characters.
 *
 * @Last modified by: dkitagawa
 *
 * @Last modified time: 04-30-2024
 *
 * @args file: The files to be converted.
"""

import chardet

def mana_alchemy(input_file, output_file):
    try:
        # Detect the encoding of the input file
        with open(input_file, 'rb') as file:
            rawdata = file.read()
            detected_encoding = chardet.detect(rawdata)['encoding']
        
        # Open the input file using the detected encoding
        with open(input_file, 'r', encoding=detected_encoding) as file:
            content = file.read()

        # Convert the content to (Western) Windows-1252 encoding
        windows1252_content = content.encode('windows-1252', errors='ignore').decode('windows-1252')

        # Save the converted content to the output file
        with open(output_file, 'w', encoding='windows-1252') as file:
            file.write(windows1252_content)
        
        print(f"Conversion successful. Output file saved as '{output_file}'.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# How to use it
mana_alchemy('utf8_file.txt', 'windows1252_file.txt')
