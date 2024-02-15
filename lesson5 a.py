import urllib.request
file = urllib.request.urlopen("http://helloworldbook3.com/data/message.txt")
message = file.read().decode('utf-8')
print(message)



a="周"
b="止随"
print(a+b)

"""
a=input("你的姓氏是什么")
b=input("你的名字是什么")
print(a+b)
"""

"""
print("你需要地毯，先让我知道你房间的大小。")
a=int(input("你的房间长有几米?"))
b=int(input("你的房间宽有几米?"))
print("你要一块 "+str(a*b)+"平方米 大小的地毯")

print("===================================================================")
print("你需要地毯，先让我知道你房间的大小。")
a=int(input("你的房间长有几米?"))
b=int(input("你的房间宽有几米?"))
print("你要一块 "+str(a*b)+"平方米 大小的地毯")
print("你要一块 "+str(a*b*9)+"平方尺 大小的地毯")
print("一平方米地毯要3元")
print("地毯一共要 "+str(a*b*3)+"元")
print("====================================================================")


a=int(input("你有多少个一分: "))
b=int(input("你有多少个一角: "))
c=int(input("你有多少个一元: "))
d = c + b/10 + a/100

print("你一共有",d,"元")
#55+(32/10)+44/100
"""

a= 0.1+0.2
b= 0.3
print(a, b)
if a - b < 0.0000001:
    print("a 等于 b")
else:
    print("a不等于b")
