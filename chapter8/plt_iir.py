import numpy as np
import matplotlib.pyplot as plt
# (1) scipy와 별도로 import 해야 함
import scipy.signal as signal

# (2) Chebyshev 1형 필터 설계
b1, a1 = signal.iirfilter(4, Wn=0.2, rp=5, rs=40,
                          btype='lowpass', ftype='cheby1')
w1, h1 = signal.freqz(b1, a1)

# (3) Cauer/elliptic 필터 설계
b2, a2 = signal.iirfilter(4, Wn=0.2, rp=5, rs=40,
                          btype='lowpass', ftype='ellip')
w2, h2 = signal.freqz(b2, a2)

# (4) 필터의 주파수 특성을 작도
plt.title('주파수 특성')
plt.plot(w1, 20*np.log10(np.abs(h1)), 'k-', label='Chebyshev I')
plt.plot(w2, 20*np.log10(np.abs(h2)), 'k--', label='Cauer/elliptic')
plt.legend(loc='best')
plt.ylabel('진폭 [dB]')
plt.xlabel('주파수 [rad/sample]')
plt.show()
