class MyCalc(object):
    @staticmethod
    def my_add(x, y):
        return x + y

a = MyCalc.my_add(5, 9)  # a = 14 가 된다 (MyCalc의 인스턴스를 만들지 않아도 된다)
