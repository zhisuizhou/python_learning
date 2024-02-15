def getMax(lst):
    lst.sort()
    #a = lst[-1]
    b = len(lst)-1
    a = lst[b]
    
    
    
    return a
    
lst = [4, 2, 1, 6, 7, 9]
print(lst)
a = getMax(lst)
print(a)
