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

# word = input('영단어를 입력해주세요 : ')
# print(word)

# for char in word:
#     print(char)

# numbers = [1, 2, 3, 4, 5]

# for number in numbers:
#     print(number)

# print(number)

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

# for i in range(len(menus)):
#     print(menus[i])
# menus의 수량이 변해도 유동적으로 맞춰 반복되도록 설정함

# for idx, menu in enumerate(menus):
#     print(idx, menu)

# enumerate : menus 항목 하나하나와 index 0,1,2... 도 함께
# idx, menu = (0, '라면') ★ 변수가 2개 인덱스/값

# 1.2.3 dictionary 반복

info ={
   'name': 'hyk',
   'location': 'seoul',

}

for i in info:
    print(i)
    print(info[i])
# 반복문으로 출력 시 key가 출력됨

# 1. dictionary (key 반복)

for key in info:
    print(key)

print('---')

# 2. key 반복
for key in info.keys():
    print(key)
print('---')
#키들을 반복한다고 keys()가 적혀있어 보다 명확함

# 3. value 반복
for value in info.values():
    print(value)
print('---')

# 4. key, value 반복
for key, value in info.items():
    print(key, value)

#풀어서 쓰기
for (key, value) in [   ('n', 'c'), ('l', 's')  ]:
    print(key, value)
#튜플 안이 반복작업된다는 것이 아니라
# ( n , c ) 이 덩어리 째로 for 문돌아가는데, 분해되어 할당됨

# 이전에 튜플 설명 시 2개의 변수에 각각 따로 할당할 수 있다고 설명했었음
# b, c = (1, 2) <=이거
# b에 1, c에 2를 순서대로 할당함


print(info.keys())
# keys 사용 시 키들을 모두 모은 객체(이경우 리스트)를 하나 만들어 반복문을 돌리게 됨
print(info.items())
# 이것도 리스트가 만들어지는데, 리스트 안에 튜플()이 만들어짐   [  (키 밸류), (키 밸류)  ]


# 딕셔너리의 경우 반복문 돌린다면 전체를 다 돌리거나, 필요한것을 선택적으로 접근하기 때문에 딕셔너리의 순서는 중요하지 않음


# 연습
blood_type = {
    'A': 10,
    'B': 8,
    'O': 5,
    'AB': 5,
}

# 1. 혈액형 종류는 다음과 같습니다. A, B, O, AB  (딕셔너리 키 목록 출력)
# 2. 혈액형 종류는 다음과 같습니다. A, B, O, AB (key)
# 3. 학생수느 28명 입니다.
# 4. A형은 10명입니다, B형은~ 

# 1, 2번 ,keys() 있고 없고 차이이지만 keys()사용하는 것을 권장
result = []
for key in blood_type.keys():
    result.append(key) #리스트에 연이어서 넣기
result = ', '.join(result)
print(f'혈액형 종류는 다음과 같습니다. {result}')
# 파이썬의 (거의) 모든 것은 객체. 객체는 어떤 실행할 수 있는 기능을 가진 것. 기능은 메소드.

# 3.
result = 0
for value in blood_type.values():
    result = result + value
    #result += value
print(f'학생수는 {result}명 입니다.')

# 4.
for k, v in blood_type.items(): # k와 v는 for문안에서만 쓰는 임시 변수이름이기 때문에 어떻게 이름지어도 괜찮
    print(f'{k}형은 {v}명입니다.')


# 1.2.4 break

# for i in range(10):
#     print(i)
#     if i > 2:
#        print('2보다 크니까 break로 끝냅니다')
#        break
# print('---')
# 연습
#보리는 출력, 쌀이 나오면 잡았다고 하고 멈춤
rice = ['보리', '보리', '보리', '쌀', '보리', '보리']

for r in rice:
    if r =='쌀':
        print('쌀 잡았다!')
        break
    print(r)
# alt + 방향키 > 코드 위치 위아래 변경
print(type(r)) # r값은 rice의 str값
print('---')
# 1.2.5 continue
for i in range(5):
    if i % 2: #2로 나눈 나머지가 1이면 True
        continue # 이아래는 스킵, 다음 for문 반복 계속진행
    print(f'{i}는 짝수입니다.')
print('---')
# 연습
age = [6, 10, 30, 20, 60, 4]
# 20살 이상이면 '성인입니다', 미만이라면 아무것도 X

for a in age:
    if a >= 20:
        print(f'{a}살 성인입니다')
        continue
print('---')

for a in age:
    if a < 20:
        continue
    print(f'{a}살 성인입니다')
print('---')


# 1.2.6 else (for 문에서의 else)

for i in range(50):
    print(i)
    if i == 1:
        print(f'{i}번째에서 break')
        break

else:
    print('break를 만나지 않았습니다')
print('---')

# 연습
numbers = [1, 5, 10]
print(5 in numbers)
print('---')

# for/else 문으로 numbers를 반복하면서 특정 숫자가 있으면 True, 없으면 False출력
my_number = 1
for n in numbers:
    if n == my_number:
        print(f'True / {n} 있습니다. ')
        break
else: # for문의 끝까지 다 확인했으나, if문에 거치는 경우가 없어서 else 실행
    print(f'False / {my_number} 없습니다.')

# 1.2.7 match
# 다른 언어에서의 case문