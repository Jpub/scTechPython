import numpy as np
from numba import jit

nthreads = 2  # 검증 환경이 듀얼 코어이기 때문에 스레드 수를 2로 설정
size = 10000000


# 원래 함수
def func_np(a, b):
    return np.exp(2.1 * a + 3.2 * b)


# Numba로 속도를 향상시킨 함수
@jit('void(double[:], double[:], double[:])', nopython=True, nogil=True)
def inner_func_nb(result, a, b):
    for i in range(len(result)):
        result[i] = np.exp(2.1 * a[i] + 3.2 * b[i])
