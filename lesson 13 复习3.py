list_a = [1, 2, 3]

#把索引代表的值取出来，赋给a
#a*2，赋给a
#a赋给索引代表的值

##list_a[0] = list_a[0] * 2
##list_a[1] = list_a[1] * 2
##list_a[2] = list_a[2] * 2
##
##print(list_a)

#得知列表中元素的个数（设a个）
#减1
#写a个：把索引代表的元素*2 赋给（替换）索引代表的元素

##a = len(list_a)
##for i in range(a):
##    list_a[i] = list_a[i] * 2
##print(list_a)


#创造循环
#用循环做n次（变量，值的个数）
#循环中：
#a*2赋给索引所代表的值
def func_lst(lst_a):
    a = len(lst_a)
    for i in range(a):
        lst_a[i] = lst_a[i] * 2
    return lst_a

list_a = func_lst(list_a)
print(list_a)

