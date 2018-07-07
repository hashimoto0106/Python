class MyBase:
    coeff = 2
    
    def __init__(self,x):
        self.x = x
        
    def mult(self):
        return self.coeff * self.x

class MyDeriv(MyBase):
    coeff = 3
    
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y
        
    def mult2(self):
        return self.coeff * self.y


a = MyBase(3)
print(a.mult())
b = MyDeriv(3, 5)
print(b.mult2())
print(b.mult())
    
