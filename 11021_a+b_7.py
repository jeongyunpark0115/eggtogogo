import sys

t = int(input())

aa = []
bb = []

for i in range(1, t + 1):
    a, b = sys.stdin.readline().split()
    a = int(a)
    b = int(b)

    aa.append(a)
    bb.append(b)

    result = "Case #%d:"%i
    summation = aa[i-1] + bb[i-1]
    print(result, summation)

    i += 1