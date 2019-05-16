# 1) python 이란?
# 1989 / 1990 네덜란드 '귀로 반 로섬'
# 크리스마스에 할 일이 없어서 프로그래밍으로 놀았다
# 이름을 좋아하는 코미디 쇼 '몬티 파이썬의 날아다니는 서커스쇼' 영국 여기서 가져왔다
#
# 파이썬 : 그리스 신화의 파르나소스 산 커다란 뱀(피톤)
#          하지만 귀도는 여기서 의미를 찾은 것이 아니다
#
# 2) 파이썬의 장점
#   - 사용분야가 많다.(보안, IOT, 빅데이터, AI, 리눅스, 클라우드, Web)
#   - Glue Language(접착제 언어)
#     C/C++/JAVA/C#/Ruby..
#   - 관련 라이브러리가 매우 많다
#   - 교육시장에서 선호
#
# 3) 파이썬의 단점
#   - 인터프리터 언어(1줄씩 기계어로 변환)
#   - 단독으로 사용시 매우 느리다

# 자료형
# 1) 정수
a = 123
print(a)
print(type(a))

# 2) 실수
a = 3.14
print(a)
print(type(a))

# 3) 복소수(실수+허수)
a = 1+2j;
print(a)
print(type(a))
print(a.real) #실수부
print(a.imag) #허수부
print(a.conjugate())  #켤레복소수

# 4) 문자열
a = "korea"
print(a)
print(type(a))
a = "k"
print(a)
print(type(a))

a = 'korea'
print(a)
print(type(a))
a = 'k'
print(a)
print(type(a))

# 5) bool
a = True
b = False
print(a)
print(type(a))
print(b)
print(type(b))

a ="""
Life is too short,
You need python...
김연아
홍길동
임꺽정
"""  #따옴표 3개 쓰면 있는 그대로 개행까지도 그대로 나온다.
print(a)