a=input("输入0到9:")
a=int(a)
b=input("你希望乘到几")
b=int(b)

for i in range(1,b+1):
        print(a,"*",i,"=",a*i)
