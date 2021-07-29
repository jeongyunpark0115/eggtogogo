import sys

# 연산의 갯수가 첫번째 줄에 입력된다
n = int(input())
aa = []
bb = []

# 그 다음에 n개의 연산을 받으면서
for _ in range(n):
    a, b = sys.stdin.readline().split()
    a = int(a)
    b = int(b)

    # a, b 값을 각각의 리스트에 넣어준다
    aa.append(a)
    bb.append(b)

# 각 리스트의 인덱스를 이용해서 a + b 값을 출력한다.
for i in range(n):
    print(aa[i] + bb[i])