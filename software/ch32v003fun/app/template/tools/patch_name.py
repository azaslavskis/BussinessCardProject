import easygui
import os

def replace_string_in_binary(file_path, target_str, replacement_str):
    """
    Replaces occurrences of target_str with replacement_str in a binary file.

    :param file_path: Path to the binary file.
    :param target_str: The string to search for in the file.
    :param replacement_str: The string to replace target_str with.
    """
    if len(target_str) != len(replacement_str):
        easygui.msgbox("Target and replacement strings must be of the same length.", title="Error")
        return

    target_bytes = target_str.encode('utf-8')
    replacement_bytes = replacement_str.encode('utf-8')

    try:
        with open(file_path, 'rb') as file:
            binary_data = file.read()

        modified_data = binary_data.replace(target_bytes, replacement_bytes)

        with open(file_path, 'wb') as file:
            file.write(modified_data)

        easygui.msgbox(f"Replaced '{target_str}' with '{replacement_str}' in {file_path}", title="Success")

    except FileNotFoundError:
        easygui.msgbox(f"File not found: {file_path}", title="Error")
    except Exception as e:
        easygui.msgbox(f"An error occurred: {e}", title="Error")







# Main script to interact with user
file_path = easygui.fileopenbox(title="Select a binary file to modify")
if file_path:
    target_str = easygui.enterbox("Enter the target string to find in the file:", title="Target String")
    replacement_str = easygui.enterbox("Enter the replacement string:", title="Replacement String")

    if target_str and replacement_str:
        replace_string_in_binary(file_path, target_str, replacement_str)
    else:
        easygui.msgbox("Target and replacement strings cannot be empty.", title="Error")
else:
    easygui.msgbox("No file selected.", title="Error")


