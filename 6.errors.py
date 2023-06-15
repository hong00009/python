# Error

# 1. syntax error (문법오류)
# if True:
#     pass
# else
# 콜론없다

# print('hi)
# 문자열이 따옴표로 끝나지 않았다, 괄호가 닫히지 않았다 등등 파이썬 문법이 안맞아 실행도못한다

# if True print('hello') 
# 엔터누락
# 여기쯤에 문제가 있다고 ^^^^ 로 표시하지만 항상 정확한 것은 아님

# 2. exception(예외)

# ZeroDivisionError
# print(5/0)
# 0으로 나눌 수 없음

# NameError
# print(my_name)
# 그런 이름은 정의되지 않았음

# TypeError
# print(1 + '1')
# int형과 str형은 덧셈을 할 수 없음

# print('1' + 1 )
# str형과 int형은 concat할 수 없음 (덧셈아님)

import random
# random.sample([1, 2])
# missing 1 required positional argument: 'k'
# 이 메소드는 인자가 2개 필요
# 매개변수 1개 부족, k 아규먼트

# random.sample([1, 2], 1, 1, 1, 1, 1, 1)
# takes 3 positional arguments but 8 were given
# 최대 3개 인자 받는데, 9개나 줬다. 인자가 너무 많다

# ValueError
# int('3.5')
# 값이 잘못됐다 (int로 바꿀 수 없는 값)

numbers = [1, 2, 3]
# numbers.index(100)
# 100이란 값은 없다 / 값이 잘못됨

# IndexError
# numbers[100]
# 100번째 인덱스는 없다 /인덱스가 잘못됨

# KeyError
my_dict = {'apple': '사과', 'banana': '바나나'}
# my_dict['melon']
# 그런 키 없음

# ModuleNotFoundError
# import asdf
# 그런 모듈이름은 못찾겠음

# ImportError
# from datetime import asdf
# from 을 통해 모듈 자체는 찾았는데, import를 못했을 때 

# KeyboardInterrupt (ctrl + c 로 종료)
# 무한루프 상황에서 탈출

# 3. 예외 처리

# try:
#   code
# except 예외:
#   code
# try의 코드 실행 중, 예외(에러 등 문제상황)가 발생하면 except 코드로 넘어감

# try:
#     num = int(input('숫자를 입력해주세요 : '))
#     print(f'입력하신 숫자의 제곱은 {num**2}입니다.')
# except ValueError:
#     print(f'숫자를입력하라고!')

# try:
#   code
# except (예외1, 예외2, ...):
#   code

# try:
#     num = input('나눌 값을 입력해주세요: ')
#     100 / int(num)
# except (ValueError, ZeroDivisionError):
#     print('문제발생')


# try:
#     num = input('나눌 값을 입력해주세요: ')
#     100 / int(num)
# except (ValueError):
#     print('숫가자 아닙니다')
# except (ZeroDivisionError):
#     print('0으로 나눌 수 없음')

# try:
#     my_list = []
#     print(my_list[5])
# except IndexError as err:
#     print(f'{err} : 오류가 발생했습니다')

# try:
#     my_list = [1, 2, 3]
#     print(my_list[3])
# except IndexError:
#     print('인덱스 에러입니다.')
# else: # 예외처리가 발생하지 않았다면 실행됨
#     print('else')

# try:
#     my_list = [1, 2, 3]
#     print(my_list[2])
# except IndexError:
#     print('인덱스 에러입니다.')
# finally: # 오류가 있든 없든 실행됨
#     print('finally')

# raise ValueError('테스트입니다') # 강제로 에러를 일으킴

# 연습
# 양의 정수 두개를 받아 몫과 나머지로 출력하는 함수를 정의

# 숫자가 아닌 다른 값을 넣음
# 0을 넣음


def my_div(a, b):
    try:
        result1 = a // b
        result2 = a % b

    except ZeroDivisionError:
        print('0으로는 나눌 수 없음!')

    except:
        print('숫자가 아님')

    else:
        return (result1, result2)


print(my_div(1,0))
print(my_div('1','5'))
print(my_div(2,3))
