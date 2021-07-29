import sys

# 첫번째 val 입력 받기
val = sys.stdin.readline()

# 입력이 있는 동안
while val != '':
    # 계산
    a, b = val.split()
    a = int(a)
    b = int(b)

    # 만약 0 0이 입력으로 들어오면 프로그램 끝내기
    if a == 0 and b == 0:
        break

    # 결과 출력
    print(a + b)

    val = sys.stdin.readline()
