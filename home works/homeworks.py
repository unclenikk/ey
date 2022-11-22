#da1)

#შემოგვაქვს ჩვენი მონაცემები პრინტ ფუნქციაში





name = "nika"                 
surname = "amrazishvili"      
age = 17                     
height = 182.5               
is_darkhair = "black"          
hobby= "basketball"          
knows_programming = False     
nikname = "unclenik"        
have_dogs = 1       

print("my name and surname is" + " " + name + " " + surname + " " + " my age is " + " " + str(age) + " " + " my height is" + " " + str(height) + " " + "my hair color is" + " " + str(is_darkhair) + " " + "my hobby is" + " " + hobby + " " + str(knows_programming) + " " + "my nickname is" + " " + nikname + " " + "have dogs" + " " + str(have_dogs))





#day2)

#შევკრიბოთ ჩვენი მონაცემები და დავაფორმატოთ


my_name = "nika"
my_surname = "amrazishvili"
my_age = 17
my_pet_name = "oti"
my_sentence = "my name is {2} my surname {0} my age {1} my pet name {3} ".format(my_surname, my_age, my_name, my_pet_name)


print(my_sentence)








#day3)



#შემოვიტანეთ 3 რიცხვი შევკრიბოთ კენტები და დავპრინტოთ ჯამი




number1 = int(input("enret number1: "))
number2 = int(input("enret number2: "))
number3 = int(input("enret number3: "))
trust = 0
if number1 % 2 == 1:
    trust += number1
if number2 % 2 == 1:
    trust += number2
if number3 % 2 == 1:
    trust += number3
print (trust)















#day4)

# შემოგვაქვს 2 სახელი რომელშიც მეტი თანხმოვანია ვპრინტავთ იმას


name1 = input("enter any name1: ")
name2 = input("enter any name2: ")

ammount_of_consonant_in_name1 = 0
ammount_of_consonant_in_name2 = 0

for L in name1:
    if L in "ბგდვზთკლმნპჟრსტფქღყჩცზწხჯჰ":
        ammount_of_consonant_in_name1 += 1
for L in name2:
    if L in "ბგდვზთკლმნპჟრსტფქღყჩცზწხჯჰ":
        ammount_of_consonant_in_name2 += 1
if ammount_of_consonant_in_name1 > ammount_of_consonant_in_name2:
    print("the ammount of consonant in name 1 is more and it contains {} consonant".format(ammount_of_consonant_in_name1))
elif ammount_of_consonant_in_name1 < ammount_of_consonant_in_name2:
    print("the ammount of consonant in name 2 is more and it contains {} consonant".format(ammount_of_consonant_in_name2))
else:
    print("they have equal ammount of consonant")














#day5)



full_name = input("enter name: ")

i = 0 

while i < len(full_name):
    if full_name[i] in "aeiou":
        print(str(i) + full_name[i])
    i += 1 














#day6)

#ვუმატებთ საჭმელს ფასებს


my_list = ["xinkali", "mwvaedi", "lobiani", "qababi", "khachapuri", "wyali",]
price = [2, 20, 15, 10, 15, 2]


print(len(my_list))
print(len(price))

i = 0
while i < len(my_list):
    print(my_list[i] + " ღირს " + str(price[i]) + "ლარი")
    i += 1













#day7)

#უდიდესი რიცხვი

scores = [20, 43, 56, 73, 10, 6, 87, 45, 97]

max_num = scores[0]
  
  
    # სქორს ეძლევა სიაში რიცხვის ადგილი
for score in scores:
    if score > max_num:    # თუ მეტია მითითებული რიცხვი მაქსიმალურზე 
        max_num = score    # მაქსიმალური რიცხვი შეედაროს მეორეს
print(max_num)




#სიის შებრუნება
students = ["nika", "ana", "mamuka", "beqa", "dachi", "iva", "ferna"]
new_arr = []
i = len(students)
while i > 0:
    new_arr.append(students[i-1])
    i -= 1
print(new_arr)






























#day8)







































#day9)




































#day10)