import random 
my_arr = []
for i in range(10):
    my_arr.append(str(random.randint(1,1000)))

x = "!".join(my_arr)
print(x)

def update_light(current):
    arr = ["red","yellow","green"]
    if current == "red":
        return "green"
    return arr[arr.index(current)-1]
print(update_light("red"))


















