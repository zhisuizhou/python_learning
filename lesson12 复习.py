lst = [1, 2, 3, 4, 5]
##a = len(lst)
##print(a)
##
##b = 7
##if b not in lst:
##     print(b,"不在列表中")
##
##c = lst + [6, 7, 8]
##print(c)
##
##d = lst*2
##print(d)
##
##e = max(lst)
##print(e)
##f = min(lst)
##print(f)
##
##g = sum(lst)
##print(g)
"""
a = 0
for i in lst:
    a = i + a
print(a)
"""
"""
def func_sum(list_a):
    a = 0
    #用循环把所有值一个一个赋给i
    for i in list_a:
        #i+a赋给a（不停循环）
        a = i + a
    return a
#外界打印a
b = func_sum(lst)
print(b)
"""




"""
lst.insert(1,10)
print(lst)


lst.append(20)
print(lst)

lst.extend([30, 40])
print(lst)
"""
