class MyCalc(object):
    @staticmethod
    def my_add(x, y):
        return x + y

# MyCalcインスタンスを生成しなくてよい
a = MyCalc.my_add(5, 9)
print(a)
