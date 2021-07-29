# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

num = int(input())
result = 1

# 1부터 num까지 for 문을 돌면서
for i in range(1, num + 1):
    # 0!의 값은 1
    if num == 0:
        print(result)
    # 그 외의 N값이 주어졌을 때
    else:
        # 1 * ... * num 값을 구한다
        # 팩토리얼 값 result는 전단계까지 곱해진 수의 값에다 다음 단계 수를 곱한 것
        result = result * i
        i = i + 1

print(result)

# 범위를 설정하는 거랑 수식 (result = result * i) 찾는 게 좀 힘들었지만 프로그램 여러번 돌리면서 나오는 값을 보고 제대로 풀었다.

# for 문을 제출해서 통과하긴 했으나 생각해보니 재귀로 풀어야되서 코드를 다시 짰다.
# 재귀가 정확하게 뭔지 모르겠어서 코드를 찾아봤다.
# 재귀함수란 함수 자기 자신을 호출하는 함수다.
n = int(input())

def factorial(n):
    result = 1
    if n > 0:
        result = n * factorial(n-1)
    return result

print(factorial(n))