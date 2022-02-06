#11725
###dfs로 풀이
from collections import deque
import sys

sys.setrecursionlimit(100000000)
n = int(input())
nums = [[] for _ in range(n+1)]
p = [0] * (n+1)

for x in range(n-1):
    x, y = map(int, sys.stdin.readline().split())
    nums[x].append(y)
    nums[y].append(x)

def dfs(i):
    for k in nums[i]:
        if p[k] == 0:
            p[k] = i
            dfs(k)
        
dfs(1)
for x in p[2:]:
    print(x)
### bfs로 풀이
from collections import deque
import sys

n = int(input())
nums = [[] for _ in range(n+1)]

for x in range(n-1):
    x, y = map(int, sys.stdin.readline().split())
    nums[x].append(y)
    nums[y].append(x)

p = [0] * (n+1)
temp = deque([1])

while(temp):
    i = temp.popleft()
    for k in nums[i]:
        if k == p[i]:
            continue
        p[k] = i
        temp.append(k)
        nums[i] = []

for x in p[2:]:
    print(x)
    
    
    
#1167
#1967
#1991
#2263
#5639
#4803
