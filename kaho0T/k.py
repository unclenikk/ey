#day 10 first kahoot 

#1) რამდენჯერ დაიპრინტება შედეგი ტერმინალში

print("hello, world!")
print("python magaria")
# 2-ჯერ

 
#2) რა დაიპრინტება

spam = 7
if spam >5:
    print("five")
if spam > 8:
    print("eight")
# დაიპრინტება five


#3) შედეგი ? 

x = 5
print(type(x))

y = 5.0
print(type(y))
#int და float


#)4  შედეგი ?

a = "nika 11 keshelava"
print(len(a))
# 17


#5) რამდენჯერ დაიპრინტება?(ორი სფეისია შუაში)

for x in "ban  ana":
    print(x)
#8


#6) შედეგი ?

my_str = "nika 11 keshelava"
print(my_str[5] + my_str[6]+ "4")
#114


#7) რა დაიპრინტება ? 

a = "Hello, World!"
print(a[3] + a[5])
#l,


#8) რამდენჯერ იმუშავებს ეს კოდი:

for i in range(1,20,3):
    print(i)
#7

#----------------------------------------------------------------------------------------


#day 11 second kahoot

#1) ramdenjer daiprinteba "python is cool"

i = 0
while i < 5:
    print("python is cool")
    break
#უსასრულოდ [დავაბრეაქე იმიტომ რომ სხვაკოდების გაშვების შემდეგ არ წაიღოს უსასრულოდ]


#2) რამდენჯერ დაიპრინტება "python is cool"

i = 0 
while i < 5:
    print("python is cool")
    i += 1
#5


#3) რამდენჯერ დაიპრინტება ორივე წინადადება ჯამში?

i = 0 
while i < 5:
    print("python is cool")
    i += 1
    print("javascript is also cool")
#10


#4) რაები დაიპრინტება

foods = ["khinkali", "mwvadi", "xachapuri", "xizilala"]

foods.append("pizza")
print(foods[4])

foods.insert(2, "lobiani")
print(len(foods))
# pizza და 6


#5) რა შედეგს მივიღებთ?

def my_function(my_number):
    print(my_number + 10)

my_function(20)
#30


#6) kesh-ის დაპრინტვისთვის, რა უნდა ჩავსვათ კვადრატულ ფრჩხილებში? []

full_name = "nika keshelava"
print(full_name[5:9])
#5:9


#7) რა დაიპრინტება საბოლოოდ 

foods = ["khinkali", "mwvadi", "xachapuri", "xizilala"]
                                
x_counter = 0

for food in foods:
    if food[0] == "x":   # ციკლში წერია თუ საჭმელელებიდან საჭმლის პირველი ასო იწყება x დან x_counter გაზარდე 1 ით
        x_counter += 1
print(x_counter)
#2   ანუ xachapuri da xizilala


#7) რა არის ალგორითმი


# ალგორითმი არის: მითითებების და ინსტრუქციების სია, რომლითაც ვაღწევთ რაიმე სასურველ მიზანს


#8) რა შედეგი გვექნება


def my_function(my_number):       # down\\\
    if my_number > 10:
        print("bigger than 10")     #  ფუნქციაში ვწერთ თუ 20 მეტია ათზე დაპრინტე : დიდია 10 ზე თუარადა ნაკლებია 10 ზე 
    elif my_number < 10: 
        print("lower than 10")    # uf ///
my_function(20)
#"bigger than 10"

#----------------------------------------------------------------------------------------

#day 12 the third Kahoot

#1) რამდენი ხაზი დაიპრინტება ტერმინალში ?


print("Hello World !")
print("""
dolor sit
amet.""")

print("Hello \n again.")
#6


#2) რას გამოიტანს ტერმინალში

name = "Nika"
age = 36

p = "My name is {1}, and I am {0}".format(name,age)
#p isnt print <3


#3) რა შედეგს გამოიტანს ტერმინალში ? 

i = 5
while i >= 0:
    print#(Goal_oriented_academy) 
    
#Error

#4) chad- ის დაპრინტვისთვის რა უნდა ჩაჯდეს ფრჩხილებში?

name = "Anri Jochadze"
print(name[7:11])
#7:11


#5) რა შედეგს გამოიტანს ტერმინალში.


num1 = int(input())  #14
num2 = int(input())  #17

my_sum = num1 + num2
boolioni = True

if num1 % 2 > 0 and num2 > 10:   
    print(my_sum) 
else:
    print(boolioni)  
# True 


#6) რა დაიპრინტება ტერმინალში.


age_1 = 5 ** 2
age_2 = 50 / 2

if age_1 > age_2:
    print("luka")
elif age_2 > age_1:
    print("nika")    
else:
    print(age_1 + age_2)
#50.0 


#7) რომელი item -ი დაიპრინტება ტერმინალში.


num = 3
things = ["str",2,[0,6,num], 5.76]
print(things[2][1])
#6


#8) რა რიცხვი დაიპრინტება ტერმინალში.


i = 0
while i < 5:
    i += 1
    if i ==3: # თუ i ==3 
        continue    # გააგრძელე ციკლი 3 ის გარეშე  პროგრამირების ენაზე if continue ში წერია ეს 
    print(i)
#1,2,4,5


#9) რა დაიპრინტება ტერმინალში.


list = [6,3,2,5,4,7] 
for x in list:              
    if(x % 2 == 1 and x > 4):        # თუ რიცხვის გაყოფის შემდეგ მივიღებთ ნაშთს 1 ს და x მეტია 4 ზე დაპრინტე სიიდან ის რიცხვი 
        print(x)
        break   # ბრეიქი კი აჩერებს ამ ციკლს პირველი სწორი პასუხის შემდეგ ანუ 5 ის იქით აღარაფერს ხედავს
#5 


#10) რას უდრის sum ცვლადი ?

sum = 0    # 5 + 4 + 3 + 2 + 1 = 15
x = 5
while x > 0:
    sum += x
    x -= 1
print(sum + 30 / 10)
#18.0


#day 13 fourth kahoot

#1) რა არის შედეგი ? 

num = 26
num = 9

print(num1 // num2)
#2


#2) შედეგი ?

full_name = "shota rustaveli"
i = 0
for char in full_name:
    if char == "s":
        i += 1
print(i)
#2 

 
#3) შედეგი ? 

num1 = 26
num2 = 9

print(num1 % num2)
# 8


#4) შედეგი ?

full_name = "nikachad keshelava"

i = 0
for char in full_name:
    if char not in "aeiou":
        i += 1
print(i)
#11

# 5) შედეგი ?
def my_sum(a,b):
    return a + b    #ვაბრუნებთ a + b ს       [3+4]
print(my_sum(2,3) * my_sum(3,4))   # 2+3 = 5 * 7 = 35 
#35                                            


#6) შედეგი ?

arr = ["nika", "nika1", "nika2"]
i = 0
for element in arr:
    i += 1
# არაფერი inst print here >>>>>>>>


#7) შედეგი ?

arr = ["nika", "nika1", "nika2"]
i = 0
for element in arr:
    i += 1
print(i)
#3


#8) შედეგი ?

arr = ["nika", "nika1", "nika2"]
i = 0
for element in arr:
    for char in element:
        i += 1
print(i)
#14



# day 13 fifth/1 kahoot 

#1) რას დაპრინტავს ? 

import random 

food_list = ["mwvadi","pizza","brinji","xawapuri","lobiani"]
print(random.choice(food_list))
#კაცი შვილმა არ იცის cos its random baby


#2) რას დაპრინტავს ? 


food_list = ["mwvadi","pizza","brinji","xawapuri","lobiani"]
print(random.choice(food_list))  # რომ არ გაეყვითლებინა მაგიტომ ""
#Error


#3) რას დაპრინტავს ? 

foods = ["mwvadi","pizza","brinji","xawapuri","lobiani"]

i = -1
for element in foods:
    for char in foods:
        i+= 1
#არაფერი where is a print >>>>>?


#4) რას დაპრინტავს ? 

foods = ["mwvadi","pizza","brinji","xawapuri","lobiani"]

i = -1
for food in foods:
    if food[1] == "i":
        i += 1
print(i)
#0


#5) რას დაპრინტავს ? 

foods = ["mwvadi","pizza","brinji","xawapuri","lobiani"]

i = -1
for food in foods:
        i += 1
print(i)
#4


#6) რას დაპრინტავს ? 

foods = ["mwvadi","pizza","brinji","xawapuri","lobiani"]

i = -1
for element in foods:
    for char in foods:
        i+= 1
print(i)
#24


#7) რას დაპრინტავს ? 

foods = ["mwvadi","pizza","brinji","xawapuri","lobiani"]

i = -1
for element in foods:
    for char in foods:
        i + 1
print(i)
# -1 


#8) რას დაპრინტავს ? 

foods = ["mwvadi","pizza","brinji","xawapuri","lobiani"]

i = -1
for element in foods:
    for char in foods:
        i = 1
print(i)
#1


#9) რას დაპრინტავს ? 

foods = ["mwvadi","pizza","brinji","xawapuri","lobiani"]

i = -1
for element in foods:
    for char in foods:
        i -= 1
print(i)
#-26


#10) რას დაპრინტავს ? 

foods = ["mwvadi","pizza","brinji","xawapuri","lobiani"]

i = -1
for element in foods:
    for char in foods:
        i -+ 1
print(i)
#-1


#11) რას დაპრინტავს ? 

x = 5
x**=3

print(x)
#125


#12 რას დაპრინტავს ? 

a = 330
b = 330

print("A")if a>b else print("=")if a==b else print("B")
# =

#---------------------------------------------------------------------------------------- 

#day 14 sixth kahoot

#1) git add . ში რას ნიშნავს . ? 
#ყველაფერს


#2) რა არის .git ?
#metadata            -[მეტადატა არის მონაცემთა საცავი]

#3)git add. ში რისი ჩასმა შეგვიძლია .ის ნაცვლად ? 
#ფაილის და ფოლდერის

#4)რა შედეგს გამოიტანს ტერმინალში ტერმინალში ?

def first_non_consecutive(arr):
    i = 0
    while i < len(arr) - 1:
        if arr[i+1] - arr[i] != 1:
            return arr[i+1]
        i += 1
print(first_non_consecutive(1,2,3,5,6))
#error

#5)რა შედეგს გამოიტანს ტერმინალში ?

def first_non_consecutive(arr):
    i = 0
    while i < len(arr) - 1:
        if arr[i+1] - arr[i] != 1:
            return arr[i+1]
        i += 1
print(first_non_consecutive(1,2,3,5,6))
#none


#6) რა შედეგს გამოიტანს ტერმინალში ?

def car_speed(s):
    return s * 100000 // 3600
print(car_speed(220))
#6111


#7) რა შედეგს გამოიტანს ტერმინალში ?

def never(s):
    final_str = ""
    for char in s:
        final_str += char * 2
    return final_str
print(never('hello worlde'))
# hheelllloo  wwoorrllddee


#8) რა შედეგს გამოიტანს ტერმინალში ?

def update_light(current):
    arr = ["red", "yellow", "green"]
    if current == "red":
        return"green"
    return arr[arr.index(current) - 1]
print(update_light("red"))
#error


#9) რა შედეგს გამოიტანს ტერმინალში ?

def update_light(current):
    arr = ["red", "yellow", "green"]
    if current == "red":
        return"green"
    return arr[arr.index(current) - 1]
print(update_light("red"))
#green


#10) რა შედეგს გამოიტანს ტერმინალში ?

def repeat_str(repeat,string):
    final_str = ""
    for i in range(repeat):
        final_str += string
    return final_str
print(repeat_str(4, "hello my brothers and sisters ანუ ძმანო და დანო ტანო ტატანო"))
#4


#11) რა შედეგს გამოიტანს ტერმინალში ?

def sum(arr):
    temp_sum = 0
    for element in arr:
        if element > 0:
            temp_sum += element
    return temp_sum

print(sum([80085,28,2008,-102]))
#82121


#12) რა შედეგს გამოიტანს ტერმინალში ?

def string(s):
    if s == "":
        return [""]
    final_str = s.split()
    return  final_str
print(string("hello nika zuka dato vano da lashas mama"))
#['hello', 'nika', 'zuka', 'dato', 'vano, 'da', 'lashas', 'mama']


#13) რა შედეგს გამოიტანს ტერმინალში ?

def better(class_points, your_points):
    sum_of_points = sum(class_points)
    ammount_of_students = len(class_points)

    avarge_score = sum_of_points / ammount_of_students

    if your_points > avarge_score:
        return True
    elif your_points <= avarge_score:
        return False
print(better(10,20,15,60,40))
#error


#14) რა შედეგს გამოიტანს ტერმინალში ?

def better(class_points, your_points):
    sum_of_points = sum(class_points)
    ammount_of_students = len(class_points)

    avarge_score = sum_of_points / ammount_of_students

    if your_points > avarge_score:
        return True
    elif your_points <= avarge_score:
        return False
print(better([45,59,10,20,30,14,15,60,],69))
#True

#---------------------------------------------------------------------------------------- 

#day 16 the seventh kahoot

#1) რა შედეგს გამოიტანს ტერმინალში ?

my_arr = [i for i in range(15,25) if i % 4 == 2]
print(my_arr)
#[18, 22]


#2) რა შედეგს გამოიტანს ტერმინალში ?

friends = {
    "dato": "14",
    "andria": 15,
    "luka": "15",
    "nika": 14,
    "AND OTHERS": "?"
}
print(friends["nika"])
print(friends["dato"])
# 14 14 


#3) რა შედეგს გამოიტანს ტერმინალში ?

friends = {
    "dato": ["luka", "nika"],
    "andria": ["zuka","nika","lasha"],
    "gabrieli": ["zuka", "andria","duta"],
    "nika": ["dato","luka","tamari","barbare"],
}
print(friends["gabrieli"][3])
print(friends["nika"][2])
print(friends["andria"][1])
print(friends["dato"][1])
#error

#4) რა შედეგს გამოიტანს ტერმინალში ?

def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - 2 * son_years_old)
print(twice_as_old(47,14)*(33,2))
#(33, 2, 33, 2, 33, 2, 33, 2, 33, 2, 33, 2, 33, 2, 33, 2, 33, 2, 33, 2, 33, 2, 33, 2, 33, 2, 33, 2, 33, 2, 33, 2, 33, 2, 33, 2, 33, 2)


#5) რა შედეგს გამოიტანს ტერმინალში ?

friends = {
    "dato": ["luka", "nika"],
    "andria": ["zuka","nika","lasha"],
    "gabrieli": ["zuka", "andria","duta"],
    "nika": ["dato","luka","tamari","barbare"],
}
print(friends["gabrieli"][0])
print(friends["nika"][2])
print(friends["andria"][2])
print(friends["dato"][0])
#zuka tamari lasha luka


#6) რა შედეგს გამოიტანს ტერმინალში ?

def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - 2 * son_years_old)
print(twice_as_old(47,14)*twice_as_old(33,9))
#285


#7) რა შედეგს გამოიტანს ტერმინალში ?

def get_planet_name(id):
    arr = ["Mercury","Venus","Earth","Jupiter","Saturn","Uranus"  ,"Neptune"]
    return arr[id-1]
print(get_planet_name(3)+get_planet_name(6)+get_planet_name(8))
#EarthSaturnNeptune


#8) რა შედეგს გამოიტანს ტერმინალში ?

def never(arr):
    i = 0
    while i < len(arr)-1:
        if arr[i+1] - arr[i] != 1:
            return arr[i+1]
        i += 1
print(never(100,10,200,2022))
#error


#9) რა შედეგს გამოიტანს ტერმინალში ?

def never(arr):
    i = 0
    while i < len(arr)-1:
        if arr[i+1] - arr[i] != 1:
            return arr[i+1]
        i += 1
print(never([100,10,200,2022]))
#none

#---------------------------------------------------------------------------------------- 

#day 18 eight kahoot

#1) რა დაიპრინტება ტერმინალში ?

list_num = list((range(abs(-3), 7)))
print(list_num)
#[3,4,5,6]


#2) რამდენი ხაზი დაიპრინტება ტერმინალში ? 

greeting = input("")
for char in greeting:
    print("char + !")
#len(greeting)


# 3) რა ერორი გამოვა ტერმინალში ?

a = [4,1,2,3]

b = list(range(1,6, 2))
for i in a:
    b.append(a[i + 1] + a[i])
print#(B)   სინტაქსისთვის # მოხსენით თქვენ და მიხვდებით სხვაობას 
#Out of Range Error


#4) რას გამოიტანს ტერმინალში ?

user_name = "GigaNigga" 
print("Hello, " + user_name)   #upper P daweret da Error aris 
#Error


#5) რა დაიპრინტება ტერმინალში 

list = [[3,5],[2,1,4,1][1,1,2]]
print(list[list[2][list[1][3]]][2])
#4


#6) რას უდრის total - ი

kalata = [20, 40, 10]
fasdakleba = 20
total = 0

for item in kalata:
    total += item - (item * fasdakleba //100)
print(str(float(total)) + "is your total price .")
#56


#70 რა დაიპრინტება ტერმინალში ?

full_name = "Jeki-Chadi"

for char in full_name[5::2]:
    if char == "c":
        break
    print(char)
#{c
# a
# i}


#8) რამდენი ხაზი დაიპრინტება ტერმინალში 

numbers = list(range(50,10, -5))
for number in numbers:
    if number <= 0:
        break
    print(numbers -20)
#8




























