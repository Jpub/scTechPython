import numpy as np
import scipy as sp
import scipy.stats
import matplotlib.pyplot as plt

plt.style.use('ggplot')

# (1) 통계분포함수 설정(이후 고정)
rv = sp.stats.rayleigh(loc=1)

# (2) 위의 통계분포함수로 확률변수 생성
r = rv.rvs(size=3000)

# (3) 확률밀도함수를 작도하기 위한 100개의 데이터 점
x = np.linspace(rv.ppf(0.01), rv.ppf(0.99), 100)

# 원래의 확률밀도함수와 함께 샘플링한 데이터의 분포를 작도
plt.figure(1)
plt.clf()
plt.plot(x, rv.pdf(x), 'k-', lw=2, label='확률밀도함수')
plt.hist(r, normed=True, histtype='barstacked', alpha=0.5)
plt.xlabel('값')
plt.ylabel('분포도')
plt.show()
