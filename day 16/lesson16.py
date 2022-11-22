# print(int(str(34.0//3)[:-2]))

# print(int(6//2.0))







# import random
# num1 = random.randint(5, 23)
# num2 = random.randrange(44)

# print(num1)
# print(num2)

# stundents_list = ["nika", "pavle", "luka", "sandro"]
# print(random.choice(stundents_list))

# scores_listr = [15,1,5,10]
# print(random.choice(scores_listr))


# my_arr = ["nika", "pavle", "luka", "sandro"]
# x = "$".join(my_arr)
# print(x)


my_arr = [5,6,4,3]

def my_join(any_arr):
    sti = ""
    for element in any_arr:
        sti += str(element) + "!"
    return sti
print(my_join(my_arr))