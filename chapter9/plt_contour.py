import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.mlab import bivariate_normal

# 2차원 메시를 생성
N = 200
x = np.linspace(-3.0, 3.0, N)
y = np.linspace(-2.0, 2.0, N)
X, Y = np.meshgrid(x, y)

# 2변량 정규분포로 2차원 분포 데이터를 만듬
z = 15 * (bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0) -
          bivariate_normal(X, Y, 1.5, 0.5, 1, 1))

# --- 플롯 작도
plt.figure(1)

# (1) z의 값을 농담값으로 삼아 이미지로 나타냄
im = plt.imshow(z, interpolation='bilinear', origin='lower',
                cmap=cm.gray, extent=(-3, 3, -2, 2))

# (2) 등고선 표시
levels = np.arange(-3, 2.5, 0.5)
ctr = plt.contour(z, levels, colors='k', origin='lower',
                  linewidths=2, extent=(-3, 3, -2, 2))

# (3) 등고선에 레이블을 인라인 표시
plt.clabel(ctr, levels, inline=1, colors='black',
           fmt='%1.1f', fontsize=14)
plt.show()
