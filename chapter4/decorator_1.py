# 데코레이터 (debug_log)의 기능을 활성화하기 위한 플래그
debug_trace = True
# 위의 플래그가 활성인 경우, 로그 파일을 연다
if debug_trace:
    log_file = open("debug.log", "w", encoding='utf-8')


# 데코레이터 함수의 정의
def debug_log(func):
    if debug_trace:
        def func_and_log(*args, **kwargs):
            # func을 실행하기 전에 로그 파일에 기록
            log_file.write("시작 %s: %s, %s\n" %
                           (func.__name__, args, kwargs))
            # func를 그대로 실행
            r = func(*args, **kwargs)
            # func가 종료되면 로그 파일에 이를 다시 기록
            log_file.write("종료 %s: 리턴값 %s\n" % (func.__name__, r))
            return r
        return func_and_log
    else:
        return func  # debug_trace = False면 아무 것도 바뀌지 않는다


# 데코레이터로 myFunc의 기능을 바꾼다
@debug_log
def myfunc(x):
    return x+x

# 데코레이터로 변경된 myFunc를 실행
myfunc(3)
myfunc(5)
log_file.close()  # 로그 파일을 닫는다
