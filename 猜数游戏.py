import random
secret = random.randint(1, 100)
guess = 0
tries = 0
print("我是机器人小程序，我有一个秘密数字，让你来猜猜")
print("它是一个从1-100的数字，我会给你6次尝试")
while guess != secret and tries < 6:
    guess = int(input("你猜的数字是什么？ "))
    if guess < secret:
         print("太小了，重新猜!")
    elif guess > secret:
         print("太大了，重新猜")
    tries = tries + 1
if guess == secret: 
    print("你猜对了！好厉害！")
   
else:
     print("6次机会用完了，太可惜了!")
     print("秘密数字是：", secret)
