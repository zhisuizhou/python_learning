"""
numBlocks = 3
for block in range(0, numBlocks):
    print('block:', block)
    for line in range(0, block * 2): # (本行及以下1行) 关于行数和星号数的公式
        print('line:', line)
        for star in range(0, (block + line) * 2):    
            print('* ', end='')
        print('# block:', block, 'line:', line, 'star:', (block + line) * 2)
        print('line 9')
    print("line 10")

import time
a = input("Hou many seconds:")
a = int(a)
for i in range(a, 0, -1):
    print(i) 
    time.sleep(1)
print("BLAST OFF!")

import time
a = input("Hou many seconds:")
a = int(a)
for i in range(a, 0, -1):
    print(i,"", end = "") 
    print(i * "* ")
    time.sleep(1)
print("BLAST OFF!")
"""

print("\t热狗 \t小面包 \t番茄酱 \t芥末 \t洋葱")
count = 1
for dog in range (10):  # 热狗 loop, for dog in range(0,2)
    for bun in range (10):  # 小面包 loop
        for ketchup in range (10):  # 番茄酱 loop
            for mustard in range (10):  # 芥末 loop
                for onion in range (10):  # 洋葱 loop
                    print("#", count, "\t", end='')
                    print(dog, "\t", bun, "\t", ketchup, "\t", end='')
                    print(mustard, "\t", onion)  # onion loop
                    count = count + 1
