n = {
    "dt": "dep trai",
    "xg": "xinh gai",
    "xt": "xau trai",
    "xg": "xau gai"
}
key = ["dt","xg","xt","xg"]
print (*key)

m = input("nguoi dung nhap: ")
while m not in n:
    print ("not found")
    m = input("nguoi dung nhap: ")

print ("nghia la: ",n[m])