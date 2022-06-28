# 14225번 - 부분수열의 합
from itertools import combinations

n = int(input())
num = list(map(int, input().split()))

import copy
nums = copy.deepcopy(num)
for i in range(2,n+1):
    nums += list(map(sum,combinations(num, i)))
nums = sorted(list(set(nums)))

ans = 0
for i in range(len(nums)):
    if i+1 != nums[i]:
        print(i+1)
        exit()
print(nums[-1]+1)


# 1062번 - 가르침
# 13460번 - 구슬 탈출 2
# 12100번 - 2048 (Easy)