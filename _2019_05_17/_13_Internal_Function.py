# 절대값 함수 abs
print(abs(10))
print(abs(-10))

# 모든 인자가 참이면 True, 아니면 False
a = [1,2,3]
b = [1,2,3,0]
c = [1,2,3,None]
d = [1,2,3,'']
e = [1,2,3,0.0]
f = [1,2,3,()]
g = ['홍길동','아이유']
h = [1,2,3,False]
i = [0,0.0,False,'',(),[],{}]


print(all(a))
print(all(b))
print(all(c))
print(all(d))
print(all(e))
print(all(f))
print(all(g))
print(all(h))
print(all(i))