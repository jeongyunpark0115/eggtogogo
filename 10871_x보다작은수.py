# 첫째 줄에 n과 x과 주어진다. (1 <= n, x <= 10,000)
n, x = input().split()
n = int(n)
x = int(x)

# 둘째 줄에 수열 A를 이루는 정수 n개가 주어진다.
a = input().split() # 리스트 a 안에 문자열 원소들

nums = []
num = 0
i = 0

# 문자열로 받은 수열을 하나씩 꺼내어 정수로 바꿔 다른 리스트 nums에 넣어주기
for i in range(len(a)):
    num = int(a[i])
    nums.append(num)
    i += 1

result = []

# nums 리스트에서 인덱스 0 부터 n-1까지 돌면서
# x보다 작은 수를 result 리스트에 넣어주기
for i in nums:
    if x > i:
        result.append(i)

# result 리스트에서 원소를 차례대로 출력하기
for i in result:
    # end= " "는 새로운 라인을 만드는 대신 " "으로 연결해준다.
    print(i, end=" ")