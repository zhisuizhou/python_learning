"""
def is_12345(a):
    if a == '1' or a == '2' or a == '3' or a == '4' or a == '5' or a =='5.0'or \
       a == '1.0' or a == '2.0' or a == '3.0' or a == '4.0':
        return True
    return False

print("enter 5 names")
aa = []

for i in range(5):
    name = input("")
    aa.append(name)
print("the names are", aa)
aa.sort()
print("the names are", aa)
print("the third name you entered in:",aa[2])
"""

a = input("replace one name. which one? (1-5)")
a = float(a)

while a < 1 or a > 5:
    a = input("replace one name. which one? (1-5)")
    a = float(a)
    
a = int(a)
del aa[a-1]
b = input("new name: ")
aa.insert(a-1, b)
print("the names are",aa)


"""

a = input("replace one name. which one? (1-5)")

while not is_12345(a):
    a = input("replace one name. which one? (1-5)")

print("ok")
"""

