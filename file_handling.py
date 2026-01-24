# File Handling Basics in Python
# This program shows how to write to a file and read from it

# -------- WRITE TO A FILE --------
file = open("sample.txt", "w")   # open file in write mode
file.write("Hello, this is my first file handling program in Python.\n")
file.write("I am learning Python step by step.")
file.close()                     # always close the file

print("Data written to file successfully.\n")


# -------- READ FROM A FILE --------
file = open("sample.txt", "r")   # open file in read mode
content = file.read()            # read entire file content
file.close()

print("Reading data from file:")
print(content)
