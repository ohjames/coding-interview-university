import sys

# Goes through a list, and if there are any nested lists, prints items individually
def print_lol(some_list, indent = False, level = 0, out = sys.stdout):
    for item in some_list:
        if isinstance(item, list):
            print_lol(item, indent, level + 1, out) #recursive
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end='', file= out)
            print(item, file= out)