import numpy as np

# npy 파일에 ndarray를 하나 저장
a = np.array([1, 2, 3])
np.save('foo', a)

# npy 파일에서 ndarray를 복원
a2 = np.load('foo.npy')

# npz(ndarray 여러 개를 저장할 수 있는 파일) 파일에 ndarray를 저장
b = np.array([[1, 2], [3, 4]])
np.savez('foo.npz', a=a, b2=b)  # b를 b2라는 이름으로 저장

# npz 파일 읽기
with np.load('foo.npz') as data:
    a3 = data['a']  # a라는 이름을 가진 변수만 읽어들임
    b3 = data['b2']
