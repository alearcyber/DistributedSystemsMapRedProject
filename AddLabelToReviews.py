import re

import shutil
import random
import os
from os import walk

def prepend_bees_to_filename(file_path, text):
    """
    Takes a file path and prepends 'bees_' to the beginning of the file's name.
    """
    try:
        # Split the file path into directory and filename
        dir_path, filename = os.path.split(file_path)

        # Prepend 'bees_' to the filename
        new_filename = text + filename

        # Create the new file path
        new_file_path = os.path.join(dir_path, new_filename)

        # Rename the file
        os.rename(file_path, new_file_path)

        return f"File renamed to: {new_file_path}"
    except Exception as e:
        return f"Error: {str(e)}"

def copy_and_rename_file(source_path, destination_dir, new_filename):
    """
    Copies a file from source_path to destination_dir and renames it to new_filename.
    """
    try:
        # Create the full path for the new file
        destination_path = os.path.join(destination_dir, new_filename)

        # Copy and rename the file
        shutil.copy2(source_path, destination_path)

        return f"File copied and renamed to: {destination_path}"
    except Exception as e:
        return f"Error: {str(e)}"


def prepend_bees_to_lines(file_path):
    """
    Reads a file, removes all special characters (keeps only lowercase, uppercase letters, and spaces),
    then prepends the string "BEES" followed by a tab to the start of each line.
    The modified content is written back to the file.
    """
    try:
        # Read the contents of the file
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Remove all special characters and prepend "BEES\t" to each line
        modified_lines = ['POS ' + re.sub(r'[^a-zA-Z ]', '', line.lower()) for line in lines]

        # Write the modified lines back to the file
        with open(file_path, 'w') as file:
            file.writelines(modified_lines)

        return "Modification complete."
    except Exception as e:
        return f"Error: {str(e)}"


path1 = "/Users/aidanlear/Downloads/aclImdb/test/neg/1_3.txt"
#prepend_bees_to_lines(path1)



def t1():
    mypath = "/Users/aidanlear/Downloads/aclImdb/test/pos/"
    from os import walk
    filenames = next(walk(mypath), (None, None, []))[2]  # [] if no file


    for filename in filenames[:]:
        prepend_bees_to_lines(mypath + filename)



def t2():
    mypath = "/Users/aidanlear/Desktop/aclImdb/test/neg/"
    filenames = next(walk(mypath), (None, None, []))[2]  # [] if no file
    filenames = filenames[:]
    random.shuffle(filenames)



    #iterates over files in a directory
    for filename in filenames[:1000]:
        copy_and_rename_file(mypath + filename, "/Users/aidanlear/Desktop/aclImdb/test/AllReviews/", 'neg_' + filename)
