# N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며,
# 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.
# 이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다.
# 우선, 제일 위에 있는 카드를 바닥에 버린다.
# 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.

# 예를 들어 N=4인 경우를 생각해 보자. 카드는 제일 위에서부터 1234 의 순서로 놓여있다.
# 1을 버리면 234가 남는다. 여기서 2를 제일 아래로 옮기면 342가 된다. 3을 버리면 42가 되고, 4를 밑으로 옮기면 24가 된다.
# 마지막으로 2를 버리고 나면, 남는 카드는 4가 된다.

# N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.



# N개의 카드가 들어있는 배열 초기화
cards = []

# 숫자 N을 입력받기
num = int(input())

# 1부터 N까지 위에서 아래로 넣기 (0번째 인덱스가 위)
for i in range(1, num + 1):
    cards.append(i)

# 카드가 하나만 남을 때까지 아래의 과정을 반복
while len(cards) > 1:
    # 먼저 제일 위에 있는 카드를 바닥에 버린다.
    del cards[0]
    print("del: ", cards)
    # 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
    popped = cards.pop(0)
    print("pop: ", cards)
    cards.append(popped)
    print("append: ", cards)
    
print("result: ", cards)

########################################

# 아래는 제출용 코드 ### 시간 초과 됨 시밤 ㅠㅠ

# N개의 카드가 들어있는 배열 초기화
cards = []

# 숫자 N을 입력받기
num = int(input())

# 1부터 N까지 위에서 아래로 넣기 (0번째 인덱스가 위)
for i in range(1, num + 1):
    cards.append(i)

# 카드가 하나만 남을 때까지 아래의 과정을 반복
while len(cards) > 1:
    # 먼저 제일 위에 있는 카드를 바닥에 버린다.
    del cards[0]
    # 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
    popped = cards.pop(0)
    cards.append(popped)
    
print(cards[0])

########################################

# 아래는 두 번째 시도 ### 이것도 안 됨 흑흑 ㅠㅠ
import sys

# N개의 카드가 들어있는 배열 초기화
cards = []

# 숫자 N을 입력받기
num = int(sys.stdin.readline())

# 1부터 N까지 위에서 아래로 넣기 (0번째 인덱스가 위)
for i in range(1, num + 1):
    cards.append(i)

# 카드가 하나만 남을 때까지 아래의 과정을 반복
while len(cards) > 1:
    # 먼저 제일 위에 있는 카드를 바닥에 버린다.
    del cards[0]
    # 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
    popped = cards.pop(0)
    cards.append(popped)
    
print(cards[0])

########################################

# 아래는 세 번째 시도
import sys
from collections import deque

# N개의 카드가 들어있는 배열 초기화
cards = deque()

# 숫자 N을 입력받기
num = int(sys.stdin.readline())

# 1부터 N까지 위에서 아래로 넣기 (0번째 인덱스가 위)
for i in range(1, num + 1):
    cards.append(i)

# 카드가 하나만 남을 때까지 아래의 과정을 반복
while len(cards) > 1:
    # 먼저 제일 위에 있는 카드를 바닥에 버린다.
    cards.popleft()
    # 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
    cards.append(cards.popleft())
    
print(cards[0])
