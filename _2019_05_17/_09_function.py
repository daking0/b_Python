# 함수(function)
# 1) function : 동작 후 리턴값 발생
# 2) procedure : 리턴값이 없고 동작만
# 3) method : 객체지향에서 함수 -> 차별화
#
# y = f(x)
# y = 2x + 10
#
# 토마토주스 = 착즙기(토마토)
# 오렌지주스 = 착즙기(오렌지)
#
# 식은 정해져있고, 들어가는 인자에 따라 다른 결과 도출 (식을 통해 계속 재사용 가능)
def line(num):
    print('*'*num)

def sum(a,b):
    return a+b

print(sum(1,1))
print(sum(10,10))
line(10)

def say():
    print("Hi~")

# 아무것도 없는 함수는 None 객체를 반환한다
ret = say()
print(ret) # None
line(20)


# 입력값의 개수가 정해지지 않은 경우
# 여러 개의 인자가 tuple 자료형으로 전달된다
def sum_many(*args):
    print(type(args))
    sum = 0
    for i in args:
        sum = sum + i
    return sum

print(sum_many(1,2,3,4,5))  # <class 'tuple'> 튜플이라는 자료형으로 묶여서 들어가진다
print(sum_many(1,2,3,4,5,6,7,8,9,10)) # <class 'tuple'>

def calc(a,b):
    return a+b, a-b, a*b, a/b # tuple로 한 번에 담겨진다

a,b,c,d = calc(100,50)
print(a,b,c,d)

result = calc(1000, 500)
print(result, type(result))

# 지역변수와 전역변수
a = 1 # 전역변수
def vartest(a): # 지역변수 a
    a = a +1
vartest(a)
print(a)

# 함수 내에서 전역변수 접근하기
# 1) 리턴값을 이용하기
a = 1
def vartest(a): # 전역변수가 지역변수로 들어가짐
    a = a + 1
    return a #전역변수로 나간다

a = vartest(a)
print(a)

# 2) 전역변수 키워드 사용하기
a = 1
def vartest():
    global a   # 지역 내에서 전역변수 a를 사용할게
    a = a + 1

vartest()
print(a)

