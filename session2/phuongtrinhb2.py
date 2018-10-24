a = int(input("bien a = "))
b = int(input("bien b = "))
c = int(input("bien c = "))
e = b*b - 4*a*c
print (e)
x = -b/2*a
x1= (-b+e**(1/2))/2*a
x2= (-b-e**(1/2))/2*a 
if e < 0:
    print("Vo nghiem")
elif e == 0:
    print("Co 1 Nghiem",x)
else:
    print("co 2 nghiem",x1 ,x2)