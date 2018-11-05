sheep = [5, 7, 300, 90, 24, 50 ,75]
print("Hello, my name is Dung and these are my sheep sizes: ",sheep, sep = "\n" )
n  = max(sheep)
print("Now my biggest sheep has size: ", n,"let's shear it")
m = sheep.index(n)
sheep[m] = 8
print("After shearing, here is my flock: ", sheep, sep = "\n")
for i in sheep:
    x = sheep.index(i)
    sheep[x] = i +50
print("One month has passed, now here is my flock", sheep, sep = "\n")