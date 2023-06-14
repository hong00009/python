# print(dir('1'))
# 1. 문자열 메소드

# .capitaliae()
greeting = 'hello my NAME is ...'

# print(greeting)
# print(greeting.capitalize())
# greeting.capitalize()
# greeting 이 가지고 있는 기능// . 찍어 호출하는 함수 = 메소드 라고 부름
# 문자열은 immutable 직접 수정은 불가하므로 "문자열.메소드"를 통해

# .title()
# print(greeting.title())

# .uppter()
# print(greeting.upper())

# .join(interable)
a = ['hi', 'my', 'name']
# print('!!'.join(a))

# .replace(old, new[, count])
# 세번째 인자 [] 대괄호는 옵션, 넣어도 안넣어도 되는 값
# print('woooooow'.replace('o', '!', 3))

# .strip([chars])
str_l = '          hello \n'
str_r = 'hellohihihihihi'
# print(str_l.strip()) #개행 포함 모든 공백 삭제
# print(str_l.lstrip()) #왼쪽만
# print(str_r.rstrip('hi')) # 오른쪽

# .find(x)
a = 'apple'
# print(a.find('l')) # 0.1.2.3번째
# print(a.find('p')) # 0.1번째 / 제일 처음 발견한 값
# print(a.find('z')) # 없으면 -1
# print('----')

# .index(x)
# print(a.index('a'))
# print(a.index('z')) # 찾는 값이 없으면 에러가 발생함
# find와 index 기능은 같으나
# 찾는 값이 없어도 실행되어 -1표기하거나, 에러가 발생하는 차이
# print('----')

# .split()
a = 'my name is abcde'
# print(a.split()) #기본적으로 ' '공백을 기준으로 잘라 리스트화
a = 'my_name_is_abcde'
# print(a.split('_'))

# print('----')

# .isXXX() = > 이렇게 생긴 함수는 True, False 반환



# 2. 리스트 메소드
# 메소드를 통해 원본 자체가 수정됨
# 리스트는 mutable한 객체이기 때문.

numbers = [5, 5, 5, 1, 2, 3, 4, 5, 5, 5, 5]

# .append(x)
numbers.append(6)
# print(numbers)
# print('----')

# .extend(iterable) # iterable 반복가능한 인자 받음
ex_numbers = [99, 100]
numbers.extend(ex_numbers)
# print(numbers)
# print('----')

# .insert(i, x)
numbers.insert(3, 3.5)
# print(numbers)
# print('----')


# .remove(x)
numbers.remove(3.5)
# print(numbers)
# print('----')

# .pop(i)
numbers.pop()
# print(numbers)
# 마지막 요소 삭제
numbers.pop(0) # 인자는 삭제할 값이 아니라 index 순서임
# print(numbers)
# print('----')

# .index(x)
# print(numbers)
# print(numbers.index(3))

# .count(x)
# print(numbers.count(5))

# .sort()
# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)

# .reverse()
numbers.reverse()
# print(numbers)
# 정렬은 아니고 앞/뒤 순서를 바꿈 

# copy 같은 주소를 참조
origin_list = [1, 2, 3]
copy_list = origin_list
# 리스트는 '얕은 복사'가 일어남
# = 방식으로 복사하면 리스트 위치를 가리키는 주소를 참조하도록 복사함
copy_list[0] = 100

# print(origin_list)
# print(copy_list)

# print(id(origin_list))
# print(id(copy_list)) # 둘다 id가 같음

# copy 복사 방법 
a = [1, 2, 3]
b = a[  :  ] # 첫콜론 양옆이 비어있으면 '처음'부터:'끝"까지로 설정
b = list(a) # 다른 복사 방법
b[0] = 100

# print(a)
# print(b)

# copy 얕은복사
a = [1, 2, [3, 4]]
b = a[:]
# b[2][0] = 100

# print(a)
# print(b)
# b만 변경했는데도 또 a와 b 둘다 같은 값이 출력됨
# print('----')

# copy 깊은 복사 
import copy
b = copy.deepcopy(a)
b[2][0] = 100
# print(a)
# print(b)

# .clear()
a = [1, 2, 3, 4]
a.clear()
# print(a)

# list comprehension
# 리스트 내부에 for, if문을 쓸 수 있음

numbers = list(range(1,11))
# print(numbers)

# 세제곱 만들기 for
result = []
for i in numbers:
    result.append(i**3)
# print(result)

# 세제곱 만들기 comp
result2 = [i**3 for i in numbers]
# for문돌려 나온 값을 차곡차곡 리스트값으로 순차저장
# print(result2)

# 짝수만 고르기 for
even_list = []
for i in numbers:
    if i % 2 == 0:
        even_list.append(i)
# print(even_list)

# 짝수만 고르기 comp
even_list2 = [ i for i in numbers if i % 2 == 0]
# print(even_list2)
#even_list2 = [ i | (for i in numbers if i % 2 == 0)]

# 연습
words = 'my name is hong'
vowels = 'aeiou'
# 모음만 제거 = my n m  s h ng

# for 
result = []
for char in words:
    if char not in vowels:
        result.append(char)
# print(''.join(result))

# comp
result2 = [ char for char in words if char not in vowels ]
# print(''.join(result))


# 3. 딕셔너리 메소드

info = {
    'name' : 'change',
    'location': 'seoul',
    'phone': '123-123-123',
}

# .pop(key[, default])
info.pop('phone')
# print(info)
# print(info.pop('school', 'key가없습니다'))
# print(info)

# .update(key = value)  수정하기
info.update(name ='changhee')
# print(info)

# .get(key[, default])
# print(info.get('name'))
#  == info['name']


# print(info['school']) # 없는 키는 에러
# print(info.get('school')) # 없는 키는 None

# dictionary comprehension
# {1: 1, 2: 8, 3: 27}

# 세제곱
cube_dict = {}
for i in range(1,4):
    cube_dict[i] = i**3
# print(cube_dict)

# 세제곱 comp 
cube_dict2 = {i: i**3 for i in range(1, 4)}
# print(cube_dict2)
# print('---')

# 연습
# 50이상 지역만 뽑아서 새로운 dict 만들기
dust = {
    '서울': 100,
    '대전': 12,
    '대구': 70,
    '부산': 20,
    '제주': 0,
}

# for
result ={}
for k, v in dust.items():
    if v >= 50:
        result[k] = v # ★★딕셔너리에 값을 저장하는 방법 몰랐음

# print(result)

# comp
result2 = {k: v for k, v in dust.items() if v >= 50}
# print(result2)

result3 = { k: '나쁨' if v >= 50  else '좋음' for k, v in dust.items() }
# print(result3)

# { k:  ## 키
# ('나쁨' if v >= 50  else '좋음' ) ## 밸류, 삼항연산자
#  for k, v in dust.items() } ## dictionary comp 식
# print('---')

# 4. 세트 메소드
# 집합, 중복데이터 없음
# 세트와 딕셔너리는 정해진 순서가 없음, print시 뒤섞여나올 수 있음
fruits = {'apple', 'banana', 'melon'}

# .add()
fruits.add('water melon')
fruits.add('water melon') #두번 실행해도 중복값이 없어 1회출력
# print(fruits)

# print('---')

# .update(*objects)
fruits.update('grape') 
# 'grape'를 이터레이션 가능한 객체로 인지하여 한글자씩 쪼개서 update함
fruits.update( {'orange', 'pear'})
# print(fruits)

# .remove(x)
fruits.remove('banana')
# print(fruits)
# fruits.remove('dog') # KeyError 'dog'는없다고 에러

# .discard(x)
fruits.discard('dog')  # 없더라도 실행되며 None 

# .pop()  # 순서가 없다보니 아무거나 임의로 꺼내지는데, 잘 쓰이지 않음
fruits.pop()
# print(fruits)


# 5. map(), zip(), filter()

# map()
# map(function, iterable)  #함수, 반복가능한 인자
number = [1, 2, 3]

number_str = map(str, number)
# map은 iterable 인자 (number) 모두 하나씩 반복문 자동으로 돌림
# print(number_str)
# print( list(number_str))

# print('---')

def cube(x):
    return x**3

cube_list = list(map(cube, number))
# print(cube_list)

# "1 2 3 4 5 6 7 8 9 10" 입력시 3제곱한 리스트 만들기
# => 1, 8, 27 .... ~ 1000

# 입력받은 값은 str형 이므로 [1, 2, 3 ... ] 리스트로 만들어야함
# numbers = input().split()
# result = map(int, numbers)
# print(numbers)
# print(type(numbers))
# print(list(result))

# numbers = list(map(int, input().split())) 
# 축약, 굉장히 자주씀, 받은 값을 쪼개서 int값으로된 list로 만들겠다
# print(numbers)

# print('---')

# zip
a_number = [1, 2, 3]
b_number = [100, 200, 300]
# print(list(zip(a_number, b_number)))
# [(1, 100), (2, 200), (3, 300)]

# print('---')

# filter(function, iterable)
# 단, 이곳의 function은 참/거짓이 반환되는 함수여야함
# 자체적으로 반복문을 돌면서 조건에 맞으면 넣고, 맞지 않으면 안넣음
def isodd(x):
    if x % 2 == 1:
        return True
    else:
        return False
    
def isodd(x):
    return bool(x % 2) # 축약, 0이면 False, 1이면 True 자동처리

numbers = [1, 2, 3, 4, 5]
result = filter(isodd, numbers)
# print(list(result))