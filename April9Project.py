#!/usr/bin/env python3.7

import os

# Get the current working directory
cwd = os.getcwd()

# Create an empty list to store file information
file_information = []

# Go through the directory tree and get file information
for dirpath, dirnames, filenames, in os.walk(cwd):
    for file in filenames:
        file_path = os.path.join(dirpath, file)
        file_size = os.path.getsize(file_path)
        file_information.append({"name": file, "size": file_size})

# Print the list of file information
for file in file_information:
    print(file)

