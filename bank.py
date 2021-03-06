class Customer():
    def __init__(self, name, balance=0.0):

        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):

        self.balance += amount
        return self.balance

shrini = Customer("pan",4500.00)
print(shrini.withdraw(200))
print(shrini.deposit(3000))
print(shrini.name,shrini.balance )
print(shrini.withdraw(500.0)
print(shrini.deposit(3000))