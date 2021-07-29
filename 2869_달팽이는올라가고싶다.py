# 낮에 달팽이가 올라가는 거리 A 미터
# 밤에 미끄러지는 거리 B 미터
# 높이가 V 미터인 나무 막대
# 정상에 올라간 후에는 미끄러지지 않음

a, b, v = map(int, input().split())

# 도착시까지 낮에 올라가는 총 거리 - 도착 전날 밤까지 미끄러지는 총 거리
# 가 정상 높이보다 크거나 같을 때를 찾는다.
# a * days - (b * (days - 1)) >= v
# days를 x로 치환하면
# ax - bx + b >= v
# ax - bx >= v - b
# 이를 x에 관한 식으로 만들면
# x(a - b) >= v - b
# x >= (v - b) / (a - b)

days = (v - b) / (a - b)

# 만약 days 가 자연수일 경우, 즉 xxx.0 일 경우 그대로 정수형 값을 출력해주고
if (days - int(days) == 0):
    print(int(days))

# days가 자연수가 아닐 경우, 즉 xxx.25 이런 식으로 소숫점 값이 있을 경우 올림 해서 출력
else:
    print(int(days) + 1)