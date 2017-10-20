import cProfile
import numpy as np
import pstats


def is_prime(a):
    """ 소수를 판정하는 프로그램(페르마의 소정리) """
    a = abs(a)
    if a == 2:
        return True
    if a < 2 or a & 1 == 0:
        return False
    return pow(2, a-1, a) == 1


def mysum(n):
    """ 1부터 N까지의 정수의 합을 계산 """
    return np.arange(1, n+1).sum()


def task1(n):
    """ 다음 2가지 처리를 수행한다
       (1) 1부터 N까지의 정수 중에서 소수를 찾는다
       (2) 1부터 N까지의 정수의 합을 계산한다
    """
    # (1)
    out = []
    append = out.append
    for k in range(1, n+1):
        if is_prime(k):
            append(k)
    # (2)
    a = mysum(n)
    return [out, a]


def task2(n):
    """ 1부터 N까지의 sqrt()를 계산한다 """
    return np.sqrt(np.arange(1, n+1))


def main():
    task1(100000)  # 부하가 큰 계산
    task2(100000)  # 부하가 작은 계산


if __name__ == '__main__':  # (3)
    from line_profiler import LineProfiler
    prf = LineProfiler()
    prf.add_function(is_prime)
    prf.runcall(is_prime, 999)
    prf.print_stats()
