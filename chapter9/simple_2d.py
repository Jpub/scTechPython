import numpy as np
from numpy import sin, cos
import matplotlib.pyplot as plt

# (1) -pi부터 pi까지 0.1을 1틱으로 배열을 만든다
x = np.arange(-np.pi, np.pi, 0.1)
# 배열 x에 대해 sin(x)를 계산(sin(x)는 유니버설 함수)
y1 = sin(x)
# 배열 x에 대해 cos(x)를 계산
y2 = cos(x)
plt.figure(1)
plt.clf()

# x, y를 작도
plt.plot(x, y1, label='코사인함수')
plt.plot(x, y2, 'r*', markersize=10, label='사인함수')  # (2)
# 각 축의 레이블을 그림
plt.xlabel('X축')
plt.ylabel('Y축')
# 범례를 그림
plt.legend(loc='best')
# (3) 그리기 실행
plt.show()
