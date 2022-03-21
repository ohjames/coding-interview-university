
# Goes through a list, and if there are any nested lists, prints items individually
def print_lol(some_list):
    for item in some_list:
        if isinstance(item, list):
            print_lol(item) #recursive
        else:
            print(item)