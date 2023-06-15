def fib_for(n):
    result = [1, 1]
    for i in range(1, n):
        end1 = result[-1] # 끝에서 첫번째 값, 리스트 자체적 기능 표기법
        end2 = result[len(result) - 2] # 끝에서 두번째 값len함수 활용 표기법
        fib_num = end1 + end2
        result.append(fib_num)
    return result[-1]

def fib_re(n):
    if n == 1 or n == 0:
        return 1 # 반복을 멈출 기준 작성
    else:
        return fib_re(n-1) + fib_re(n-2) # 핵심내용 작성
