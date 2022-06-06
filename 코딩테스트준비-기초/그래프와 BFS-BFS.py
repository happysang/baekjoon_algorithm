# 1697번 - 숨바꼭질
from collections import deque
def bfs(v):
    lis = deque([v])
    
    while(lis):
        a = lis.popleft()

        if a<=100000-1 and nums[a+1] == 0:
            nums[a+1] = nums[a]+1
            lis.append(a+1)
        if a>=2 and nums[a-1] == 0:
            nums[a-1] = nums[a]+1
            lis.append(a-1)
        if a<=100000//2 and nums[2*a] == 0:
            nums[2*a] = nums[a]+1
            lis.append(2*a)
            
n,k = map(int, input().split())

nums = [0 for _ in range(100001)]

bfs(n)

print(nums[k])



# 13913번 - 숨바꼭질 4
# 14226번 - 이모티콘
# 13549번 - 숨바꼭질 3
# 1261번 - 알고스팟
