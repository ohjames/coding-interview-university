
import readline

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (min, secs) = time_string.split(splitter)
    return(min + '.' + secs)

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        return(data.strip().split(','))
    except IOError as ioerr:
        print("File error: " + str(ioerr))
        return(None)

 
# with open("james.txt") as jaf:
#     data = jaf.readline()
# james = data.strip().split(',')
# with open("julie.txt") as juf:
#     data = juf.readline()
# julie = data.strip().split(',')
# with open("mikey.txt") as mif:
#     data = mif.readline()
# mikey = data.strip().split(',')
# with open("sarah.txt") as saf:
#     data = saf.readline()
# sarah = data.strip().split(',')

james = get_coach_data('james.txt')
julie = get_coach_data('julie.txt')
mikey = get_coach_data('mikey.txt')
sarah = get_coach_data('sarah.txt')

# clean_james = []
# clean_julie = []
# clean_mikey = []
# clean_sarah = []

# for each_t in james:
#     clean_james.append(sanitize(each_t))
# for each_t in julie:
#     clean_julie.append(sanitize(each_t))
# for each_t in mikey:
#     clean_mikey.append(sanitize(each_t))
# for each_t in sarah:
#     clean_sarah.append(sanitize(each_t))
clean_james = sorted([sanitize(t) for t in james])
clean_julie = sorted([sanitize(t) for t in julie])
clean_mikey = sorted([sanitize(t) for t in mikey])
clean_sarah = sorted([sanitize(t) for t in sarah])

print(sorted(clean_james))
print(sorted(clean_julie))
print(sorted(clean_mikey))
print(sorted(clean_sarah))


data = [6, 3, 1, 2, 4, 5]
data.sort() # Performs in-place sorting
data2 = sorted(data) # Performs copied sorting; data will have unsorted list, data2 sorted list

unique_james = []
unique_julie = []
unique_mikey = []
unique_sarah = []
for each_t in james:
    if each_t not in unique_james:
        unique_james.append(each_t)
print(unique_james[0:3])
for each_t in julie:
    if each_t not in unique_julie:
        unique_julie.append(each_t)
print(unique_julie[0:3])
for each_t in mikey:
    if each_t not in unique_mikey:
        unique_mikey.append(each_t)
print(unique_mikey[0:3])
for each_t in sarah:
    if each_t not in unique_sarah:
        unique_sarah.append(each_t)
print(unique_sarah[0:3])

print(sorted(set([sanitize(t) for t in james])) [0:3])
print(sorted(set([sanitize(t) for t in julie])) [0:3])
print(sorted(set([sanitize(t) for t in mikey])) [0:3])
print(sorted(set([sanitize(t) for t in sarah])) [0:3])