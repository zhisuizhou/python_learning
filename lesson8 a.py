"""
a=input("输入0到9:")
a=int(a)
for b in range(1,11):
    c=(a*b)
    a=int(a)
    print(a,"*",b,"=",c)
"""



a=input("输入0到9:")
a=int(a)
i=0
while i < 11:
    i=i+1
    print(i,"*",a,"=",i*a)
