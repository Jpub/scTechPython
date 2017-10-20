# (1) 전역 네임스페이스에 x를 정의
x = 100


class MyClass:
    # (2) 이 클래스의 변수 i와 x를 정의
    i = 10  # 메소드 price() 안에서 참조
    x += 2  # 전역 네임스페이스 상의 x에 2를 더함
    xx = x + 2  # (3) MyClass 안의 x를 참조
    print('xx = ', xx)

    def price(self):
        y = self.i * x  # (4) 전역 네임스페이스의 객체 x를 참조
    z = self.i * self.x  # (5) 인스턴스 속성 -> 클래스 속성 순으로 검색하여 참조
    # z = i * x  # (6) 오류 (여기서 변수 i를 볼 수 없다)
    print("price y = %d" % y)
    print("price z = %d" % z)

    def shop(self):
        # price()  # (7) 오류 (NameError)
        self.price()  # (8) 오류 없음
        # MyClass.price(self) # (9) 역시 오류 없음
        MyClass.i = 20  # (10) 클래스 변수를 변경
        print("메소드 shop 실행 끝")


# (11) 테스트를 위한 실행 코드
if __name__ == '__main__':
    a = MyClass()
    b = MyClass()
    a.shop()  # 이 안에서 MyClass.i = 20 이 실행된다.
    print('(a.i, b.i) = ({}, {})'.format(a.i, b.i))
    a.i = 2  # 인스턴스 속성 값을 설정
    MyClass.i = 4  # 클래스 속성 값을 설정
    print('(a.i, b.i) = ({}, {})'.format(a.i, b.i))
