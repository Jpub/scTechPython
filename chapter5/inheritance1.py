# (1) 클래스 MyBase의 정의 (MyDeriv의 기반 클래스)
class MyBase(object):
    coeff = 2

    def __init__(self, x):
        self.x = x

    def mult(self):
        return self.coeff * self.x


# (2) 클래스 MyDeriv의 정의 (MyBase의 파생 클래스)
class MyDeriv(MyBase):
    coeff = 3  # (3) 속성을 재정의

    # (4) 생성자 메소드를 재정의
    def __init__(self, x, y):
        super().__init__(x)  # (5) 기반 클래스의 메소드 호출 예
        self.y = y  # (6) 속성 y를 추가하여 인스턴스를 생성할 때 초기화함

    # (7) 새로운 메소드를 재정의
    def mult2(self):
        return self.coeff * self.x * self.y


# (8)MyBase와 MyDeriv를 사용하는 예
a = MyBase(3)  # MyBase의 인스턴스를 생성
print(a.mult())  # 결과 : 2*3=6
b = MyDeriv(3, 5)  # MyDeriv의 인스턴스를 생성
print(b.mult())  # 결과 : 3*3=9 (상속받은 메소드 확인)
print(b.mult2())  # 결과 :3*5*5=45 (새로 추가한 메소드 확인)
