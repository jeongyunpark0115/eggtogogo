import sys

# t stands for the number of testcases given as the first input
t = int(input())

# each testcase has two numbers, k and n (1 <= k, n <= 14)
T = t * 2
testcases = []

# for the range of 2t(T), add each number in the testcases array
for _ in range(T):
    input = int(sys.stdin.readline())
    testcases.append(input)
    
