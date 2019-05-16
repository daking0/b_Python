# 문자열 인덱싱
a = "Life is too short, Youd need Python"
print(a[3]) # e
print(a[12]) # s
print(a[-1]) # n
print(a[-2]) # o

# 문자열 슬라이싱
# 앞은 포함, 뒤는 이전
print(a[0:4]) # 0부터 3까지 Life
print(a[0:3])  # Lif
print(a[8:11]) # too
print(a[19:]) # 19부터 ~ 끝
print(a[:17]) # 처음부터 ~ 17 이전
print(a[:]) # 전체 문자열

a = '20190516Sunny'
print("date: " + a[:8]) # 20190516
print("weather: " +a[8:]) # Sunny
year = a[:4]
day = a[4:8]
weather = a[8:]
print("year: " + year)
print("day: " + day) # 20190516
print("weather: " + weather) # Sunny

# 문자열 포맷팅
s = "I eat %s apples." % 3  # s는 모든걸 다 받는다
print(s)
number = 10
day = 'three'
s = """
I ate %s apples.
so I was sick for %s days.
""" % (number, day)
print(s)


s = """
I ate {0} apples.
so I was sick for {1} days.
""" .format(number, day)
print(s)

# 문자열 함수
s = "Hello Python"
print(s, type(s))

# 문자 개수 세기
print(s, type(s))

# 문자 개수 세기
print(s.count('l')) # l이라는 문자 몇 개야
print(s.count('e'))

# 문자 위치 알려주기
print(s.find('P'))
print(s.find('k')) # 없는 건 -1
print(s.index('P')) #
#print(s.index('k')) # 예외 발생

# 문자 삽입
a = ","
b = a.join('abcd')
print(b)

# 대소문자 바꾸기
a = 'hi'
b = 'HI'
print(a.upper())
print(b.lower())

# 왼쪽 공백 지우기
a = ' hi'
print('Hi' + a)
print('Hi' + a.lstrip())

# 오른쪽 공백 지우기
a = 'hi '
print(a + "Fine Thank You")
print(a.rstrip() + "Fine Thank You")

# 양쪽 공백지우기
a = " hi "
print('***' + a + '***')
print('***' + a.strip() + '***')

# 문자열 바꾸기
a = "Life is too short"
b = a.replace("short","long")
print(b)

# 문자열 나누기
a = "Life is too short"
b = a.split()
print(b)

a = 'a:b:c:d'
b = a.split(':')
print(b)