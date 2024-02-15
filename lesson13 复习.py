def get_max_socre(a):
    course = None
    score = None

    #取字典中的所有值
    c = a.values()
    #放入列表
    b = list(c)
    #排序
    b.sort()
    #取b列表中最后一个元素
    d = b[-1]
    #用b列表中的最大值找到字典中值相应的键
    #取出字典中第一个值 与 d比较（相等：把键赋给course，值赋给score，返回出去，break）(不相等：继续循环）

    while True:
        
        key = None
        a[key]
        
            
    return course, score
    

dic = {
    "语文" : 90,
    "数学" : 97,
    "英语" : 91 }
course, score = get_max_socre(dic)
print(course, score)
