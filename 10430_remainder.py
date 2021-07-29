a, b, c = input().split() # str
a = int(a)
b = int(b)
c = int(c)

print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print(((a % c) * (b % c)) % c)
