# my_str = "nika 11 keshelava"
# print(int(my_str[5]+my_str[6]) + int("4"))          # = 15
# print(int(my_str[5]) + int(my_str[6]) + int("4"))   #= 6


# print(my_str.count(" ")+ int("4"))   # = 6

# print(my_str.index("k"))
# print(my_str.count("k"))

# def find_index_of_chars(any_str,any_char):
#     arr_of_index = []
#     i = 0
#     while i < len(any_str):
#         if any_str[i] == any_char:
#             arr_of_index.append(i)
#         i += 1
#     print(any_char, "gvxvdeba", arr_of_index, "adgilebze")
# print(find_index_of_chars("nika keshelava paithon", "a"))
# print(find_index_of_chars("nika keshelava beta version nice", "n"))

name = "nikako"
name1 = ""
for i in range(len(name)):
    if i == 2 or i == 3:
        name1 += "mu"
    else:
        name1 += name[i]
print(name1)






























