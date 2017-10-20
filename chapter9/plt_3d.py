from mpl_toolkits.mplot3d.axes3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.mlab import bivariate_normal

# 2차원 메시를 작성
N = 200
x = np.linspace(-3.0, 3.0, N)
y = np.linspace(-2.0, 2.0, N)
X, Y = np.meshgrid(x, y)

# 2변량 정규분포로 2차원 분포 데이터를 생성
z = 15 * (bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0) -
          bivariate_normal(X, Y, 1.5, 0.5, 1, 1))

# 데이터를 3차원 플롯으로 플로팅
fig = plt.figure(1)  # (1)
ax = fig.add_subplot(111, projection='3d')  # (2)
surf = ax.plot_surface(X, Y, z, cmap=cm.gray)
ax.set_zlim3d(-3.01, 3.01)
plt.colorbar(surf, shrink=0.5, aspect=10)
plt.show()
