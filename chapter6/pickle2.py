import pickle
import numpy as np

# 저장할 객체를 만든다
a = np.float(2.3)
b = np.array([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6]])
c = {'yokohama': 1, 'tokyo': 2, 'nagoya': 3}

# 여러 개의 객체를 하나의 pickle 파일로 만들기
with open('pickle1.pickle', 'wb') as f:
    pickle.dump(a, f)
    pickle.dump(b, f)
    pickle.dump(c, f)

# 저장한 pickle 파일에서 여러 개의 객체를 읽어들이기
with open('pickle1.pickle', 'rb') as f:
    a2 = pickle.load(f)
    b2 = pickle.load(f)
    c2 = pickle.load(f)
