# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

n = int(input())

# 합 초기화
sigma = 0

# 1 부터 n 까지
for i in range(1, n + 1):
    sigma = sigma + i
    i += 1

print(sigma)