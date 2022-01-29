#1260
def dfs(v):
    print(v, end=' ')
    visit[v] = 1
    for i in range(1, n + 1):
        if visit[i] == 0 and s[v][i] == 1:
            dfs(i)


def bfs(v):
    lis = [v]
    visit[v] = 1
    while(lis):
        v = lis[0]
        print(v, end=' ')
        del lis[0]
        for i in range(1, n + 1):
            if visit[i] == 0 and s[v][i] == 1:
                lis.append(i)
                visit[i] = 1


n, m, v = map(int, input().split())
s = [[0] * (n + 1) for i in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    s[x][y] = 1
    s[y][x] = 1

visit = [0 for i in range(n + 1)]
dfs(v)
print()
visit = [0 for i in range(n + 1)]
bfs(v)



#2606
n = int(input())
v = int(input())
global cnt
cnt = 0
visit = [0 for _ in range(n+1)]
nums = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(v):
    x, y = map(int, input().split())
    nums[x][y] = 1
    nums[y][x] = 1

def dfs(v):
    global cnt
    visit[v] = 1
    cnt += 1
    for i in range(1, n+1):
        if visit[i] == 0 and nums[v][i] == 1:
            dfs(i)

dfs(1)
print(cnt-1)



#2667
###bfs로 풀이
from collections import deque
num = int(input())
nums = []

for x in range(num):
    nums.append(list(map(int,input())))
    
yy = [0,0,1,-1]
xx = [1,-1,0,0]
    
def bfs(nums, y, x):
    lis = deque()
    lis.append((y,x))
    nums[y][x] = 0
    count = 1
    
    while lis:
        i,j = lis.popleft()
        for k in range(4):
            dy = i+yy[k]
            dx = j+xx[k]
            if dx < 0 or dx >= num or dy < 0 or dy >= num:
                continue
            else:
                if nums[dy][dx] == 1:
                    nums[dy][dx] = 0
                    lis.append((dy,dx))
                    count += 1        
    return count

res = []
for i in range(num):
    for j in range(num):
        if nums[i][j] == 1:
            res.append(bfs(nums, i, j))
            
print(len(res))
for x in sorted(res):
    print(x)



#1012
#2178
#7576
#7569
#1697
#2206
#7562
#1707
