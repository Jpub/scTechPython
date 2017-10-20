import scipy as sp
import matplotlib.pyplot as plt

# (1) scipy와 별도로 import해야 한다
from scipy import signal

# (2) 선형 시스템을 정의
s1 = sp.signal.lti([1], [1, 1])

# (3) bode 함수를 이용한 분석
w, mag, phase = sp.signal.bode(s1)

# (4) 보드 플롯 작도
plt.figure(1)
plt.subplot(2, 1, 1)
plt.semilogx(w, mag)  # Bode magnitude plot
plt.box('on')
plt.xlabel('주파수 [rad/s]')
plt.ylabel('게인 [dB]')
plt.title('보드 플롯')
plt.subplot(2, 1, 2)
plt.semilogx(w, phase)  # Bode phase plot
plt.xlabel('주파수 [rad/s]')
plt.ylabel('위상 [deg]')
plt.box('on')
plt.show()
