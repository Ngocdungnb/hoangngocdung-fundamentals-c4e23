from random import randint

x = randint(0,100)
print(x)
if x<30:
    print('''
    | (_) __ _| |__ | |_ _ __ (_)_ __   __ _ 
 | | |/ _` | '_ \| __| '_ \| | '_ \ / _` |
 | | | (_| | | | | |_| | | | | | | | (_| |
 |_|_|\__, |_| |_|\__|_| |_|_|_| |_|\__, |
      |___/                         |___/  ''')
elif x<60:
    print('''  
     ___(                        )
   (                          _)
  (_                       __))
    ((                _____)
      (_________)----'
         _/  /
        /  _/
      _/  /
     / __/
   _/ /
  /__/
 //
/'
''')
else :
    print('''
░░░░░░░░░░░█▀▀░░█░░░░░░
░░░░░░▄▀▀▀▀░░░░░█▄▄░░░░
░░░░░░█░█░░░░░░░░░░▐░░░
░░░░░░▐▐░░░░░░░░░▄░▐░░░
░░░░░░█░░░░░░░░▄▀▀░▐░░░
░░░░▄▀░░░░░░░░▐░▄▄▀░░░░
░░▄▀░░░▐░░░░░█▄▀░▐░░░░░
░░█░░░▐░░░░░░░░▄░█░░░░░
░░░█▄░░▀▄░░░░▄▀▐░█░░░░░
░░░█▐▀▀▀░▀▀▀▀░░▐░█░░░░░
░░▐█▐▄░░▀░░░░░░▐░█▄▄░░░
░░░▀▀▄░░░░░░░░▄▐▄▄▄▀░░░
░░░░░░░░░░░░░░░░░░░░░░░
                   ''')
                   