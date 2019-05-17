# for 문
# 시작과 끝이 명확하게 반복할 때 사용
test = ['one', 'two', 'three']
for i in test:
    print(i)

def line():
    print("*" * 30)
line()

print("*" * 30)
for i in test:
    print(i, end =", ")
line()

marks = [90,25,67,45,80]
number = 0
for mark in marks:
    number = number +1
    if mark >= 60:
        print("%d번 학생 합격" %number)
    else:
        print("%d번 학생 불합격" %number)

# range() 함수
# for문과 결합해서 많이 사용된다
line()
a = range(10)
print(a, type(a))
b = list(range(10))
print(b)

line()
sum = 0
for i in range(0,10):
    print(i, end=" ")
    sum = sum + i;
print("sum: "+str(sum))
print("sum: ",sum)

# 구구단
line()
for i in range(2,10):
    for j in range (1,10):
        print ("%d x %d = %d" % (i,j, i*j), end = "\t")
    print()

# 리스트에 원하는 규칙의 값을 채우기
# 3의 배수 순차적으로 10개
result = []
for i in range(1,11):
    result.append(3*i)
print(result)

line()
result = [i*3 for i in range(1,11)]
print(result)
line()

# 짝수인 3의 배수만 담고 싶다
result = [i*3 for i in range(1,11) if i%2 == 0]
print(result)
