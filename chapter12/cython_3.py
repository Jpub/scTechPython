import cython_2
import numpy as np
import time

N = 10000000


# cython_2.py에 정의된 함수의 본래 파이썬 버전
def matrix_cal(X, Y, a):
    for i in range(N):
        if Y[i] < 0:
            Y[i] += 10.0 + 1e-7*i
    return a*X + np.exp(Y)

if __name__ == '__main__':
    # 계산 대상이 될 ndarray 생성
    a = 3.4
    X = np.random.randn(N)
    Y = np.random.randn(N)
    # Cython 버전 함수로 계산
    ts = time.clock()
    Z = cython_2.matrix_cal_cy(X, Y, a)
    print('Cython 함수의 실행 시간: {0:.3f}[s]'.format(time.clock() - ts))
    # 변환전 matrix_cal 함수로 계산
    ts = time.clock()
    Z = matrix_cal(X, Y, a)
    print('원래 버전의 실행 시간: {0:.3f}[s]'.format(time.clock() - ts))
