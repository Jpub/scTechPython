import h5py
import numpy as np

# 저장할 데이터를 생성
t = np.arange(0, 5, 0.1)
y = np.sin(2*np.pi*0.3*t)
dist = [2, 5, 1, 3, 8, 9, 12]

# 데이터의 일부를 계층 구조로 저장
with h5py.File('data1.h5', 'w') as f:
    f.create_group('wave')
    f.create_dataset('wave/t', data=t)
    f.create_dataset('wave/y', data=y)
    f.create_dataset('dist', data=dist)

# with 블럭을 벗어나면 f가 일단 닫힌다

# 데이터 읽기
with h5py.File('data1.h5', 'r') as f:
    t = np.array(f['wave/t'])  # ndarray 형태로 읽어들인다
    y = np.array(f['wave/y'])
    dist = np.array(f['dist'])
