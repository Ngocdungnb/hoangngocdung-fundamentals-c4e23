c = {
    "dt": "dep trai",
    "xg": "xinh gai",
    "xt": "xau trai",
    "xg": "xau gai"
}
# key = ["dt","xg","xt","xg"]
# print (*key)

while True:
    m = input("nguoi dung nhap: ")
    if m in c:
        print(c[m])
    else:
        x = input("co muon them noi dung ko?(y/n): ").upper()
        print (x)
        if x == "N":
            print("thank u")
            break
        elif x == "Y":
            z = input("nhap noi dung: ")
            c[m]= z
            print(c)
     

        
            
            