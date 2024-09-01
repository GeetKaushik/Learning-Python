# Write a program to fetch the info of files in a directory using built-in OS module

import os

def get_files_info(directory):
    # List all files and directories in the given directory
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file():
                info = entry.stat()
                print(f"File Name: {entry.name}")
                print(f"Size: {info.st_size} bytes")
                print(f"Last Modified: {info.st_mtime}")
                print(f"Last Accessed: {info.st_atime}")
                print(f"Creation Time: {info.st_ctime}")
                print("="*40)

# Example usage:
directory = "Chapter-1/Practice-Set-1"  # Replace with your directory path
get_files_info(directory)
