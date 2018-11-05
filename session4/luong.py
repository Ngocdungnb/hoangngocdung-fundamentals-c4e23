l_list = [
    {
        'stt' : '1',
        'name': 'huy',
        'hour': 30,
        'VND': 50,
    },
    {
        'stt' : '1',
        'name': 'huy',
        'hour': 20,
        'VND': 50,
    },
    {
        'stt' : '1',
        'name': 'huy',
        'hour': 15,
        'VND': 50,
    }
]
for i in l_list:
    print(i['hour'])
x = 0
for h in l_list:
    z = h['hour']*h['VND']
    x += z
    # x = x + z 
print(x)
    

