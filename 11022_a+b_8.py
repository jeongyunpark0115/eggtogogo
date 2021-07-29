import sys

t = int(input())

for i in range(1, t + 1):
    a, b = sys.stdin.readline().split()
    a = int(a)
    b = int(b)
    c = a + b

    print("Case #%d: %d + %d = %d"%(i, a, b, c))

    i += 1