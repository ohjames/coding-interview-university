from exercise1.nester import print_lol

man = []
other = []

try:
    data = open("path.txt")
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(":", 1)
            line_spoken = line_spoken.strip()
            if role == "Man":
                man.appened(line_spoken)
            elif role == "Other Man":
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError: 
    print("The data file is missing")
#Method 1
try:
    man_file = open("man_data.txt", "w")
    other_file = open("other_data.txt", "w")
    print(man, file=man_file)
    print(other, file=other_file)
except IOError as err:
    print("File error: " + str(err))
finally:
    if 'man_file' in locals():
        man_file.close()
    if 'other_file' in locals():
        other_file.close()
#Method 2 with statements included
try:
    with open("man_data.txt", "w") as man_file:
        print_lol(man, out= man_file)
    with open("other_data.txt", "w") as other_file:
        print_lol(other, out= other_file)
except IOError as err:
    print("File error: " + str(err))
#Method 3 combine with statements
try:
    with open("man_data.txt", "w") as man_file, open("other_data.txt", "w") as other_file:
        print_lol(man, out= man_file)
        print_lol(other, out= other_file)
except IOError as err:
    print("File error: " + str(err))
#Method 4 use pickle
import pickle
try:
    with open("man_data.txt", "wb") as man_file, open("other_data.txt", "wb") as other_file:
        pickle.dump(man, man_file)
        pickle.dump(other, other_file)
except IOError as err:
    print("File error: " + str(err))
except pickle.PickleError as perr:
    print("Pickling error: " + str(perr))