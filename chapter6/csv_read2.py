import numpy as np  # NumPy를 임포트
import csv  # 표준 라이브러리의 csv 모듈을 임포트


# CSV 파일 읽기
dat = np.loadtxt('data1.csv', delimiter=',', skiprows=1, dtype=float)

# ndarray 타입인 dat를 CSV파일에 쓰기(한글을 사용할 수 없으므로 주의)
np.savetxt('data1_saved.csv', dat, fmt='%.1f,%.8f,%d',
           header='time,vel,alt', comments='')

# ndarray 타입인 dat를 CSV파일에 쓰기(한글 사용가능)
with open('out.csv', 'w', newline='', encoding='utf-8') as f:
    f.write('time,속도,고도\n')
    writer = csv.writer(f)
    writer.writerows(dat)
