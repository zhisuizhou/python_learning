class Money:
    def __init__(self, a):
        self.amount = a
    def getMoney(self, a):
        self.amount = self.amount + a

        if self.amount > 99999:
            self.amount = 99999
    def spendMoney(self, a):
        if self.amount >= a:

            self.amount = self.amount - a
    def __str__(self):
        result = "你现在有" + str(self.amount) + "元"
        return result

a = Money(0)
print(a)
a.getMoney(100)
print(a)
a.getMoney(10000)
print(a)
a.spendMoney(100)
print(a)
a.getMoney(100000)
print(a)
a.spendMoney(200000)
print(a)
a.spendMoney(99999)
print(a)
