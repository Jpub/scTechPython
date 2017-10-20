# 클래스 정의
class MyClass(object):  # 상속하는 클래스 없음
    """ 이 클래스의 닥스트링 """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def my_print(self):
        print('{}년에 열리는 올림픽 개최지는 {}'.format(self.x, self.y))

# 클래스의 인스턴스를 생성
a = MyClass(2016, '리우데자네이루')
b = MyClass(2020, '도쿄')
# 메소드를 실행
a.my_print()
b.my_print()
