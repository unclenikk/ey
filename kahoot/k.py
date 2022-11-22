#day 10 first kahoot 

#1)
#   რამდენჯერ დაიპრინტება შედეგი ტერმინალში

print("hello, world!")
print("python magaria")
# 2-ჯერ

 
#2)
#   რა დაიპრინტება

spam = 7
if spam >5:
    print("five")
if spam > 8:
    print("eight")
# დაიპრინტება five


#3)
#   შედეგი ? 

x = 5
print(type(x))

y = 5.0
print(type(y))
#int და float


#)4 
#   შედეგი ? 

a = "nika 11 keshelava"
print(len(a))
# 17


#5)
#   რამდენჯერ დაიპრინტება?(ორი სფეისია შუაში)

for x in "ban  ana":
    print(x)
#8


#6)
#   შედეგი ? 

my_str = "nika 11 keshelava"
print(my_str[5] + my_str[6]+ "4")
#114


#7)
#   რა დაიპრინტება ? 

a = "Hello, World!"
print(a[3] + a[5])
#l,


#8)
#   რამდენჯერ იმუშავებს ეს კოდი:

for i in range(1,20,3):
    print(i)
#7

#----------------------------------------------------------------------------------------


#day 11 second kahoot

#1)
#   ramdenjer daiprinteba "python is cool"

i = 0
while i < 5:
    print("python is cool")
    break
#უსასრულოდ [დავაბრეაქე იმიტომ რომ სხვაკოდების გაშვების შემდეგ არ წაიღოს უსასრულოდ]


#2)
#   რამდენჯერ დაიპრინტება "python is cool"

i = 0 
while i < 5:
    print("python is cool")
    i += 1
#5


#3)
#   რამდენჯერ დაიპრინტება ორივე წინადადება ჯამში?

i = 0 
while i < 5:
    print("python is cool")
    i += 1
    print("javascript is also cool")
#10


#4)
#   რაები დაიპრინტება

foods = ["khinkali", "mwvadi", "xachapuri", "xizilala"]

foods.append("pizza")
print(foods[4])

foods.insert(2, "lobiani")
print(len(foods))
# pizza და 6


#5)
#   რა შედეგს მივიღებთ?

def my_function(my_number):
    print(my_number + 10)

my_function(20)
#30


#6)
#   kesh-ის დაპრინტვისთვის, რა უნდა ჩავსვათ კვადრატულ ფრჩხილებში? []

full_name = "nika keshelava"
print(full_name[5:9])
#5:9


#7)
#   რა დაიპრინტება საბოლოოდ 

foods = ["khinkali", "mwvadi", "xachapuri", "xizilala"]
                                
x_counter = 0

for food in foods:
    if food[0] == "x":   # ციკლში წერია თუ საჭმელელებიდან საჭმლის პირველი ასო იწყება x დან x_counter გაზარდე 1 ით
        x_counter += 1
print(x_counter)
#2   ანუ xachapuri da xizilala


#7)
#   რა არის ალგორითმი

# ალგორითმი არის: მითითებების და ინსტრუქციების სია, რომლითაც ვაღწევთ რაიმე სასურველ მიზანს


#8)
#   რა შედეგი გვექნება 

def my_function(my_number):       # down\\\
    if my_number > 10:
        print("bigger than 10")     #  ფუნქციაში ვწერთ თუ 20 მეტია ათზე დაპრინტე : დიდია 10 ზე თუარადა ნაკლებია 10 ზე 
    elif my_number < 10: 
        print("lower than 10")    # uf ///
my_function(20)
#"bigger than 10"

#----------------------------------------------------------------------------------------

#day 12 the third Kahoot

#1)
#   რამდენი ხაზი დაიპრინტება ტერმინალში ?

print("Hello World !")
print("""
dolor sit
amet.""")

print("Hello \n again.")
#6


#2)
#   რას გამოიტანს ტერმინალში

name = "Nika"
age = 36

p = "My name is {1}, and I am {0}".format(name,age)
#არაფერს.


#3)
#   რა შედეგს გამოიტანს ტერმინალში ? 

i = 5
while i >= 0:
    print#(Goal_oriented_academy) 
    
#Error

#4)
#   chad- ის დაპრინტვისთვის რა უნდა ჩაჯდეს ფრჩხილებში?

name = "Anri Jochadze"
print(name[7:11])
#7:11


#5)
#   რა შედეგს გამოიტანს ტერმინალში.

num1 = int(input())  #14
num2 = int(input())  #17

my_sum = num1 + num2
boolioni = True

if num1 % 2 > 0 and num2 > 10:   
    print(my_sum) 
else:
    print(boolioni)  
# True 


#6)
#   რა დაიპრინტება ტერმინალში.

age_1 = 5 ** 2
age_2 = 50 / 2

if age_1 > age_2:
    print("luka")
elif age_2 > age_1:
    print("nika")    
else:
    print(age_1 + age_2)
#50.0 


#7)
#   რომელი item -ი დაიპრინტება ტერმინალში.

num = 3
things = ["str",2,[0,6,num], 5.76]
print(things[2][1])
#6


#8)
#   რა რიცხვი დაიპრინტება ტერმინალში.

i = 0
while i < 5:
    i += 1
    if i ==3: # თუ i ==3 
        continue    # გააგრძელე ციკლი 3 ის გარეშე  პროგრამირების ენაზე if continue ში წერია ეს 
    print(i)
#1,2,4,5


#9)
#   რა დაიპრინტება ტერმინალში.

list = [6,3,2,5,4,7] 
for x in list:              
    if(x % 2 == 1 and x > 4):        # თუ რიცხვის გაყოფის შემდეგ მივიღებთ ნაშთს 1 ს და x მეტია 4 ზე დაპრინტე სიიდან ის რიცხვი 
        print(x)
        break   # ბრეიქი კი აჩერებს ამ ციკლს პირველი სწორი პასუხის შემდეგ ანუ 5 ის იქით აღარაფერს ხედავს
#5 


#10)
#   რას უდრის sum ცვლადი ?

sum = 0    # 5 + 4 + 3 + 2 + 1 = 15
x = 5
while x > 0:
    sum += x
    x -= 1
print(sum + 30 / 10)
#18.0

#----------------------------------------------------------------------------------------

#



















































































































































































































































































































































