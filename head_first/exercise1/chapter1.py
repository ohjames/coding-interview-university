movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, 
    ["Graham Chapman", ["Michael Palin", "John Cleese", 
    "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

# for item in movies:
#     if isinstance(item, list):
#         for nested_item in item:
#             if isinstance(nested_item, list):
#                 for double_nested in nested_item:
#                     print(double_nested)
#             else:
#                 print(nested_item)            
#     else:
#         print(item)

import exercise2

exercise2.print_lol(movies)