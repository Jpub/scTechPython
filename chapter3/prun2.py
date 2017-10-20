import numpy as np
from memory_profiler import profile


@profile  # 이 함수를 메모리 프로파일링 대상으로
def func_a():
    a = np.random.randn(500, 500)
    return a**2


@profile  # 이 함수를 메모리 프로파일링 대상으로
def func_b():
    a = np.random.randn(1000, 1000)
    return a**2


def func_both():
    a = func_a()
    b = func_b()
    return [a, b]

if __name__ == '__main__':
    func_both()
