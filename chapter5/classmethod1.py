# CoeffVar 클래스를 정의
class CoeffVar(object):
    coefficient = 1

    @classmethod  # 메소드 mul을 클래스 메소드로 지정
    def mul(cls, fact):  # 첫번째 인자는 cls
        return cls.coefficient * fact


# CoeffVar 클래스를 상속하는 클래스 MulFive를 정의
class MulFive(CoeffVar):
    coefficient = 5


x = MulFive.mul(4)  # CoeffVar.mul(MulFive, 4) -> 20
