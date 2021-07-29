import sys

t = int(input())

aa =[]
bb = []

for i in range(t):
    a, b = sys.stdin.readline().split()
    a = int(a)
    b = int(b)

    aa.append(a)
    bb.append(b)

    print(aa[i] + bb[i])