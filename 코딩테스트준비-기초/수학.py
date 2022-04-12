# 10430번 - 나머지
A, B, C = map(int, input().split())
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)


# 4375번 - 1
import sys
while True:
    try:
        tar = int(sys.stdin.readline())
    except:
        break

    num = 1
    cnt = 1
    while True:
        if num % tar != 0:
            num += 10**cnt ## str(num) 이런식으로 제곱하려했는데 시간아웃걸림. 참고하기.
            cnt +=1
        else:
            break
    print(len(str(num)))


# 1037번 - 약수
import sys
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))


if len(nums)%2 == 0:
    print(sorted(nums)[0] * sorted(nums)[-1])
else:
    print(sorted(nums)[n//2] ** 2)
    

# 17427번 - 약수의 합2



# 17425번 - 약수의 합
# 2609번 - 최대공약수와 최소공배수
# 1978번 - 소수 찾기
# 1929번 - 소수 구하기
# 6588번 - 골드바흐의 추측