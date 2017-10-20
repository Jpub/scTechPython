# 파일명 : module_2.py
import module_1  # module_1을 import해서 이 모듈 안의 프로그램을 실행


# module_1 안의 변수에 접근
weight = module_1.wgt
# module_1 안의 함수를 사용
module_1.teacher(weight)
weight = module_1.run(weight)
module_1.teacher(weight)
