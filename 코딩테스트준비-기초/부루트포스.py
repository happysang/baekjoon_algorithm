# 2309번 - 일곱 난쟁이
import sys

nums = []
for _ in range(9):
    nums.append(int(sys.stdin.readline().strip()))

gap = sum(nums)-100


for i in nums:
    for j in nums:
        if i == j:
            continue
        if gap == i+j:
            nums.remove(i)
            nums.remove(j)
            
            for i in sorted(nums):
                print(i)
            exit()


# 3085번 - 사탕 게임



# 1476번 - 날짜 계산
import sys
e,s,m = map(int, sys.stdin.readline().split())
year = 0

while(True):
    if year % 15 + 1 == e and year % 28 + 1 == s and year % 19 + 1 == m:
        print(year+1)
        break
    else:
        year += 1


# 1107번 - 리모컨


# 14500번 - 테트로미노



# 6064번 - 카잉 달력


# 1748번 - 수 이어 쓰기 1
import sys
n = sys.stdin.readline().strip()
num = int(n)

res = 0
for i in range(len(n)):
    k = 9 * (10**i) * (i+1)
    res += k
    if i==len(n)-1:
        res -= k
        if i != 0:
            temp = num - ((10**i)-1)
        else:
            temp = num
        res += temp*(i+1)
        
print(res)



# 9095번 - 1, 2, 3 더하기