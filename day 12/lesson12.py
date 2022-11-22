# arr = ['nika', 'luka', 'giorgi', 'iva', 'farna']
# for i in range(len(arr)):
#     print(i , arr[i])

# for i, item in enumerate(arr):
#     print(i, item)


# my_str = "mamuka kargi bikia"

# print(my_str.split("k"))

def abbrev_name(name):
    name_arr = name.split()
    return name_arr[0][0].capitalize() + "." + name_arr[1][0].capitalize() #+ "." + name_arr[2][0].capitalize()

print(abbrev_name("jayi juyi"))









