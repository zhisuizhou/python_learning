numBlocks = int(input('你希望打印多少个星星块: '))
numLines = int(input('每个块都多少行星星: '))
numStars = int(input('每行有多少个星星: '))
for block in range(0, numBlocks):   # 4
    for line in range(0, numLines): # 5
        for star in range(0, numStars): # 6    
            print('* ', end='') # 7
        print() # 8
        print('line:', line) # 9
    print('block:', block) # 10
