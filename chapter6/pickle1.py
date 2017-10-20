import pickle  # 표준 라이브러리 pickle을 import

# 저장할 객체를 만든다
mydata = [1, 2, 3]

# 객체(mydata)를 'pickle1.pickle'(확장자 생략 가능) 파일에 저장
with open('pickle1.pickle', 'wb') as f:
    pickle.dump(mydata, f)

# 'pickle1.pickle' 파일에서 데이터를 읽어 들여 dat에 대입
with open('pickle1.pickle', 'rb') as f:
    dat = pickle.load(f)
