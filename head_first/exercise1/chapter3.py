# Method 1: Extra logic
import os

if os.path.exists("path.txt"):
    data = open("path.txt")

    for each_line in data:
        if not each_line.find(":") == -1:
            (role, line_spoken) = each_line.split(":", 1)
            print(role, end='')
            print(' said ', end='')
            print(line_spoken, end='')

    data.close()
else:
    print("The data file is missing")

# Method 2: Exception handling
try:
    data = open("path.txt")

    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(":", 1)
            print(role, end='')
            print(' said ', end='')
            print(line_spoken, end='')
        except ValueError:
            pass

    data.close()
except IOError: 
    print("The data file is missing")