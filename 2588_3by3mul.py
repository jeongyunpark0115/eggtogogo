# 세 자리 수 a * 세 자리 수 b 과정에서
# 정수 a와 b가 주어질 때

# a * (b의 일의 자리 수)의 결과
# a * (b의 십의 자리 수)의 결과
# a * (b의 백의 자리 수)의 결과
# a * b의 값

# 네 개의 수를 차례대로 출력하라
# 예제 입력
# 472
# 385

a = int(input())
b = str(input())

b1 = int(b[2]) # b의 일의 자리 수
b2 = int(b[1]) # b의 십의 자리 수
b3 = int(b[0]) # b의 백의 자리 수
int_b = int(b)

print(a * b1)
print(a * b2)
print(a * b3)
print(a * int_b)




