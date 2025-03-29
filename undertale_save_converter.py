# Undertale Game Save Converter (For PC, Switch and PSVita)
# https://github.com/Javiergrandealo/undertale-save-converter
#Forked from: https://github.com/tomchapin/undertale-save-converter/tree/master

#############################################################################################
# Imports
#############################################################################################
import os
import sys

#############################################################################################
# Helper Methods
#############################################################################################

def clear_screen():
    """
    Clears the terminal screen.
    Compatible with Windows, macOS, and Linux.
    """
    if os.name == 'nt':  # Windows
        os.system("cls")
    else:  # macOS and Linux
        os.system("clear")


#############################################################################################
# PC to Switch/Vita
#############################################################################################

def pc_file_to_switch_text(input_file):
    """
    Converts lines in a PC file (such as file9 or file0) into a single line of text
    with line breaks formatted for Switch/Vita.
    """
    result = ''
    file_contents = input_file.read()

    # Divide the content into lines and process each one
    lines = file_contents.splitlines()
    for cnt, line in enumerate(lines):
        # Removes whitespace at the beginning and end of the line
        new_line = line.strip()

        # Add a line break "\r\n" after each line except the last one
        if cnt < len(lines) - 1:
            result += new_line + "\\r\\n"
        else:
            result += new_line  # The last line does not have "\r\n"

    return result

def pc_undertale_ini_to_switch_text(input_file):
    """
    Converts all of the PC undertale.ini file's lines to a single line of text meant for the Switch or Vita game save file
    """
    result = ''
    file_contents = input_file.read()

    for line in file_contents.splitlines():  # Divide text into lines
        new_line = line.strip()  # delete spaces from the start and end of the line

        if not new_line:  # Ignore empty lines
            continue

        if new_line.startswith("["):  # if the line starts with a bracket
            result += new_line + "\\r\\n"
        elif "=" in new_line:  # if the line is a key-value pair
            key, value = new_line.split("=", 1)  # Divide the line into key and value
            value = value.strip('"')  # delete quotes from the start and end of the value
            result += f'{key}=\\"{value}\\"\\r\\n'
        else:
            # if the line is not a key-value pair or a bracket
            continue

    # Replaze the last line ending with a space
    result = result.replace("\\r\\n[", "\\r[")

    return result

def convert_from_pc_to_switch():
    clear_screen()
    print("Converting from PC to switch/vita...")

    pc_file9 = open("file9", "r")
    pc_file0 = open("file0", "r")
    pc_undertale_ini = open("undertale.ini", "r")
    switch_undertale_sav = open("undertale.sav", "w")

    switch_undertale_sav.write('{ "default": "", "file9": "')
    switch_undertale_sav.write(pc_file_to_switch_text(pc_file9))
    switch_undertale_sav.write('", "config.ini": "", "undertale.ini": "')
    switch_undertale_sav.write(pc_undertale_ini_to_switch_text(pc_undertale_ini))
    switch_undertale_sav.write('", "file0": "')
    switch_undertale_sav.write(pc_file_to_switch_text(pc_file0))
    switch_undertale_sav.write('" }')
    switch_undertale_sav.write(chr(0))

    pc_file9.close()
    pc_undertale_ini.close()
    pc_file0.close()
    switch_undertale_sav.close()

    print("Done! Your new undertale.sav file is ready!")


#############################################################################################
# Switch/Vita to PC
#############################################################################################

def undertale_save_contents():
    switch_undertale_sav = open("undertale.sav", "r")

    # Load the single run-on line of text from the undertale.sav file
    contents = switch_undertale_sav.read()

    # Close the file handle
    switch_undertale_sav.close()

    return contents


def file9_content_from_switch_save():
    return undertale_save_contents().split('"file9": "')[1].split('", "config.ini"')[0]


def undertale_ini_content_from_switch_save():
    return undertale_save_contents().split('"undertale.ini": "')[1].split('", "file0"')[0]


def file0_content_from_switch_save():
    return undertale_save_contents().split('"file0": "')[1].split('" }')[0]


def switch_file_text_to_pc_file_lines(extracted_text):
    result = ''

    # Convert all the line endings to PC line endings
    lines = extracted_text.split("\\r\\n")

    for cnt, line in enumerate(lines):
        if cnt == 0:
            # First line doesn't have an extra space before the line ending
            result += line + "\n"
        elif cnt+1 == len(lines):
            # The last line has a space, but does not have a line ending
            result += line + " "
        else:
            # Every following line has an extra space right before the line ending
            result += line + " \n"

    return result


def switch_undertale_ini_to_pc_file_lines(extracted_text):
    return extracted_text.replace('\\r\\n', "\n").replace('\\r', "\n").replace('\\"', '"')


def convert_from_switch_to_pc():
    clear_screen()
    print("Converting from Switch/Vita to PC...")

    pc_file9 = open("file9", "w")
    pc_file9.write(switch_file_text_to_pc_file_lines(file9_content_from_switch_save()))
    pc_file9.close()

    pc_file0 = open("file0", "w")
    pc_file0.write(switch_file_text_to_pc_file_lines(file0_content_from_switch_save()))
    pc_file0.close()

    pc_undertale_ini = open("undertale.ini", "w")
    pc_undertale_ini.write(switch_undertale_ini_to_pc_file_lines(undertale_ini_content_from_switch_save()))
    pc_undertale_ini.close()

    print("Done! Your new PC game save files are ready!")


#############################################################################################
# Menu
#############################################################################################

def display_menu():
    clear_screen()
    print("")
    print("  -------------------------------------")
    print("  Undertale PC/Switch/Vita Save Converter")
    print("  -------------------------------------")
    print("")
    print("  1. Convert from PC to Switch/Vita")
    print("     Make sure you have copied your game's file0, file9, and undertale.ini files to this folder.")
    print("     (These files are typically located in your system's %LocalAppData%\\UNDERTALE\\ folder)")
    print("")
    print("  2. Convert from Switch/Vita to PC")
    print("     Make sure you have the undertale.sav file copied from your Nintendo Switch or PSVita.")
    print("")
    print("  Press (1) or (2) to select a menu option, or type 'exit' to quit:")

    user_input = input("Your choice: ").strip().lower()
    if user_input == '1':
        # 1 was selected
        convert_from_pc_to_switch()
    elif user_input == '2':
        # 2 was selected
        convert_from_switch_to_pc()
    elif user_input == 'exit':
        # Exit the program
        return
    else:
        # Invalid input, redisplay the menu
        print("Invalid input. Please try again.")
        input("Press Enter to continue...")
        display_menu()


if __name__ == '__main__':
    display_menu()