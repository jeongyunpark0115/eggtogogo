a, b = map(int, input().split())
print(a + b)

# 숫자가 지나치게 클 경우 C언어는 메모리에 담지 못하고 에러를 출력한다.
# 하지만 파이썬은 오버플로우가 없어서 괜찮다.
# 터지지 않는 이유는 arbitrary precision 덕분이다.
# 기존의 사용할 수 있는 메모리 양이 정해져있는 fixed precision과 달리
# 현재 남아있는 만큼의 가용 메모리를 모두 수 표현에 끌어다 쓸 수 있는 형태

# 내가 본 글
# https://yongku.tistory.com/entry/%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-10757%EB%B2%88-%ED%81%B0-%EC%88%98-AB-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython

# 파이썬3에는 오버플로우가 없다?
# https://ahracho.github.io/posts/python/2017-05-09-python-integer-overflow/
