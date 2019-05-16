# 파이썬의 (자료구조) 기본 자료형
# 1) 리스트 : list
#     순서(인덱스)가 있다
#     중복값도 허용
#     a = [1,2,3,4]
#     []에 L자가 들어있다
#     => 그래서 list
#
# 2) 튜플 : tuple
#     읽기 전용 리스트
#     순서가 있다
#     중복값도 허용
#     a = (1,2,3,4)
#     (에 t자가 들어있다
#     => 그래서 tuple
#
# 3) 셋 : set
#     집합
#     순서가 없다
#     중복도 없다
#     a = {1,2,3,4}
#     {에 S자가 들어있다
#     => 그래서 set
#
# 4) 딕셔너리 : dict
#     key : value
#     map, hash 구조
#     a = {'name':'홍길동', 'age':24}
#     순서가 없으니까 set이랑 {] 공유
#     key:value => 그러니까 dict

a = (1, 2, 3, 4)
print(a, type(a))
a = {1, 2, 3, 4}
print(a, type(a))
a = [1, 2, 3, 4]
print(a, type(a))
a = {1: '커피', 2: '치즈'}
print(a, type(a))
print('*' * 30)

# 리스트의 인덱싱
a = [1, 2, 3]
print(a)
print(a[0])
b = a[0] +a[2]
print(b)
print(a[2], a[-1])

# 리스트의 슬라이싱
a = [1,2,3,4,5]
print(a[0:3])
print(a[3:])

# 리스트 연산자
a = 'Hello'
b = 'World'
c = a + b
print(c)

a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)
c = a * 3
print(c)
print('*' * 30)

# 리스트의 수정, 변경, 삭제
# 문자열은 읽기전용
# 리스트는 수정가능
a = 'Hello'
# a[0] = 'S'
a = 'S' +a[1:]
print(a)
a = [1,2,3]
a[2] = 4
print(a)

# 리스트에서 연속된 범위의 값 수정
a = [1,2,3]
a[1:2] = ['a','b', 'c']
print(a)

# 리스트 요소 삭제하기
a = [1,2,3]
a[1:3] = []
print(a)

# del함수를 이용해 삭제하기
a = [1,2,3,4,5]
del a[1]
print(a)

# 리스트에 추가하기
a = [1,2,3]
a.append(4)
a.append(5)
a.append('홍길동')
a.append(3.14)
print(a)

# 리스트의 정렬
a = [5,1,3,2,3,6,9]
a.sort()
print(a)
a.reverse()
print(a)

# 리스트 요소값 위치 반환
a = [1,2,3,4,5]
print(a.index(3))
print(a.index(1))

# 리스트에 요소 삽입
a = [1,2,3,4,5]
a.insert(0,4) # 0 위치에 4 삽입
print(a)
a.insert(3,7)
print(a)

# 리스트 요소 제거
a = [1,2,3,1,2,3]
a.remove(3) # 처음 만난 3을 제거한다
print(a)
a.remove(3)
print(a)

# 리스트 요소 꺼내기
# 가장 나중에 추가된 요소를 꺼내서 반환 후 삭제한다.
a = [1,2,3]
print(a.pop()) # 3
print(a)       # [1,2]
a = [1,2,3,4,5]
print(a.pop(1)) # 2
print(a) #[1,3,4,5]

# 리스트에 포함된 요소의 개수 세기
a = [1,2,3,1,2,1]
print(a.count(1))
print(a.count(2))

# 리스트 확장
a = [1,2,3]
a.extend([4,5])
print(a)

a = [1,2,3]
b = [4,5]
a = a + b
print(a)

# 튜플(tuple)
# 읽기 전용 리스트
# (삽입, 삭제, 수정 X)

a = (1,2,3)
print(a, type(a))
b = 1,2,3 #괄호 생략 가능
print(b, type(b))

a, b = 10, 20 #(a,b) = (10,20)
print(a,b)
a,b = b, a
print(a, b)

# 튜플의 값을 삭제 시도
a = (1,2,3,4)
#del a[0] #예외 발생
# a[0] = 10
# 변환 가능한 걸로 강제 형변환 후 다시 tuple로 형변환
a = list(a)
a[0] = 10
a = tuple(a)
print(a)

# 튜플도 인덱싱, 슬라이싱 잘된다
# 튜플 더하기
a = (1,2,3)
b = (4,5,6)
c = a + b
print(c)

# 튜플 곱하기
a = (1,2,3)
print(a * 3)


# 셋(set)
# 집합
# 합집합, 교집합, 차집합
# 순서가 없고, 중복불가능
s1 = {1,2,3}
print(s1,type(s1))

# 합집합
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s3 = s1.union(s2)
print(s3)
s4 = s1 | s2
print(s4)

# 교집합
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s3 = s1.intersection(s2)
print(s3)
s4 = s1 & s2
print(s4)

# 차집합
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s3 = s1.difference(s2)
print(s3)
s4 = s1 - s2
print(s4)

# 값 추가하기
a = {1,2,3}
a.add(4)
print(a)

# 값 여러개 추가하기
a = {1,2,3}
a.update({4,5})
print(a)

# 특정 값 제거하기
s1 = {1,2,3}
s1.remove(2)
print(s1)
print('*' * 30)

# 리스트 <-> 튜플 <-> 셋의 상호변환
a = [1,2,3,4,3,1]
print(a, type(a))
b = set(a)
print(b, type(b)) # 중복값은 삭제되고 나옴
c = tuple(b)
print(c, type(c))
d = list(c)
print(d, type(d))
d[0] = 10
print(d, type(d))