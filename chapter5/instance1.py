import time


class MyTime(object):
    def __init__(self, hour, minutes, sec):
        self.hour = hour
        self.minutes = minutes
        self.sec = sec

    @staticmethod  # now()를 스태틱 메소드로 지정
    def now():
        t = time.localtime()
        return MyTime(t.tm_hour, t.tm_min, t.tm_sec)

    @staticmethod  # two_hours_later()를 스태틱 메소드로 지정
    def two_hours_later():
        t = time.localtime(time.time() + 7200)
        return MyTime(t.tm_hour, t.tm_min, t.tm_sec)

# MyTimes 클래스의 인스턴스를 3가지 방법으로 생성
a = MyTime(15, 20, 58)  # __init__ 를 사용한 일반적인 방법
b = MyTime.now()  # 스태틱 메소드를 사용한 인스턴스 생성 1
c = MyTime.two_hours_later()  # 스태틱 메소드를 사용한 인스턴스 생성 2
