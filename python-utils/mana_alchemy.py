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

def mana_alchemy(input_file, output_file):
    try:
        # Open the UTF-8 encoded file in binary mode
        with open(input_file, 'rb') as utf8_file:
            # Read the content as bytes
            content_bytes = utf8_file.read()

        # Decode bytes with error handling to ignore or replace invalid characters
        content = content_bytes.decode('utf-8', errors='replace')

        # Convert to Windows-1252
        windows1252_content = content.encode('windows-1252', errors='replace').decode('windows-1252')

        # Save the file
        with open(output_file, 'w', encoding='windows-1252') as windows1252_file:
            windows1252_file.write(windows1252_content)
        
        print(f"Conversion successful. File saved as '{output_file}'.")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")


# How to use it
mana_alchemy('utf8_file.txt', 'windows1252_file.txt')
