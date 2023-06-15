# 1. 모듈

# import fibo
# print(dir(fibo))

# print(fibo.fib_for(5))
# print(fibo.fib_re(3))
# dot notation

# 함수도 변수에 저장할 수 있다.
# my_fib = fibo.fib_for
# 함수실행시에는 반드시 () 가 있어야만 실행되므로
# 이렇게 괄호 없이 함수이름만 있다면 함수정의 자체에 접근하는 것
# print(my_fib(4) )


# 2. 패키지

# 패키지 안에 __init__.py 파일이 있어야 패키지로 인식함
# 언더바 두개는 무슨뜻 / 
# myPackage/
#  math /
#       __init__.py
#       fibo.py
#       formula.py
# 아래의 것은 보통 서브모듈이라고 부름

# import myPackage

# print(myPackage)


# from myPackage.math.formula import *
# from 위치에서 * 를 가져와줘
# 서랍에서 도구를 꺼내와 내 책상에 올려놓는 개념
# 너무 많은 것을 가져오는 것은 지양, 꼭 필요한 것만 지정하여 불러오기 

# print(my_max(1, 54))

formula = 123
#내가 변수로 이미 사용해버린 formula가 있다면
# from myPackage.math import formula

# print(formula) # 가장 마지막 이름으로 처리됨

# 변수 이름과 중복될 경우 'as X' 로 이름바꿔 부르기 가능
from myPackage.math import formula as f
# (from 경로) import 모듈 (as 변경할 이름)

# print(f)


# 3. 모듈 사용해보기
# 3.1 math
# print(min(1, 2))

import math
# print(math.pi)
# print(math.e)

pi = math.pi
# print(pi)
# print(math.ceil(pi)) # 올림
# print(math.floor(pi)) # 내림
# print(math.trunc(pi)) 
# # 이런 기능은 외우는 것이 아니라, 파이썬 자습서, 문서에 수학파트 설명 따라 사용

# print(math.pow(2, 5)) # 제곱
# print(math.sqrt(9)) # 제곱근(루트)

# 3.2 random

import random

# print(random.random()) # 0~1 사이의 무작위 숫자
# print(random.randint(1, 10))

# seed
# 난수를 발생시키지만 동일한 순서로 발생시켜야 할때 (고정값으로 버그 상황 재구현)
# random.seed(2)
# print(random.random())

# shuffle # 섞어줌
a = [1, 2, 3, 4, 5]
random.shuffle(a)
# print(a)

# choice /한개고름
result = random.choice(a)
# print(result)

# sample /여러개 고름
result2 = random.sample(a,3) 
# print(result2)


# 3.3  datetime
from datetime import datetime
# datetime 폴더 안에 datetime이라는 파일이 있음..
now = datetime.now()
# print(now)  #지금

today = datetime.today()
# print(today) #오늘

utc = datetime.utcnow()
# print(utc) # utc 기준시간

# 참고 : https://docs.python.org/ko/3/library/datetime.html#module-datetime
# strftime()
# str / f / time () : str을 formating 하겠다 time으로

result = now.strftime('%Y년 %m월 %d일')
# print(result)

result2 = now.strftime('%d / %m / %y')
# print(result2)

# now는 변수/함수를 다량 가지고 있는 객체
# print(now.year)  # 연도
# print(now.weekday()) # 요일(0~6 숫자로 /월~일)

birth = datetime(2023, 1 , 1, 13, 30)
print(birth)
# print(birth.strftime('%m/%d는 내 생일이야'))

from datetime import timedelta

future = timedelta(days=3)
print(future)

print(birth + future)

print(now + timedelta(days=100)) # 100일후

christmas = datetime(2023, 12, 25)
diff= christmas - now # 크리스마스까지 며칠?
print(diff.total_seconds()) # 일을 초로 변환