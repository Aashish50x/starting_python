# Write a python program to print the contents of a directory using the os module.

import os

# Specify the directory you want to list
directory_path = '/'
# calling main directory by "/" operator

# List all files and directories in the specified path
contents = os.listdir(directory_path)

# Print each file and directory name
for item in contents:
    print(item)