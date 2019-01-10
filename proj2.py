class store():
    def __init__(self):
        self.price=price
        self.id=id
        self.quant=qunat

    def remove(self,n):
        if self.quant > n:
            self.quant=self.quant-1
        else:
            print("requested amount of quantity unavilable")

    def add(self,m):
        self.quant+=m
        return self.quant

class inventory(store):
    if
