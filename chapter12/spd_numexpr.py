import time
import numexpr as ne
import numpy as np

# 커다란 NumPy 배열을 만든다
N = 10000000
a = np.random.randn(N)
b = np.random.randn(N)

# NumPy로 삼각함수 및 곱의 합 계산을 한 후 수행시간을 측정
ts1 = time.clock()
c1 = (a * np.sin(b)).sum()
te1 = time.clock()
print('NumPy : %.6f [s]' % (te1 - ts1))

# Numexpr로 위와 같은 계산을 한 후 수행시간을 측정
ts2 = time.clock()
c2 = ne.evaluate('sum(a * sin(b))')
te2 = time.clock()
print('Numexpr : %.6f [s]' % (te2 - ts2))

# 속도가 향상된 정도를 평가한다
print('%.3f[％] 개선되었다' % (100-100*(te2-ts2)/(te1-ts1)))
