import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
# (1) scipy와는 별도로 import 해야함
from scipy.fftpack import fft

# (2) 30 Hz 신호와 잡음을 합성한 신호 y를 생성
Fs = 500  # 샘플링 주파수
T = 1/Fs  # 샘플링 간격
L = 2**14  # 신호의 길이(샘플링 수)
t = sp.arange(L)*T  # 시간 벡터
y = np.sin(2*np.pi*30*t) + 5*sp.randn(t.size)  # 신호생성

# (3) FFT 수행
Y = sp.fftpack.fft(y, L)/L
f = (Fs/L)*sp.arange(L/2 + 1)  # 주파수 벡터를 구함

# (4) "원래의 시계열 데이터"와 "FFT로 주파수 분석을 거친 결과"를 그래프로
plt.figure(1)
plt.subplot(2, 1, 1)
plt.plot(t, y)
plt.xlabel('시간 [s]')
plt.ylabel('값')
plt.subplot(2, 1, 2)
plt.plot(f, 2*abs(Y[:L/2 + 1]))
plt.xlabel('주파수 [Hz]')
plt.ylabel('|Y(f)|')
