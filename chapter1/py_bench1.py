import numpy as np
import time


def mult_basic(N, M, L, a, x, y):
    """ 행렬계산을 사용하지 않고 for문으로 사용해서 계산하는 함수
    단, ndarray를 사용하지 않으면 배열을 원하는 크기로 만들기가 어렵기 때문에,
    입력 변수는 NumPy의 ndarray로 만들어 넘긴다 """
    r = np.empty((N, L))
    for i in range(N):
        for j in range(L):
            tmp = 0.0
            for k in range(M):
                tmp = tmp + a[k]*x[i][k]*y[k][j]
            r[i][j] = tmp
    return r


def mult_fast(N, M, L, a, x, y):
    """ NumPy의 함수를 사용한 고속 계산 함수
    함수 mult_basic과 같은 결과를 얻는다 """
    return np.dot(x*a, y)  # 한줄로 처리할 수 있다


if __name__ == '__main__':
    # 계산 대상이 되는 배열 생성
    np.random.seed(0)
    N = 10000
    M = 1000
    L = 10000
    a = np.random.random(M) - 0.5
    x = np.random.random((N, M)) - 0.5
    y = np.random.random((M, L)) - 0.5

    # 행렬계산을 사용하지 않고 for문 사용
    ts = time.time()
    r1 = mult_basic(N, M, L, a, x, y)
    te = time.time()
    print("Basic method : %.3f [ms]" % (1000*(te - ts)))

    # NumPy를 사용한 고속 계산
    ts = time.time()
    r2 = mult_fast(N, M, L, a, x, y)
    te = time.time()
    print("Fast method  : %.3f [ms]" % (1000*(te - ts)))
