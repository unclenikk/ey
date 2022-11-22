#როგორ დააბრუნონ ფუნქციებმა მნიშვნელობები რეთარნით 
def reverse_arr():
    
    
    students = ["nika", "ana", "mamuka", "beqa", "dachi", "iva", "ferna"]
    
    new_arr = []
    i = len(students)
    
    while i > 0:
        new_arr.append(students[i-1])
        i -= 1
    print(new_arr)

def list_price():
    my_list = ["xinkali", "mwvaedi", "lobiani", "qababi", "khachapuri", "wyali",]
    price = [2, 20, 15, 10, 15, 2]
    i = 0
    while i < len(my_list):
        print(my_list[i] + " ღირს " + str(price[i]) + "ლარი")
        i += 1






