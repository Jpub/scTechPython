import xlwt  # Excel 파일 쓰기를 위한 라이브러리
import xlrd  # Excel 파일 읽기를 위한 라이브러리

# --- Excel 파일 쓰기
# Workbook을 만듬
wb = xlwt.Workbook()
# 시트 추가
ws = wb.add_sheet('시트1')
# 시트의 특정 셀에 값을 넣음
ws.write(0, 0, 'Upper Left')
ws.write(1, 0, 1)
ws.write(1, 1, 2)
ws.write(1, 2, xlwt.Formula("A3+B3"))
# Workbook에 이름을 지정하여 저장
wb.save('xlwt.xls')

# --- Excel 파일 읽기
# 읽어들일 Workbook을 지정하여 파일 열기
wb = xlrd.open_workbook('xlwt.xls')
# 시트명으로 시트를 지정
st = wb.sheet_by_name('시트1')
# 지정한 시트의 특정 셀 값을 읽은 뒤 화면에 표시
print(st.cell(0, 0).value)
