my_name = "nika"
print(my_name * 3)

surname = "amrazishvili"
print(surname[0:-1])

surname = "amrazishvili"
new_s = ""
i = 1
while i < len(surname)-1: 
    new_s += surname[i]
    i += 1
print(new_s)


surname = "  amrazishvili  "
my_str = ""
for char in surname:
    if char != " ":
        my_str += char
print(my_str)

name = "nika"
name1 = ""
i = len(name)
for char in range(len(name)):
    name1 += name[i-1]
    i -= 1
print(name1)

# string = "nika"
# def solution(string):
#     str = ""
#     i = len(string)
#     while i > 0:
#         str += string[i-1]
#         i -= 1
#     return str
# print(solution(string))


# name = "nika"
# name1 = ""
# i = len(name)
# while i > 0:
#     name1 += name[i-1]
#     i -= 1
# print(name1)









