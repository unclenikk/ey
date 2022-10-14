#1) for loop
#2) while loop

#i- საიტერაციო ცვლადი 
#for i in range(7):    #range(7) = 0.1.2.3.4.5.6
    #print("nika")


#for x in range(3,6):
    #print(str(x) + " nika")

#for i in range(3,6):
    #print(i, " nika")


 
       #start #finish #step
#for x in range(5, 10, 2 ):    #range (5, 10) = 5,7,9
    #print(str(x) + "nika")


# i = 0
# while i < 5:
    #print("nika")
    # i += 1   #საიტერაციო ცვლადის ინკრემენტაცია 

# full_name = "nika amrazishvili"
# i = 0
# while i < len(full_name):
#     print(full_name[i])
#     i += 1


#a = "qwerty"
#b = "asdfgh"

#qa
#ws
#ed
#rf


# a = "qwerty"
# b = "asdfgh"

# i = 0
# while i < (len(a)):
#     print(a[i]+b[i])

#     i += 1

# if 10>5 and 3 > 1:
#     print("cool")

full_name = input("enter your name: ")

i = 0


while i < len(full_name):
    if full_name[i] in "aeiou":
        print(str(i) + full_name[i])
    i += 1
