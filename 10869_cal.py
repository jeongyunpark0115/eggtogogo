# nums = input()
# print(type(nums)) # str

# 아래 세줄을 한줄로 정리하는 법
# nums = input().split()
# intnum = map(int, nums)
# isnum = list(intnum)

nums = list(map(int, input().split()))

a = nums[0]
b = nums[1]

print(a + b)
print(a - b)
print(a * b)
print(int(a / b))
print(a % b)