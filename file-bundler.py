#  --------------------------------------------------------------------------
#   Creation: 03/03/2022
#   Authors: J. Alex
#   
#   Running the script:
#       py file-bundler.py <SOURCE> <TARGET> <NAME>
#       
#       <SOURCE>    - Full path to directory of unorganized files.             (ex. "/path/to/dir")
#       <TARGET>    - Full path to directory where zip-archive will be placed. (ex. "/path/to/anotherdir")
#       <NAME>      - Name of zip-archive.
#
#  --------------------------------------------------------------------------

import os
import shutil
import sys

"""
    This dictionary represents the wanted file structure once the script is finished.
        Keys - Subfolders.
        Value - List of wanted files in each subfolder. Values are matched with keyword "in" (i.e values are matched fully or partially.)

    Note: Key named "root" represents the root folder (not a subfolder!)
"""
DIRECTORY_FILE_DICTIONARY = {
    "bluetooth": ["bluetooth", "ble"],
    "web": ["webrelated"],
    "root": ["rooted"],
}

PATH_TMP = "./temp"
PATH_SOURCE = ""
PATH_TARGET = ""
OUTPUT_FILENAME = ""

if len(sys.argv) > 4:
        raise ValueError("Too many arguments given!\n\t[i] - py file-bundler.py <SOURCE> <TARGET> <NAME>")

# Check if path args exist, if not prompt user to enter them.
try:
    PATH_SOURCE = sys.argv[1]
    PATH_TARGET = sys.argv[2]
    OUTPUT_FILENAME = sys.argv[3]
except:
    print("[!] - Couldn't read/find args.!")
    print("[i] - py file-bundler.py <SOURCE> <TARGET> <NAME>\n")
    print("Enter full path to files (SOURCE): ", end="")
    PATH_SOURCE = input()
    print("Enter full output path (TARGET): ", end="")
    PATH_TARGET = input()
    print("Enter output filename (NAME): ", end="")
    OUTPUT_FILENAME = input()

print(f"SOURCE: {PATH_SOURCE}")
print(f"TARGET: {PATH_TARGET}")
print(f"NAME: {OUTPUT_FILENAME}")

# Create temp directory
if not os.path.exists(PATH_TMP):
    os.mkdir(PATH_TMP)
    print(f"'{PATH_TMP}' created...")

# Create target directory if they do not exist
if not os.path.exists(PATH_TARGET):
    os.mkdir(PATH_TARGET)
    print(f"'{PATH_TARGET}' created...")

# Create directories based on dictionary
for key in DIRECTORY_FILE_DICTIONARY.keys():
    if (key == "root"):  # "root" is root, not a separate folder
        continue

    full_path_from_key_name = os.path.join(PATH_TMP, key)
    if not os.path.exists(full_path_from_key_name):
        os.mkdir(full_path_from_key_name)
        print(f"'{full_path_from_key_name}' created...")

# Perform copy on each file to target
for file in os.listdir(PATH_SOURCE):
    performed_copy = False  # Reset flag, assumes that we will not copy file
    full_path_to_target_file = os.path.join(PATH_SOURCE, file)
    for key in DIRECTORY_FILE_DICTIONARY.keys():
        for value in DIRECTORY_FILE_DICTIONARY[key]:
            if (value in file):
                target = os.path.join(PATH_TMP, key) if key != "root" else PATH_TMP
                shutil.copy(full_path_to_target_file, target)
                performed_copy = True
                print(f"copied '{file}' to {key}\t[{file} -> {key}]")
                break

    if (not performed_copy):
        print(f"\n[!] - Detected extra file '{file}'...")
        while True:
            print(f"Choose directory to place file in {DIRECTORY_FILE_DICTIONARY.keys()} or use 'skip' to skip file: ", end="")
            usrinp = input()
            allowed_input = True if usrinp in DIRECTORY_FILE_DICTIONARY.keys() else False

            if allowed_input:
                if (usrinp == "skip"):
                    print(f"\nskipped '{file}'...")
                    break
                elif (usrinp == "root"):
                    shutil.copy(full_path_to_target_file, PATH_TMP)
                    print(f"\ncopied '{file}' to {usrinp}\t[{file} -> {usrinp}]")
                    break
                else:
                    shutil.copy(full_path_to_target_file, os.path.join(PATH_TMP, usrinp))
                    print(f"\ncopied '{file}' to {usrinp}\t[{file} -> {usrinp}]")
                    break

print(f"Creating archive '{OUTPUT_FILENAME}.zip'... ", end="")
shutil.make_archive(OUTPUT_FILENAME, "zip", PATH_TMP)
print(f"Done!")

print(f"Doing some cleanup... ", end="")
shutil.rmtree(PATH_TMP)
print(f"Done!")

try:
    shutil.move(f"./{OUTPUT_FILENAME}.zip", PATH_TARGET)
    print(f"Moved '{OUTPUT_FILENAME}.zip' to {PATH_TARGET}...")
except:
    print(f"[!] - File already exist in output directory, skipped MOVE...")

print(f"We are done!")