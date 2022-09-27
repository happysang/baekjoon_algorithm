# 3번-11659
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
nums = list(map(int, input().split()))

sums = [0]
tar = 0
for t in nums:
    tar += t
    sums.append(tar)
    
for _ in range(m):
    l,r = map(int, input().split())
    print(sums[r]-sums[l-1])




# 8번-1253
import sys
input = sys.stdin.readline
res = 0
n = int(input())
nums = list(map(int, input().split()))
nums.sort()

for i in range(n):
    tar = nums[i]
    l = 0
    r = n-1
    while(l<r):
        if l == i:
            l += 1
            continue
        if r == i:
            r -= 1
            continue
        
        if nums[l]+nums[r] == tar:
            res+=1
            break
        elif nums[l]+nums[r] < tar:
            l+=1
        elif nums[l]+nums[r] > tar:
            r-=1
print(res)




# 10번-11003 -> 시간초과
import sys
from collections import deque

input = sys.stdin.readline
n,l = map(int, input().split())
nums = list(map(int, input().split()))

tar = deque()

for i in range(n):
    while(tar and tar[0][0] <= i-l):
        tar.popleft()
    while(tar and tar[-1][1]>=nums[i]):
        tar.pop()
    tar.append( [i,nums[i]] )
    print(tar[0][1], end=" ")


# 15번-2750



# 23번-11724
# 26번-1206
# 29번-1920
# 36번-1541
# 37번-1929
# 50번-1717
# 54번-1516
# 56번-1753
# 58번-1854
# 59번-11657
# 61번-11404
# 64번-1197
# 71번-2042
# 75번-11438
# 81번-1722
# 82번-1256
# 86번-2193
# 90번-9252
# 94번-11049
# 95번-2098
# 96번-14003





# 17298
# n = int(input())
# nums = list(map(int, input().split()))
# res = [-1 for _ in range(n)]

# stk = []
# for i in range(n):
#     while(stk and nums[stk[-1]] < nums[i]):
#         res[stk.pop()] = nums[i]
#     stk.append(i)
# print(*res)