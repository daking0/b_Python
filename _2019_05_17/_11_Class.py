# class의 필요성
# - 함수는 무조건 무언가 결과를 보내줘야하는 등 독립성이 떨어진다
# - 함수보다는 큰 단위로 설계하기 위해서

# 클래스
#     함수는 필연적으로 외부로부터 값을 받고 다시 반환해야하는 숙명적인 구조를 가지고 있다
#     (즉, 외부와의 깊은 연결관계를 맺고 있다)
#     이것은 함수의 재사용성이 높지 않다는 것을 의미한다
#     또 함수는 기능 단위이므로 큰 프로그램의 단순묘사가 어렵다
#
#     그래서 클래스가 탄생하게 되었다
#     클래스는 스스로 필요한 것은 내장하므로 독립성을 가지게 되고
#     필드들과 메서드들을 동시에 보유하고 있으므로 보다 큰 단위의 묘사가 가능해졌다

#self == this
class Calculator:  #메서드 첫 인자는 무조건 self(자바도 있지만 생략되있다)
    def __init__(self): # 생성자
        self.result = 0 # 멤버 변수 -> 여기에 쓰면 이때 변수가 선언된 것

    def adder(self, num): # 멤버 함수(일반 메서드)
        self.result += num #생성자에서 생성된 멤버 변수를 가져와서 사용
        return self.result

cal1 = Calculator() # 이 때 __init__(cal1)으로 호출된 것
cal2 = Calculator()

print(cal1.adder(10))
print(cal1.adder(20))
print(cal2.adder(100))
print(cal2.adder(200))

#result는 객체 소속

# 클래스 변수
# 객체에 동일한 객체 변수가 없을 시 클래스 변수를 접근한다
class Academy:
    academy_name = "비트캠프" # 클래스 소속 변수
    def __init__(self,name):
        self.name = name

    def study(self, hour):
        print("%s의 %s에서 하루 %d시간 공부를 한다" % (Academy.academy_name,self.name, hour))

aca0 = Academy("신촌")
aca1 = Academy("신논현")
aca2= Academy("종로")
aca3 = Academy("강남")

aca0.study(8)
aca1.study(8)
aca2.study(8)
aca3.study(8)

# 파이썬의 클래스 변수나 객체 변수는 중간에 언제든지 만들 수 있다
# 반드시 선언부에서 안 만들어도 된다
Academy.manager = "홍다경" # 클래스 소속 변수 생성
print(aca0.manager)        # 객체 변수에 manager가 없어서 -> 클래스 변수 지칭
aca0.manager = "아이유"    # aca0의 객체 변수 생성
print(aca0.manager)        # 객체 자체 변수
print(aca1.manager)        # 클래스 소속의 변수

# 클래스의 상속
class House:
    def __init__(self,name="주인"):
        self.owner = name
    def travel(self,where):
        print("{0}가 {1}로 여행을 가다".format(self.owner, where))

house0 = House()
house0.travel("호주")
house1 = House("아이유")
house1.travel("파리")

class Hotel(House): #상속받음
    pass

house0 = Hotel()
house0.travel("독일")

class Palace(House):
    def travel(self,where,day):
        print("{0}일 동안".format(day), end=" ")
        super().travel(where) # 이게 더 좋은방식
        # House.travel(self,where) # 부모 객체 메서드

pal0 = Palace("수지")
pal0.travel("노르웨이",10)
