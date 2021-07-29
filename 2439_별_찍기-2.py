n = int(input())

for i in range(1, n + 1):
    print(' '*(n-1) + '*'*i)
    # print(' '*(n-1), '*'*i) 이렇게 하면 쉼표 때문에 띄어쓰기 한 칸 더 됨
    n = n - 1
    i += 1