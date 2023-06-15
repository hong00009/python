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