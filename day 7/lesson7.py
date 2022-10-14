# my_list = ["xinkali", "mwvaedi", "lobiani", "qababi", "khachapuri", "wyali",]
# price = [2, 20, 15, 10, 15, 2]


# print(len(my_list))
# print(len(price))

# i = 0
# while i < len(my_list):
#     print(my_list[i] + " ღირს " + str(price[i]) + "ლარი")
#     i += 1


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



menu = []
for i in range(3):
    food = input("enter a food: ")
    ammount_of_a = 0
    for char in food:
        if char == "a":
            count += 1
    if count >= 2:
        menu.append(food)


print(menu)





