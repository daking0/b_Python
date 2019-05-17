# 예외처리
# 예외처리는 예상치 못한 또는
# 예외가 발생할 것이라고 예측되는 부분에 처리함으로써
# 프로그램을 중단할 것인지
# 아니면 예외의 원인을 알려주고 진행시킬 것인지
# 결정하는 프로그램에서 매우 중요한 문법이다

# f = open("empty.txt", 'r')
# result = f.read()
# f.close()

# 잘못된 수식
#print(4/0)

# 인덱스 범위 아웃
# a = [1.2,3]
# print(a[4])

def line(num=30):
    print('*' * num)

# try-except 문
try:
    print(4/0)
except ZeroDivisionError as e:
    print("예외 발생")
    print(e)
print("end")
line()

try:
    f = open("empty.txt", 'r')
    # f= open("foo.txt", 'r')
except FileNotFoundError as e:
    print(e)
else: #예외가 발생하지 않으면 실행
    data = f.read()
    print(data)
    f.close()

f = open("foo.txt", 'r')
try:
    result = f.read()
    print(result)
except FileNotFoundError as e:
    print(e)
finally: # 예외 발생 여부와 상관없이 무조건 실행
    f.close()

# 예외 일부러 발생시키기
# Java: throw ne Exception("에러~")

class Bird:
    def fly(self):
        raise  NotImplementedError

eagle = Bird()
eagle.fly()