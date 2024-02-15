"""
a = input("please buy something:")
a=float(a)
if a<= 10:
    print("you must give to me",a*0.9)
else:
    if a>10:
        print("you must give to me",a*0.8)
"""


a=input("you are m or f:")
if a=="f":
    b=input("how old are you:")
    b=int(b)
    if 10<=b<=12:
            print("you can join")
    else:
        print("you can't join")
else:
    print("you can't join")
       
