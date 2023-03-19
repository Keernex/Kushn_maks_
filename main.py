q = int(input())
w = q // 1000
r = q // 100 % 10
e = q // 10 % 10
t = q % 10
print(t * w * e * r)
