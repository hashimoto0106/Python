#クラス定義
class MyClass(object):
    x = 0
    y = 0
    
    def my_print(self):
        self.x += 1
        MyClass.y += 1
        print('(x,y) = ({}, {})'.format(self.x, self.y))
        

f = MyClass
hashimoto = MyClass()
naoki = f()

hashimoto.my_print()
naoki.my_print()
naoki.my_print()


class MyClass2(object):
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
        
    def __del__(self):
        self.a = 0
        self.b = 0
        
    def my_print(self):
        print('(a,b) = ({}, {})'.format(self.a, self.b))
        
a = MyClass2(2018,11)
a.my_print()
