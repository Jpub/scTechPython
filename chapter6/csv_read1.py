import csv # 표준 라이브러리 모듈 csv를 임포트하여 사용할 준비를 한다


# CSV 파일 읽기
with open('data1.csv', 'r', encoding='utf8') as f:
    dat = [k for k in csv.reader(f)] # 리스트 컴프리헨션을 사용한다

# CSV 파일 쓰기
with open('out.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(dat)
