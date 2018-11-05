n =  input(" password:  ")
while not n.islower(): 
    print ( " not ok")
    n = input(" password: ") 
    while not n.isupper(): 
        print ( " not ok")
        n = input(" password: ") 
        while not n.isdigit():
            print ( " not ok")
            n = input(" password: ") 
            while not len(n)>8:
                print ( " not ok")
                n = input(" password: ") 
else:
    print("oke ")