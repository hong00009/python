# 여기는 주석입니다.

# 안녕하세요
# 파이썬입니다.  여러줄 주석처리 Ctrl+/

# a라는 변수에 1이라는 숫자를 저장합니다.
a = 1

# 1. 변수
# 변수이름 = 값
# 변수이름은 어떤 이름이든 상관없음.
# 단, 영어, 숫자, _로 구성, 키워드는 사용 불가

# 키워드(식별자)는 변수이름으로 사용 불가
#if  등 보라색으로 표기되는 것들
import keyword
# print(keyword.kwlist)


# 1.1 number

a = 1000000
# print(type(a))

b = 1.1
# print(type(b))

# 실수 => 부동소수점으로 관리
c = 1.1
d = 1.12
e = -0.02
# print(c-d)

# import math
# print(math.isclose(c-d,e))

# complex  / 허수
f = 1 -4j
# print(type(f))

# 1.2 boolean

a = True
b = False

# print(type(a))

c = 1 # list도 가능 c = [2]
d = 0

# print(bool(c))
# print(bool(d))

e = None
# print(type(e))

# 1.3 String (문자열)
greeting = 'hello'
name = 'hyk'
# print(greeting, name)
# print(type(name))


# age = input() # 입력받기. 어떤 값을 넣어도 문자열(글자) 형태로 받아짐
# print(type(age))

intro = '안녕하세요 저는 \n홍길동\t입니다.  \\'
# print(intro)

intro = """
안녕하세요
저는 홍길동입니다.
docstring
"""
# print(intro)

# string interpolation

dust = 111
message = '오늘 미세먼지 농도는 10입니다.'


message1 = '오늘 미세먼지 농도는 %s입니다.' % dust
# print(message1)

message2 = '오늘 미세먼지 농도는 {}입니다.' .format(dust)
# print(message2)

message3 = f'오늘 미세먼지 농도는 {dust}입니다.'
# print(message3)


# 2. 연산자 
# 2.1 산술연산자
# + - * / 
a = 10
b = 3

# // 나눗셈과정의 '몫'
# print (a // b)

# % 나머지
# print(a % b)

#divmod  몫,나머지 한번에
# print(divmod(a,b))

# ** 거듭제곱
# print(a ** b)

# 2.2 비교연산자
# > < = 
a = 1
b = 2
# print(a >= b)
# print(a <= b)
# print(a == b)
# print(a != b)
# print('hi' == 'hello')

# 2.3 논리연산자
a = True
b = False

# and (둘다 True이면 True)
# print(a and a)
# print(a and b)
# print(b and a)
# print(b and b)

# or (둘 중 하나라도 True이면 True)
# print(a or a)
# print(a or b)
# print(b or a)
# print(b or b)

# not
# print(not a)

# 2.4 복합연산자
n = 0
# n = n + 1
# n += 1
while n < 5 :
    # print(n)
    n+=1

# 2.5 기타연산자
# concatenation 문자열간 연결
# print('hello' + 'hi')

# in 포함되어있는가? True / False
# print ('hi' in 'hihello')
# print(1 in [1, 2, 3, 4])
# print(1 in range(1, 5))

# is 두개가 같은가? Treu / False (==과 비슷)
a = 'hi'
b = 'hi'
# print(a is b)

# 연산자간 우선순위
# print(-3 ** 4)


# 3. 형변환
# 3.1 임시적 형변환

# print(True + 3) # True를 1로

a = 3
#if a % 2 :
    # print('홀수입니다.')

# 3.1 명시적 형변환
# print('미세먼지 농도 : ' + str(10)) # 숫자 > 글자
# print(10 + int('20')) # 글자 > 숫자
# print(float('3.4')) # 글자 > 숫자소수
# print(float(2)) # 숫자 정수 > 숫자 소수 
# print(int('2.5')) # 에러, 10진수 숫자만 int변환 가능



# 4. 시퀀스 데이터 
# 순서가 있다
# 리스트 list, 튜플 tuple, 레인지 range, 문자열 string 등
# 파이썬에서는 List, 다른 언어에서는 Array / 한국어로는 배열
# 4.1 리스트
# a = [value1, value2, value3, ...]
# a[index]

a = []
b = list()
# print(type(a), type(b))

location = ['서울', '대전', '대구']
# print(location[2])
location[0] = '부산' # 리스트 값 수정 가능
# print(location)

#리스트 안 다양한 형태 가능
a = [ # 리스트
    [1, 2, 3], # 리스트
    {4, 5, 6}, # 세트
    (7, 8, 9), # 튜플
    0,
]
# print(a)

# 4.2 튜플
# 수정 불가 (immutable)
# a = (value1, value2, value3, ...)
# a[1]

a = (1, 2, 3, 4, 5)
# a[1] = 10 # 이런식으로 수정 불가
# print(a[2])

b, c = (1, 2)
# print(b, c)
b, c = c, b
# print(b, c)

# 4.3 레인지 range 숫자만가능
# range(n) : 0부터 n-1까지
# range(n,m) : n부터 m-1까지
# range(n, m, s) : n부터 m-1까지 s간격으로

a = range(5,10,2)
# print(list(a))

# 4.4 시퀀스에서 사용할 수 있는 연산

# in
a = 'a'
b = ['a', 'p', 'p', 'l', 'e']
c = 5
d = range(10)
# print(a in b)
# print(c in d)

# concatnation 연결
a = [1, 2]
b = [3, 4]

# print(a + b) # 연결

# 반복
a = [123]
# print(a * 5)  # 5번 반복연결

# indexing
a = 'abcde'
b = range(10)
# print(a[1])
# print(b[5])
# 음수도 가능
# print(a[-2]) #뒤에서부터, -1부터 시작 = d

# slicing 자르기
a = 'hello'
# print(a[1:3])
b = (1, 2, 3, 4, 5)
# print(b[1:3])
c = '123456789'
# print(c[1:10:2])
# print(c[::2])

# 함수
a = [1, 2, 1, 4, 5]
# print(len(a))  # len 파이썬 내장함수, 바로호출해 사용
# print(a.count(1)) # a라는 객체가 가지고 있는 기능을 사용시 . (메소드)

# 5. 시퀀스가 아닌 자료
# 순서가 정해지지 않음

# 5.1 set 집합
# a = {value1, value2, ...}
# 순서가 없고 중복이 없음

a = {5, 2, 3, 4, 1, 2, 3, 4, 5 , 5}
b = {2, 4, 6, 8}

# print(a | b) # 합집합
# print(a - b) # 차집합
# print(a & b) # 교집합

a = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# print(list(set(a))) 
# 리스트를 세트로 형변환 - 중복값 없는 집합형태
# 중복값 없애고 다시 리스트로 변환

#print(dir(a))

# 5.2 dictionary
# a = {key: value1, key2: value2, ...}
# key는 immutable한 것만 가능. 불변. 

a = {}
# a = dict()

book = {
    'apple': '사과', 
    'banana': '바나나',
}
# print(book['apple'])

b = {1: 1, 2: 2, 3: 3, 1: 4} # key 중복 시 가장 나중 key 기준
print(b[1])
print(b)
print(b.keys())
print(b.values())


# 정리
# 1. 시퀀스 (ordered 순서가있음)
# 반복 작업 가능
# - 'String' : immutable
# - [List] : mutable
# - (Tuple) : immutable
# - range() : immutable

# 2. 시퀀스가 아닌것 (unordered 순서가없음)
# - {Set} : mutable
# - {Dict: ionary} : mutable
