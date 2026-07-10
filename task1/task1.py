# Task 1: File Handling and Automation

import os

try:
    # Create and write to a text file
    with open("sample.txt", "w") as file:
        file.write("Hello Alfido Tech Internship!")

    # Read the file
    with open("sample.txt", "r") as file:
        content = file.read()
        print("File Content:", content)

    # Rename the file
    os.rename("sample.txt", "renamed_sample.txt")

    # Move the file to a new folder
    os.makedirs("moved_folder", exist_ok=True)
    os.replace("renamed_sample.txt", "moved_folder/renamed_sample.txt")

    # Delete the file
    os.remove("moved_folder/renamed_sample.txt")

    print("All file operations completed successfully!")

except Exception as e:
    print("Error occurred:", e)