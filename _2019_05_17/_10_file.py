# 파일 입출력

# 파일 생성됨
f = open("새파일.txt", 'w') # w 는 readstream 생성한 것
f.close()

# 파일에 기록하기
f = open("print.txt", 'w', encoding="utf-8")
for i in range(10):
    f.write("%d번째 줄입니다\n" % i)
f.close()

# 파일을 한 줄 읽기 (첫 줄 하나만 출력)
print("파일의 첫 한 줄 읽기")
f = open("print.txt",'r', encoding="utf-8")
line = f.readline()
print(line)
f.close()

# 파일을 여러 줄 읽기
print("파일을 여러번 읽기")
f = open("print.txt",'r', encoding="utf-8")
while True:
    line = f.readline()
    if not line:
        break
    print(line, end='')

f.close()

# 파일 여러 줄 읽기
print("파일을 여러번 읽기(end=''를 추가)")
f = open("print.txt",'r', encoding="utf-8")
lines = f.readlines()
print(lines)
for i in lines:
    print(i, end='')
f.close()


# 파일을 한 번에 읽기
print("파일을 한 번에 읽기")
f = open("print.txt",'r', encoding="utf-8")
data = f.read()
print(data)
f.close()

#기존 파일에 새로운 내용 추가
f = open ("print.txt", 'a', encoding="utf-8")
for i in range (10,15):
    f.write("%d번째 줄입니다\n"  % i)
f.close()

# with문 사용하기
# open 후에 close 해야한다는 사실이 개발자들을 불편하게 했다
# 그래서 with 문을 사용하낟
# with 문을 사용하면 자동으로 close 가 호출된다
with open("foo.txt", 'w', encoding="utf-8") as f:
    f.write("Life is too short, You need Python!!") # 끝나면 자동으로 f.close()가 호출
