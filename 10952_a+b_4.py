import sys

# 첫번째 val 입력 받기
val = sys.stdin.readline()

while True:
    # val 입력이 멈추면 break
    if val == '':
        break
    
    # 계산
    a, b = val.split()
    a = int(a)
    b = int(b)

    # 결과 출력
    print(a + b)

    # 다음 테스트 케이스 입력 받기
    val = sys.stdin.readline()
