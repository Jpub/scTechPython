import numpy as np
import scipy as sp

# 저장할 데이터를 생성
t = np.arange(0, 5, 0.1)
y = np.sin(2*np.pi*0.3*t)

# MAT-file에 쓰기
out_dat = {}
out_dat['time'] = t  # ndarray t를 time이라는 이름으로 out_dat 내부에 추가
out_dat['y'] = y
sp.io.savemat('data2.mat', out_dat, format='5')

# MAT-file을 읽기
matdat = sp.io.loadmat('data1.mat', squeeze_me=True)
tt = matdat['time']  # ndarray로 읽어들임
