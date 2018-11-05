n =  input(" password:  ")
while (len(n)<=8) or n.isalpha() or (n.isupper() or n.islower()) or n.isdigit():
    print ("not ok")
    n = input(" password: ") 
    if (len(n)<=8):
        print ("ngan qua")
    if n.ialpha():
        print(" can so'")   
    if (n.isupper() or n.islower()) or n.isdigit():
        print ("asdas")



