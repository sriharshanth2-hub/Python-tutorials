import os
file_path = "practice.txt"
if os.path.exists(file_path) :
    print(f"The location '{file_path}' exists")
if os.path.isfile(file_path) :
    print("That is a file")
else :
    print("file doesnt exist")