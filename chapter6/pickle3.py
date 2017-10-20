import pickle
import numpy as np


def pickle_vars(fname, mode='wb', **vars):
    """
    사용법
    pickle_vars('저장할파일명', a=a, b=b, c=c)
    인자로 작성할 파일의 이름과 객체의 이름을 차례로 열거한다
    """
    dic = {}
    for key in vars.keys():
        exec('dic[key]=vars.get(key)')
    with open(fname, mode) as f:
        pickle.dump(dic, f)
    return dic

if __name__ == "__main__":
    # 여러 가지 객체를 생성
    a = np.float(2.3)
    b = np.array([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6]])
    c = {'yokohama': 1, 'tokyo': 2, 'nagoya': 3}
    # 여러 개의 변수와 그에 포함된 데이터를 저장
    saved_dat = pickle_vars('pickle1.pickle', a=a, b=b, c=c)
    # 저장된 pickle 파일에서 데이터를 읽어들임
    with open('pickle1.pickle', 'rb') as f:
        dat = pickle.load(f)
        for key in dat.keys():
            exec(key+'=dat.get(key)')  # 데이터의 원래 변수명으로 복원
