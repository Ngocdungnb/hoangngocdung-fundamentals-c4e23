#items = ["ghe","so huyet","chao"]
#i =  int(input("index: "))
#name = input( "mon moi: ")
#items[i-1] = name
#print (*items, sep = "\n")
items = ["ghe","so huyet","chao"]
i = int(input("muon xoa:"))
items.pop(i-1)
print(*items, sep = "\n")
