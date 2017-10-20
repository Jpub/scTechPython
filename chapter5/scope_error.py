x = 10


class MyClass(object):
    x = 3  # x가 속하는 네임스페이스가 생성된다

    def __init__(self, y):
        self.x += y

    def my_add(self, z):
        x = x + z  # 오류 : x의 유효 범위가 생성되지 않았다
        # self.x 로 바꾸면 참조 가능


if __name__ == '__main__':
    a = MyClass(10)
    a.my_add(10)
    print(a.x)
