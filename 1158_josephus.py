# 1부터 n까지 원소를 갖는 원형 큐 생성
# 원형 큐 nums 도는 동안
# k <= len(nums)이면 k - 1 출력
# k > len(nums)이면 len(nums) % (k -1) 의 결과값 출력

# n, k 입력값 받기
n, k = map(int, input().split())

# 원형큐 초기화
nums = []

# 결과값 리스트
answer = []

# 원형큐 돌아가면서 선택될 인덱스
# (7,3)이면 첫번째 picked가 3인데 얘 인덱스는 2
picked = k - 1

# 원형큐 만들기
for i in range(1, n + 1):
    nums.append(i)

for i in nums:
    if k <= len(nums):
        answer.append(nums.pop(picked))
        picked = k - 1

    elif k > len(nums):
        picked = (picked) % len(nums)
        answer.append(nums.pop(picked))
        picked = k - 1

print("<", ', '.join(str(i) for i in answer), ">", sep = '')