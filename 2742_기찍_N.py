n = int(input())

nums = []

for i in range(1, n + 1):
    nums.append(i)
    i += 1

for j in range(len(nums)):
    print(nums.pop())
    j += 1