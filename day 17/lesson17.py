def say_hello(name):
    print(name + " gamarjoba")
say_hello("nika")
say_hello("levani")


def say_hello(name):
    return(name + " gamarjoba")

def dashla(any_str):
    return any_str.split()
print(dashla(say_hello("nika")))


my_arr = ["nika", "luka", "sandro"]
my_students = {
    "luka": 18,
    "nika": 24,
    "sandro": 30,
    "mzia": 46,
}

print(my_students["nika"])

my_dict = {0: "a",
           1: "b",
           2: "c",
           3: "d"
           }

print(my_dict[0])



my_arr = ["nika", "luka", "sandro"]
my_students = {
    "luka": 18,
    "nika": 24,
    "sandro": 30,
    "mzia": 46,
    "shako_rou": [56,15]
}

print(my_students["nika"])
my_students["erekle"] = 32

print(my_students)


my_students["nika"] = 5

print(my_students)
print(my_students.get("mzia"))

print(list(my_students.items()))
print(list(my_students.items())[0][1])


print(list(my_students.keys()))
print(list(my_students.values()))

my_students.pop("shako_rou")
print(my_students)


list = [1, 1, 2, 3, 5, 9, 13]
print(list[list[2]])



list = [[1,1],[2,3],[5,8,2]]
print(list[list[2][list[1][0]]])







