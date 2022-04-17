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
# 1107번 - 리모컨
# 14500번 - 테트로미노
# 6064번 - 카잉 달력
# 1748번 - 수 이어 쓰기 1
# 9095번 - 1, 2, 3 더하기