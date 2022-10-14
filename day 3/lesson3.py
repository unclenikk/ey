# my_name = "nika"
# my_surname = "amrazishvili"
# my_age = 17
# my_pet_name = "oti"
# my_sentence = "my name is {2} my surname {0} my age {1} my pet name {3} ".format(my_surname, my_age, my_name, my_pet_name)

# #ფორმატს ეკუთნის {}.format    {რიცხვი უთითებს ფორმატში ტექსტში რიგობით ადგილს}



# print(my_sentence)

 
# my_name = "nika"
# if "e" in my_name:
#     print("sheicavs e-s")

# else:
#     print("ar sheicavs e-s")

                    #else- არის ფოლსის ტიპის მსგავსი ინფორმაციის გამოტანა მაგ ნიკაში თუ ე არ ურევია დამიპრინტავს ამას
#input
#output
# my_name = input("enter your name: ")

# print("chemi saxelia " + my_name) 

# my_age = 17
# my_age += 2
# print(my_age)

# my_age = input("enter your age: ")  #input-ით ყოველთვის შემოდის სტრინგი
# my_name = input("enter your name: ")
# my_surname = input("enter your surname: ")

# print("my name is {} my surname is {} my age is {}". format(my_name, my_surname,
# my_age))

# year = input("enter years")

# new_age = int(my_age) + int(year)
# print("after {} years i am now {} years old".format(year, new_age))


#print(2+2)
#print("2" + 2)
#print("2" + "2")



# num1 = int(input("enter num1: "))
# num2 = int(input("enter num2: "))

# product = num1 * num2 

# if product > 100:
#     print(product)
# else:
#     print("you lose")    


# += ინკრემენტაცია (გაზრდა)



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