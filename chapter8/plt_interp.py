import numpy as np
import matplotlib.pyplot as plt

# (1) 이름이 너무 길어서 별명을 사용한다
import scipy.interpolate as ipl


# (2) 보간으로 근사할 함수를 정의
def f(x):
    return (x-7) * (x-2) * (x+0.2) * (x-4)

# (3) 정답 데이터 생성(틱 크기 0.1)
x = np.linspace(0, 8, 81)
y = np.array(list(map(f, x)))

# (4) 보간 대상 데이터(틱 크기 1)
x0 = np.arange(9)
y0 = np.array(list(map(f, x0)))

# (5) 보간 함수를 설정(선형보간)
# 보간 함수를 설정(선형보간/3차 스플라인)
f_linear = ipl.interp1d(x0, y0, bounds_error=False)
f_cubic = ipl.interp1d(x0, y0, kind='cubic', bounds_error=False)
#  보간 처리 실행
y1 = f_linear(x)  # 선형 보간
y2 = f_cubic(x)  # 3차 스플라인 보간

# (6) 보간 처리한 데이터와 정답 데이터의 비교를 위해 그래프 작도
plt.figure(1)
plt.clf()
plt.plot(x, y, 'k-', label='근사할 함수')
plt.plot(x0, y0, 'ko', label='보간 전 데이터', markersize=10)
plt.plot(x, y1, 'k:', label='선형 보간', linewidth=4)
plt.plot(x, y2, 'k--', label='3차 스플라인 보간', linewidth=4, alpha=0.7)
plt.legend(loc='best')
plt.xlabel('x')
plt.ylabel('y')
plt.grid('on')
