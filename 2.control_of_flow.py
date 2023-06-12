# 1. 제어문

# 1.1 조건문
# if <조건식>:
#   if의 조건식이 참인 경우 실행하는 코드
# elif <조건식>:
#   elif의 조건식이 참인 경우 실행하는 코드
# else:
#   거짓인 경우 실행하는 코드

a =10
if a > 5:
    pass
elif a > 8:
    pass
else:
    pass

# 연습1
# 사용자에게 날짜 입력을 받아서 크리스마스인지 확인
# a = input('날짜를 입력하세요(ex: 1/1, 12/12) : ')

# if a == '12/25':
#     print('크리스마스입니다')
# else:
#     print('크리스마스가 아닙니다.')


# 연습2
# 사용자에게 숫자 하나를 입력받아서 홀수인지 짝수인지 확인

# num = int(input('숫자를 입력하세요 : '))
# if num % 2 == 1:
#     # 입력받은 숫자를 2로 나눴을때 나머지가 1이면 홀수
#     print('홀수입니다.')
# else:
#     print('짝수입니다.')

# if num % 3:
#     print('3의 배수 X')
# else:
#     print('3의 배수입니다')

# 연습3
# 사용자에게 1~100 점수를 입력받아서 
# 100~90 A, 89~80 B, 79~70 C, 나머지 F
# 95점 이상인 사람에게는 good 이라는 문장을 추가로 출력

# score = int( input('점수를 입력하세요(0~100):'))

# if score >= 90:
#     print('A')
#     if score >= 95:
#         print('good')
# elif score >= 80:
#     print('B')
# elif score >= 70:
#     print('C')
# else:
#     print('F') 

# 1.2 조건표현식 (다른 언어에서 삼항연산자)
# true_value if <조건식> else false_value

# 홀짝 판별
# num = int( input('숫자를 입력하세요 : '))

# result = '홀수' if num % 2 else '짝수'
# print(result)

num = -7
if num >= 0:
    value = num
else:
    value = 0
# print(value)

# 조건표현식으로 바꿔보기
value = num if num >= 0 else 0
# print(value)


# 1.2 반복문
# while 조건식이 참(True)인 경우 반복적으로 코드를 실행
# while <조건식>:
#   반복할 코드

n = 0 
# while n < 5:
#     print('아직은 5보다 작습니다.')
#     n += 1

greeting =''
# while greeting != 'hi':
#     greeting = input('안녕! \n')

# 1.2.2 for
# for variable in sequence:
#   실행할 코드
# 보통 for 와 in 사이에는 for문안에서만 사용될 변수를 단수형이름으로 지어서 사용함

# for i in range(5):
#     print(i)

# 연습1
# 사용자에게 영단어 하나를 입력받아서 알파벳 하나씩 출력

word = input('영단어를 입력해주세요 : ')
print(word)

for char in word:
    print(char)

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)

print(number)

# 연습2
# 반복문과 조건문을 같이 사용해서 1~20까지의 숫자 중에
# 홀수만 저장된 numbers 리스트를 출력해주세요

# 반복문으로 1~20까지 돌리고
# 하나씩 홀짝 판별하여 새로운 list에 하나씩 저장

# result = []
# for i in range(1,21):
#     if i % 2 == 1:
#          print(i, '홀수')
#         result.append(i)
#      else :
#         # print(i, '짝수')
# # print(result)


# 연습3
# 점심 메뉴 리스트를 작성해서 하나씩 출력

menus = ['라면', '김밥', '돈까스', '삼겹살', '쫄면']

for i in range(len(menus)):
    print(menus[i])
# menus의 수량이 변해도 유동적으로 맞춰 반복되도록 설정함

for idx, menu in enumerate(menus):
    print(idx, menu)

# enumerate : menus 항목 하나하나와 index 0,1,2... 도 함께
# idx, menu = (0, '라면') ★ 변수가 2개 인덱스/값