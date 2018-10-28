n =  input(" password:  ")
while (len(n)<=8) or n.isalpha() or (n.isupper() or n.islower()) or n.isdigit():
    print ("not ok")
    n = input(" password: ") 
    if (len(n)<=8):
        print ("ngan qua")
    elif n.isalpha():
        print(" can so'")   
    elif (n.isupper() or n.islower()) or n.isdigit():
        print ("CAN CHU THUONG CA CHU IN VA SO")
    else:
        
        break
print ("ok")     
   

