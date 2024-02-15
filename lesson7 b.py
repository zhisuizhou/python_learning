a=input("你的油箱可以装几升油")
if float(a) > 1000000000:
    a = 100000000
    print("你的输入过大，油箱已经被调整为100000000升")
else:
    a=int(float(a))
b=input("你的油箱还有百分之几的油")
b=float(b)
if float(b) > 100:
    b = 100
    print("你的输入过大，已经被调整为百分之100")

c=10
h = 200
#d=a*b*c/100
if a*b/100 > 5:
    e = (a*b/100-5)*c
else:
    e = 0

print("you can go another",e,"km")
print("你离下个加油站还有",h,"千米")
if  e >= h:
    print("你可以在下个加油站加油")
else:
    print("你不可以在下个加油站加油")
