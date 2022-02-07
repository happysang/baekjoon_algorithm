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
from collections import deque
import sys

num = int(input())
nums = [[]for _ in range(num)]

for i in range(num):
    x,y,z = sys.stdin.readline().split()
    tx, ty, tz = ord(x)-65, ord(y)-65, ord(z)-65
    if ty > 0:
        nums[tx].append(ty)
        nums[ty].append(tx)
    else:
        nums[tx].append(ty)
    if tz > 0:
        nums[tx].append(tz)
        nums[tz].append(tx)
    else:
        nums[tx].append(tz)
nums[0] = [0] + nums[0]



res1 = [0]
def dfs1(i):
    for x in nums[i][1:]:
        if x>0:
            res1.append(x)
            dfs1(x)


res2 = []
temp = [0]
def dfs2(i):
    global temp
    global res2
    for x in nums[i][1:]:
        if x > 0:
            temp.append(x)
            dfs2(x)
        else:
            if temp:
                res2 += reversed(temp)
                temp = []

res3 = []
def dfs3(t):
    if nums[t][1] > 0 and nums[t][1] not in res3:
        dfs3(nums[t][1])
    if nums[t][2] > 0 and nums[t][2] not in res3:
        dfs3(nums[t][2])
    if t not in res3:
        res3.append(t)


dfs1(0)
dfs2(0)
for x in res2:
    dfs3(x)

for x in res1:
    print(chr(x+65), end='')
print()

for x in res2:
    print(chr(x+65), end='')
print()

for x in res3:
    print(chr(x+65), end='')
print()


#2263
#5639
#4803
