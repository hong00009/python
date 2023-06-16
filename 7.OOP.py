# 객체지향 프로그래밍
# - 클래스 (Class) : 같은 종류의 집단에 속하는 속성(attribute)과 행위(method)를 정의한 것
# 데이터 - 기능 / 변수 - 함수 / 속성 - 행위
# - 인스턴스(instance) : 클래스를 실제로 메모리상에 할당한 것
# 붕어빵 틀은 붕어빵을 만들기 위한 도구, 붕어빵 자체는 아님
# 클래스는 이렇게 만드는거야! 하고 정의한 기계 (선언), 인스턴스는 현실에 존재하는 것, 만들어진 결과 (실행)
# - 속성(attribute) : 클래스/인스턴스가 가지고 있는 데이터/값
# - 행위(method) : 클래스/인스턴스가 가지고 있는 함수/기능

number = 1 + 2j
# print(type(number))  # <class 'complex'>   class로 정의됨

# print(number.real)
# print(number.imag)
# 실수와 허수에 접근할 수 있도록 한 어트리뷰트 real과 imag

my_list = [1, 2, 3]
my_list.sort()
# . 점을 찍고 ()괄호, 기능사용. 정렬하는 메소드
# print(type(my_list))
# <class 'list'> list를 통해 만들어진 하나의 인스턴스

# 클래스가 없다면
power = False
number = '010-1234-1234'
book = {
    '홍길동': '010-432-4321',
    '이순신': '010-567-5678'
}
model = 'iPhone12'

def on():
    global power
    if power == False:
        power = True
        print('핸드폰이 켜졌습니다.')

def off():
    global power
    if power == True:
        power = False
        print('핸드폰이 꺼졌습니다')

def set_my_number(n):
    number = n

# on()
# off()
# cannot access local variable 'power' where it is not associated with a value
# global power 로 전역변수 접근 처리


# 클래스
# class ClassName:
#   attribute
#   method

# 클래스이름은 PascalCase로 앞글자부터 대문자로

# 클래스 선언
class TestClass:
    a = 1   # attribute
    
    def b(self):   # method
        print('b')

# 인스턴스화
class_a = TestClass()
# 인스턴스화 이후 기능과 데이터를 사용할 수 있음

# print(class_a.a)
# class_a.b()


# 클래스가 있다면
# 정의 만들기
class Phone:
    # 기본값들
    power = False
    number = '010-000-0000'
    book = {}
    model = ''
    
    def on(self):
        if self.power == False:
            self.power = True
    # self / 추후 인스턴스화 될 그것 자체를 의미

    def off(self):
        if self.power == True:
            self.power = False

    def call(self, target):
        if self.power == True:
            print(f'내 번호는 {self.number}')
            print(f'{target} 전화 거는중')
        else:
            print('핸드폰 전원을 켜주세요')

my_phone = Phone()
# 인스턴스화
your_phone = Phone()

# my_phone.on()
# my_phone.power = True
# print(my_phone.power)
# print(your_phone.power)
# my_phone.number = '010-999-9999'
# my_phone.call('010-1111-1212')
# your_phone.call('010-2222-2222')

p1 = Phone()
Phone.on(p1)
# == p1.on() 
# print(p1.power)

# 연습
class MyList:
    data = []
    def append(self, item):
        self.data += [item]
        # self.data = self.data +[item]
        #나 자신이 가지고 있는 data속성에 접근하여

    # data안 맨 마지막 요소를 삭제하고, 삭제된 요소 하나를 리턴
    def pop(self):
        v = self.data[-1] 
        self.data = self.data[:-1]  # 첫번째부터 -1번째까지 잘라 덮어씌우기
                                    # [7, 8, 9] 라면 8까지만
        return v
        


list_a = MyList()
# print(list_a.data)
# list_a.append(123)
# list_a.append(456)
# list_a.append(789)
# print(list_a.data)

# print(list_a.pop())
# print(list_a.data)

# 정리
class Person:   # => 클래스 정의(선언) : 클래스 객체 생성
    name = 'hong'   # => 속성(attribute) : 변수/값/데이터

    def hello(self):   #  => 행동(method) : 함수/기능
        return self.name
    
p = Person()    # => 인스턴스화 / 인스턴스 객체를 생성 

p.name  #   => 속성을 호출 
p.hello()   # => 메소드 호출

# 6/16
# self : 인스턴스 객체 자기자신 (다른언어에서는 this)
#       - 특별한 상황을 제외하고는 무조건 매소드의 첫번째 인자로 설정
#       - 인스턴스 매소드를 실행할 때 자동으로 첫 번째 인자에 인스턴스를 할당한다

# 1)
p1 = Person()
p1.hello()

# 2)
Person.hello(p1)

# 1)과 2) 2개는 같은 기능을 함

p2 = Person()
# print(p1.name)  # p1은 인스턴스화만 되고 내용물은 없어 Person 클래스의 기본값이 나옴
p2.name = 'kim'
# print(p2.name)


# 생성자, 소멸자
# 매직 매소드, 특정한 조건에 자동으로 파이썬이 실행하는 매소드
# 초기값을 설정해야 할때 __init__(self, ...) 을 사용하여 설정함

# def __init__(self):
#   print('생성될 때 호출되는 매소드')

# def __del__(self):
#   print('소멸될 때 호출되는 매서드')

class Person():   # <- () 상속을 위해 괄호
    name = ''

    def __init__(self, name):
        self.name = name
        # print('생성됨')
    
    # def __del__(self):
    #     print('소멸됨')
    #     # 소멸자는 잘 사용하지는 않음

p1 = Person('eeee')
# 위 코드는 이런 의미로 동작함 Person.__init__(p1, 'eeee') 

# del p1 #정의된 변수/함수를 지우는 키워드 del

# print(p1.name)

p2 = Person('Lee')
# print(p2.name)


# 연습 1
class Pikachu:
    def __init__(self, name='pikachu'): # 이름짓기, 안지으면 그냥 피카츄
        # 시작할때 설정할 값
        self.name = name
        self.level = 1
        self.hp = self.level * 100

    def attack(self, opponent):
        damage = self.level * 5 #내 레벨의 5정도 공격수치
        opponent.hp -= damage

p1 = Pikachu() # 그냥 생성
p2 = Pikachu('chu') # 츄라는 이름으로 생성

# p1.attack(p2)
# print(p1.hp, p2.hp) # hp 깎임

# 연습 2 
# Circle 클래스

# 속성
# pi : 원주율 (3.14)
# 인스턴스 속성
# r : 반지름 (필수입력)
# x : x 좌표 (default = 0)
# y : y 좌표 (default = 0)

# 매소드 
# area() : 원의 넓이를 반환
# center() :원의 중심을 (x, y) 튜플로 반환
# move(x, y) : 원의 중심을 (x, y)로 변경

class Circle:
    pi = 3.14 # 공공재 같은 개념
 

    def __init__(self, r, x=0, y=0):
        self.r = r
        self.x = x
        self.y = y
        
    def area(self):
        return self.r**2 * Circle.pi  # CIrcle 클래스내부 pi 변수에 접근
    
    def center(self):
        return (self.x, self.y)
    
    def move(self, x, y):
        self.x = x
        self.y = y
        print(f'원의 중심이 ({x}, {y})로 이동했습니다.')

c1 = Circle(5, 10, 10)
# print(c1.r, c1.x)
# print(c1.center())
# print(c1.area())
# c1.move(2,2)


# 클래스 변수
# - 클래스 선언 블록의 최상단에 위치함
# - ClassName.class_variable 로 접근/할당함

# 인스턴스 변수
# - self.instance_variable 로 접근/할당함


class TestClass:
    class_variable = '클래스변수'

    def __init__(self, arg):
        self.instance_variable = arg

    def status(self):
        return self.instance_variable
    
t1 = TestClass('인스턴스변수')
# print(TestClass.class_variable)
# print(t1.class_variable) # 기본적으로 본인의 cv가 없기 때문에, 상위 정의(TC)로 찾아가 cv를 출력함

# print(t1.instance_variable)


# instance method
# class ClassName:
#   def func():
#       pass

# class method
# class ClassName:
#   @classmethod     #이부분에 @(데코레이터)와 함께 표기
#   def func():
#       pass

# static method
# class ClassName:
#   @staticmethod   #이부분에 @(데코레이터)와 함께 표기
#   def func():
#       pass


class MyClass:
    
    def instance_method(self):
        return self
    # self / 이 클래스로 인스턴스화한 후 그 인스턴스 자체를 가리킴

    @classmethod
    def class_method(cls):
        return cls
    # cls는 해당 클래스 자체를 가리킴, 클래스변수 등 클래스 자체의 값 활용
    # 클래스메소드의 기본인자는 항상 cls로 설정
    # 개인적으로는 쓸일이 별로 없음
    
    @staticmethod
    def static_method(arg):
        return arg
    # 클래스변수, 인스턴스 변수 다 필요없이 그냥 작동할때 사용
    # 인자가 없을 수 있고, self 필요없음.
    # 개인적으로는 쓸일이 별로 없음

m1 = MyClass()
# print(m1.instance_method())
# print(m1.class_method()) # MyClass 형태라고 출력
# print(MyClass.class_method()) # 위 코드는 이것과 같은 뜻
# print(m1.static_method('hello'))



# 연습
class Puppy:
    num_of_dogs = 0  # 클래스변수
    
    def __init__(self, name):
        #처음에는 강아지 이름만 설정
        self.name = name
        Puppy.num_of_dogs += 1

    @classmethod
    def get_status(cls):
        return f'현재 강아지는 {cls.num_of_dogs}마리 입니다.'
    
    @staticmethod
    def bark():
        return '멍멍'

p1 = Puppy('인절미')
p2 = Puppy('초코')
# print(Puppy.num_of_dogs)
# print(Puppy.get_status())
# print(p1.bark())
# print(p2.bark('그르릉'))


class Person:
    population = 0
    def __init__(self, name):
        self.name = name
        Person.population += 1
        # 인스턴스화 되어 한명의 사람이 만들어지면 인구수 증가

    def greeting(self):
        print(f'안녕하세요 {self.name}입니다')

p1 = Person('홍길동')
# p1.greeting()


# 다른 클래스의 기능을 모두 가져오고 싶다면 상속

class Student(Person):
    def __init__(self, name, id):
        self.name = name
        self.id = id
        Person.population +=1

# 둘다 init이 있다면, 상속받은 init이 실행되고 원본 init은 실행안함 / overriding
# 우선적으로 내꺼부터 찾고, 없을 경우 상위를 찾기 때문

s1 = Student('이순신', '12345')
# s1.greeting()  
# Student 클래스에는 greeting()이 없으므로, 상속된 Person에서 찾아 실행함

# print(Student.population)

class Soldier(Person):
    # method overriding
    # 메소드 이름이 겹쳤을 때는, 가장 가까운곳(내꺼) 부터 호출
    def greeting(self):
        print('충성!')

s2 = Soldier('국방이')
# s2.greeting()


# 다른 예제

# super
class Person():
    def __init__(self, email, phone, location, name):
        self.email = email
        self. phone = phone
        self.location = location
        self.name = name

class Soldier(Person):
    def __init__(self,email,phone,location,name,id):
        super().__init__(email,phone,location,name)
        #상속 원본부터 강제로 먼저 실행하여, 중복되는 기능 처리
        #이후 soldier에만 추가된 기능만 적으면 됨
        self.id = id


# 다중상속

class Person():
    def __init__(self, name):
        self.name = name
    def breath(self):
        print('후하')

class Mom(Person):
    gene = 'XX'

    def swim(self):
        print('어푸어푸')
    def greeting(self):
        print('안녀어어어엉')

class Dad(Person):
    gene = 'XY'
    
    def run(self):
        print('다다다')
    def greeting(self):
        print('안녕!!')

class FirstBaby(Mom, Dad):
    pass
b1 = FirstBaby('첫째')
# b1.swim()
# b1.run()
# print(b1.gene) # XX
# b1.greeting()  # 안녀어어엉


class SecondBaby(Dad, Mom):
    pass

b2 = SecondBaby('둘째')
# b2.breath()
# b2.run()
# print(b2.gene)  # XY
# b2.greeting()  # 안녕!!

# 여러개를 상속받았을 때 중복되는 것(변수/함수)이 있다면 항상 맨앞에 상속받은 쪽의 Class로 작동함

import random

class Pocketmon():
    def __init__(self):
        self.level = 1
        self.hp = self.level * 5
        self.exp = 0
        self.status ='normal'

    def attack(self, opponent):
        damage = self.level * 2
        opponent.hp -= damage

        if opponent.status != 'normal':
            opponent.status = 'normal'

        if opponent.check_hp():
            self.exp += 5
 

    def sing(self, opponent):
        opponent.status = 'sleeping'


    def check_hp(self):
        return True if self.hp <= 0 else False
    
    def check_exp(self):
        if self.exp >= self.level * 5:
            self.level += 1

class Type():
    def __init__(self, type_name):
        self.type_name = type_name


class WaterPocketmon(Pocketmon):
    pass

class FirePocketmon(Pocketmon):
    pass

koboki = WaterPocketmon()
pairi = FirePocketmon()

while True:
    koboki.attack(pairi)
    if pairi.check_hp():
        break

print(koboki.exp)
print(pairi.hp)

koboki.sing(pairi)
print(pairi.status)

print(koboki.level)

while True:
    koboki.attack(pairi)
    if pairi.check_hp():
        break

print(pairi.status)