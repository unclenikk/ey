


# print(5, "nika", 6)


# my_arr = ["banana", 11, True, 10.5, [1,2,3], 5, 10]

# კვადრატული ფრჩხილით შექმნილი კოლექცია არის list


# print(my_arr[-1])
# print(my_arr[3])
# print(my_arr[1:4: 2])
# print(my_arr[:4])



# menu = ["xinkali", "mwvaedi", "lobiani", "qababi", "khachapuri", "wyali",]
# if "lobiani" in menu:
#     print("lobiani gvaqvs")

# menu[1] = "BBQ"
# print(menu)


# menu[2:4] = ["aa", "bb", "cc"]
# print(menu)


# my_name = "nikusha"


# new_name = ""

# for i in range (len(my_name)):
#     if i == 2 or i ==3:
#         new_name += "x"
#     else:
#         new_name += my_name[i]

# print(new_name)

# print(my_name.replace("ku", "qq"))


# my_str = "qwqfnugqeguioqgqegqegedgkkkkkfqefqeg"
# new_str = ""

# for char in my_str:
#     if char == "k":
#         new_str += "#"
#     else:
#         new_str += char

# print(new_str)



# menu = ["xinkali", "mwvaedi", "lobiani", "qababi", "khachapuri", "wyali",]
# # menu.insert(3, "nayini")
# # print(menu)

# menu.append("cecxli")
# menu.append("navti")
# print(menu)



# menu = []
# menu.append("Pizza")
# print(menu)



# menu = []
# for i in range(3):
#     food = input("enter a food: ")
#     ammount_of_a = 0
#     for char in food:
#         if char == "a":
#             ammount_of_a += 1
#     if ammount_of_a >= 1:
#         menu.append(food)
#         ammount_of_a = 0
 
# print(menu)




# menu = ["xinkali", "mwvaedi", "lobiani", "qababi", "xachapuri", "wyali",]
# menu.remove("wyali")
# print(menu)

# new_menu = []


# for food in menu:
#     if food[1] != "a":
#        new_menu.append(food)

# print(new_menu)


# scores = [20, 43, 56, 73, 10, 6, 87, 45, 97]
# scores.sort()    #- ზრდის მიხედვით

# print(scores)



# students = ["nika", "ana", "mamuka", "beqa", "dachi", "iva", "ferna"]
# students.sort()
# print(students)


# students = ["nika", "ana", "mamuka", "beqa", "dachi", "iva", "ferna"]
# students.sort(reverse=True)
# print(students)


scores = [20, 43, 56, 73, 10, 6, 87, 45, 97]

max_num = scores[0]

for score in scores:
    if score > max_num:
        max_num = score
print(max_num)


i = 0

while i < len(scores):
    if scores[i] > max_num:
        max_num = scores[i]
    i += 1
print(max_num)


name = "nikax"
scores = [20, 43, 56, 73, 10]

i = 0
while i < (len(name)):
    print(name[i] + str(scores[i]))
    i += 1




students = ["nika", "ana", "mamuka", "beqa", "dachi", "iva", "ferna"]

new_arr = []
i = len(students)
while i > 0:
    new_arr.append(students[i-1])
    i -= 1
print(new_arr)




my_str = "nika 11 keshelava"












