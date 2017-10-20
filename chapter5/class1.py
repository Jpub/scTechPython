# 클래스 정의
class MyClass(object):  # (1) 상속하는 클래스 없음
    """ (2) 클래스의 닥스트링 """
    # (3) 변수 x, y의 정의
    x = 0
    y = 0

    def my_print(self):
        self.x += 1  # x를 인스턴스마다 별도로 존재하는 변수로 다룸
        MyClass.y += 1  # y를 클래스마다 존재하는 변수로 다룸
        print('(x, y) = ({}, {})'.format(self.x, self.y))


# 클래스의 인스턴스를 생성
f = MyClass  # (5) ()가 없으면 클래스에 별명을 붙인다는 의미
a = MyClass()  # (6) MyClass 클래스의 인스턴스를 만들고 여기에 a라는 이름을 붙임
b = f()  # (7) f()는 MyClass()와 같은 의미((5)에서 별명을 붙였으므로)
# (8) 메소드 실행
a.my_print()
b.my_print()
b.my_print()
