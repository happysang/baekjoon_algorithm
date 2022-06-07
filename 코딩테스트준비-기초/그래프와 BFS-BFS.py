# 1697번 - 숨바꼭질
from collections import deque
def bfs(v):
    lis = deque([v])
    
    while(lis):
        a = lis.popleft()
        if a == k:
            print(nums[k])
            exit()
        
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
if n>k:
    print(n-k)
    exit()
nums = [0 for _ in range(100001)]

bfs(n)



# 13913번 - 숨바꼭질 4
# 14226번 - 이모티콘
# 13549번 - 숨바꼭질 3
from collections import deque
def bfs(v):
    lis = deque([v])
    
    while(lis):
        a = lis.popleft()
        if a == k:
            print(nums[k])
            exit()
            
        if a<=100000//2 and nums[2*a] == -1:
            if nums[a] == -1:
                nums[2*a] = 0
            else:
                nums[2*a] = nums[a]
            lis.appendleft(2*a)
            
            
        if a<=100000-1 and nums[a+1] == -1:
            if nums[a] == -1:
                nums[a+1] = 1
            else:
                nums[a+1] = nums[a]+1
            lis.append(a+1)
            
                        
        if a>=1 and nums[a-1] == -1:
            if nums[a] == -1:
                nums[a-1] = 1
            else:
                nums[a-1] = nums[a]+1
            lis.append(a-1)
            

n,k = map(int, input().split())
if n>=k:
    print(n-k)
    exit()
    
nums = [-1 for _ in range(100001)]

bfs(n)


# 1261번 - 알고스팟
