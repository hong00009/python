# 함수 function

height = 200
width = 50
# 사각형의 둘레 300, 넓이 5000

height2 = 100
width2 = 100



dull = height * 2 + width * 2
nulb = height * width
# print(f'사각형의 둘레는 {dull}, 넓이는 {nulb}입니다')

# 1. 함수의 선언
# parameter = 매개변수
# def func(parameter1, parameter2, ...):
#   code line1
#   code line2
#   ...
#   return value

def rectangle(height, width):
    perimeter = 2 * (height + width)
    area = height * width

    print(f'사각형의 둘레는 {perimeter}, 넓이는 {area}입니다')

# 2. 함수의 호출
# argument = 인수 /함수에 넣는 값
# func(args1, args2) 


# rectangle(100,100)
# rectangle(200,100)
# rectangle('hello') > 동작X

# 3. 연습
# print(max(10,5)) 

def my_max(num1, num2):
    if num1 > num2:
        print(f'{num1} 더 큽니다.')
    elif num2 > num1:
        print(f'{num2} 더 큽니다.')  
    else:
        print('같습니다.')
    # return None
    # 리턴을 하지 않으면, 파이썬은 자동으로  return None을 하게 된다
# result = my_max(10,10)
# print(result)

# 4. return
def my_max(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
        print('hello') # 리턴 이후에 작성된 내용은 리턴 후 함수가 끝나기 때문에 더이상 처리가 안됨
        print('hello')
    else:
        return num1

result = my_max(1, 2)
# print(result)

# 5. 인자 (parameter)

# 5.1 위치 인자

def cylinder(r, h):
    return r**2 * h * 3.14

# print(cylinder(5, 10))
# print(cylinder(10, 5))
# print(cylinder(1))

# 5.2 기본값
# def func(args=value):
#   return args
# 아무런 인자를 받지 못할 경우 처리할 기본인자값

def greeting(name='이름없음'):
    print(f'{name}님 안녕하세요!')

# greeting('홍길동')
# greeting('이순신')
# greeting()

# 기본인자는 첫번째 인자로는 설정할 수 없음
# def greeting(name='이름없음', location):  > X 불가

# def greeting(location, name='이름없음'):
#     print(f'{name}님 {location}에서 접속했습니다!')
# greeting('ㅁ',)
# greeting(name='홍길동', location='서울')
# greeting(location='서울', name='홍길동')

# 위치인자 사용시 모두 항상 채워넣어야
## 항상 위치인자를 먼저 사용해야한다.
# greeting(location='서울', '홍길동') > X 불가
# SyntaxError: positional argument follows keyword argument


# print 함수 인자들 (*values, sep, end, file, flush)
# print('hello')
# print('hello', end='????')
# print('hello', 'hi', sep='/')


# 5.3 가변 인자 리스트
# def func(*args):
#   code ...
#   return ...
# 몇개의 인자가 들어와도 상관없다는 * 별표
# print('hello', 'hi', '안녕', '안녕하세요', sep='/')

# def my_max(*numbers):
#     a = 0
#     for i in numbers:
#         if i > a:
#             a = i       
#     return a
    
# result = my_max(1, 2, 3, 4, 5, 100, 1000) 
# print(result)


# 내코드
def my_max(*numbers):
    result = numbers[0]
    
    for number in numbers:
        if result < number:
            result = number
    return result


# 강의 코드 
def my_max(*numbers):
    result = 0
    
    for idx, number in enumerate(numbers):
        # 만약 for문의 첫 번째 실행이라면 (index가 0), 해당 값을 제일 큰 수(result)로 설정
        if idx == 0:
            result = number
        # 만약 첫 번째가 아니라면 (index가 0이 아님) result 값과 비교
        else:
            if result < number:
                result = number    
    return result


result = my_max(-1, -2, -3, -4, -5, 2) 
# print(result)


# 5.4 정의되지 않는 키워드 인자 처리
# def func(**kwargs):
#   code ...
# kwargs = keyword arguments / 데이터(key 와 value)가 몇개 들어올 지 모르지만 유동적으로

# print(dict(name='홍길동', location='서울'))

# 위 문장은 아래와 같은 동작을 함
# a = {
#     'name' : '홍길동',
#     'location' : '서울',
# }
# print(a)

def fake_dict(**kwargs):
    result = []
    for k, v in kwargs.items(): # items() : key, value를 뽑아냄
        result.append(f'{k}: {v}')
    print(', '.join(result))
# fake_dict(name='홍길동', location='서울')


# 예시

def user(username, password, password_confirm):
    if password == password_confirm:
        print(f'{username}님 회원가입이 완료되었습니다.')
    else:
        print('비밀번호가 일치하지 않습니다.')

# user 함수에 이렇게 인자를 넣어도 되고
# user('홍길동','1234','12345')

# 이렇게 별도로 만들어 **kwargs(별 두개와 키워드 아규먼츠)로 통째로 넣을 수도 있음
# 파이썬이 적절히 풀어서 제자리에 넣어줌
my_user = {
    'username' : '이순신',
    'password': 'qwer',
    'password_confirm': 'qwer',
}

# user(**my_user)


# 6/14
# 6. lambda
# lambda parameter : expression
# 람다는 콜론 : 을 기준으로 앞은 매개변수, 뒤는 연산
def my_sum(a, b):
    return a+b

result = my_sum(1, 5)
# print(result)

# print((lambda a,b: a + b)(1, 2))


def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f = lambda x : x + 42
# f변수에 할당되면서 f는 함수로 호출할 수 있게됨
def f(x):
    return x + 42
# 42가 저장됨

# print(f(100))
# 100을 넣고 print 시 142가됨
# 함수재사용보다는 선언한 당시에 즉시 사용하는 경우에 가까움

# 7. 이름공간 및 스코프(scope)
# 앞글자만 따서 LEGB - 우선순위순

# 1. Local 로컬스코프 : 정의된 함수 내부
# - 함수가 실행된 시점 이후부터 리턴할 때까지 존재
# 2. Enclosed : 상위함수
# (함수 안의 함수(중첩)가 가능하므로)
# - 함수가 실행된 시점 이후부터 리턴할 때까지 존재
# 3. Global : 함수 밖 or import된 모듈
# - 모듈이 호출된 시점 이후 끝까지 존재
# 4. Built-in : 파이썬에 내장되어있는 함수 혹은 변수
# - 파이썬이 실행된 이후 끝까지 존재

# 기존의 함수 이름과 똑같은 변수를 생성하여 이름이 겹친 상태
# print = 'hello'
# print(print)
# print를 문자열 값으로 할당하고 함수식으로 호출하면 
# "str형식은 함수가 아니어서 실행할 수 없어" 라고 하며 에러남

a = 1 # 전역변수 a
def localscope(a):
    # 로컬변수 a > 함수 내부에서만 쓰이는 변수
    print(a)

# localscope(10)

# 타입힌팅
# 함수 인자의 타입이 뭔지 힌트를 준다 / 함수 어노테이션
def my_sum(a: int, b: int) -> int:
    return a+b
# a, b 인자는 int형으로 받을거고, 리턴 결과도 int형이 될 것이다 라는 힌트

global_a  = 1 
def localscope2():
    global global_a
    global_a = 2
    print(global_a)

localscope2()
# print(global_a)
# 함수 내부값만 실행되고 바깥의 변수값은 변경이안됨
# 바깥에 있는 변수(전역변수)를 내부에서 사용할거면 global 처리를 해줘야함

# 8. 재귀함수(recursive function)

# 예제, 팩토리얼 계산 일반 함수
def fact(n):
    result = 1
    while n > 1:
        result = result * n
        n -= 1
    return result
# => 120
# print(fact(6))


# 팩토리얼 재귀
def factorial(n):
    if n <=1:
        return n
    else:
        return n * factorial(n-1)
# print(factorial(5))


# 피보나치 수열 일반 함수
def fib(n):
    result = [1, 1]
    for i in range(1, n):
        end1 = result[-1] # 끝에서 첫번째 값, 리스트 자체적 기능 표기법
        end2 = result[len(result) - 2] # 끝에서 두번째 값len함수 활용 표기법
        fib_num = end1 + end2
        result.append(fib_num)
    return result[-1]
# print(fib(10))

# 피보나치 수열 재귀
def fib(n):
    if n == 1 or n == 0:
        return 1 # 반복을 멈출 기준 작성
    else:
        return fib(n-1) + fib(n-2) # 핵심내용 작성
# print(fib(10))