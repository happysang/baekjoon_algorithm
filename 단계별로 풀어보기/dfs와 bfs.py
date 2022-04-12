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
###dfs로 풀이
num = int(input())

nums = []
for _ in range(num):
    nums.append(list(map(int, input())))

yy = [1,-1,0,0]
xx = [0,0,1,-1]
global count

def dfs(nums, y, x):
    global count
    nums[y][x] = 0
    for _ in range(num):
        for t in range(4):
            ty = y + yy[t]
            tx = x + xx[t]
            if ty < 0 or ty >= num or tx < 0 or tx >= num:
                continue 
            if nums[ty][tx] == 1:
                nums[ty][tx] = 0
                count += 1
                dfs(nums, ty, tx)
        return count
    
res = []
for y in range(num):
    for x in range(num):
        if nums[y][x] == 1:
            count = 1
            res.append(dfs(nums, y, x))

print(len(res))
for x in sorted(res):
    print(x)


#1012
###bsf로 풀기
num = int(input())

dx = [0,0,1,-1]
dy = [-1,1,0,0]


from collections import deque
def bfs(y,x):
    lis = deque()
    lis.append((y,x))
    nums[y][x] = 0
    while(lis):
        b , a = lis.popleft()
        for k in range(4):
            xx = a + dx[k]
            yy = b + dy[k]
            
            if 0<=xx<m and 0<=yy<n and nums[yy][xx] ==1:
                nums[yy][xx] = 0
                lis.append((yy,xx))
        
    

for _ in range(num):
    m, n, k = map(int, input().split())
    nums = [[0 for _ in range(m)] for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int, input().split())
        nums[y][x] = 1
    
    cnt = 0
    for y in range(n):
        for x in range(m):
            if nums[y][x] == 1:
                cnt += 1
                bfs(y,x)
    print(cnt)

### dfs로 풀기
import sys
sys.setrecursionlimit(10000000)

case = int(input())
yy = [0,0,1,-1]
xx = [1,-1,0,0]

def dfs(y,x):
    nums[y][x] = 0
    for _ in range(m):
        for k in range(4):
            yyy = y + yy[k]
            xxx = x + xx[k]
            if 0 <= yyy < n and 0 <= xxx < m and nums[yyy][xxx] == 1:
    
                dfs(yyy,xxx)

for _ in range(case):
    m, n, k = map(int, input().split())
    nums = [[0 for _ in range(m)] for _ in range(n)]
    
    for _ in range(k):
        x,y = map(int, input().split())
        nums[y][x] = 1  
        
    cnt = 0
    for j in range(n):
        for i in range(m):
            if nums[j][i] == 1:
                cnt += 1
                dfs(j,i)
                
    print(cnt)
    
    
    
#2178
from collections import deque
n,m = map(int, input().split())
nums = [['0' for _ in range(m+1)]]

for _ in range(n):
    nums.append(list("0"+input()))

yy = [1,0,-1,0]
xx = [0,1,0,-1]

nums[1][1] = 1
lis = deque()
lis.append((1,1))

while(lis):
    a,b = lis.popleft()
    
    for i in range(4):
        y = a + yy[i]
        x = b + xx[i]
        
        if 1<=y<n+1 and 1<=x<m+1 and nums[y][x] == '1':
            lis.append((y,x))
            nums[y][x] = nums[a][b] + 1
        
print(nums[n][m])



#7576
#7569
#1697
#2206
#7562
#1707
