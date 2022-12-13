# arr = ['nika', 'luka', 'giorgi', 'iva', 'farna']
# i = 0
# for element in arr:
#     print(i , element)
#     i += 1

# arr = ['nika', 'luka', 'giorgi', 'iva', 'farna']
# for i in range(1,len(arr)+1):
#     print(i,arr[i-1])


# for i, item in enumerate(arr):
#     print(i, item)


# my_str = "mamuka kargi bikia"

# print(my_str.split("k"))

def abbrev_name(name):
    name_arr = name.split()
    return name_arr[0][0].capitalize() + "." + name_arr[1][0].capitalize() #+ "." + name_arr[2][0].capitalize()

print(abbrev_name("jayi juyi"))







