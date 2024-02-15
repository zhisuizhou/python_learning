"""
def func_c(string_1,string_2):
    #把输入的东西相乘,赋值
    c = float(string_1) * float(string_2)
    #返回出去
    return c

a = input("number1:")
b = input("number2:")
d = func_c(a, b)
print(d)




###写一个函数，实现对一个数进行平方后再减去1


def func_p(string_a):
    c = float(string_a)
    #把几米（设a）乘自己，赋给b
    #把b减1，赋给b
    b = c * c - 1
    #返回b出去（别忘了赋值）
    return b

a = input("number:")#3
b = func_p(a)
print(b)







def func_m(float_b):
    #用直径（a）除以2，得半径，赋值（设b）
    b = float_b/2
    #用3.1415926赋给π（pi）
    pi = 3.1415926
    #π乘b乘b，赋给c
    c = pi * b * b
    #把c返回出去（别忘了赋值）
    return c

a = input("number:")
a = float(a)
ret = func_m(a)
print(ret)
"""
