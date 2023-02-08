### 2468
from collections import deque
import sys
input = sys.stdin.readline


n = int(input())
nums = []
maxv = 0
for _ in range(n):
    lis = list(map(int, input().split()))
    maxv = max(maxv, max(lis))
    nums.append(lis)
    
dx = [1,0,-1,0]
dy = [0,1,0,-1]

ans = []
for rain in range(maxv):
    visit = [[0 for _ in range(n)] for _ in range(n)]
    res = 0
    for i in range(n):
        for j in range(n):
            
            #bfs시작
            if nums[i][j] > rain and visit[i][j] == 0:
                res += 1
                temp = deque([ [i,j] ])
                while(temp):
                    lis = temp.popleft()
                    y,x = lis[0], lis[1]
                    for k in range(4):
                        if 0 <= y+dy[k] < n and 0 <= x+dx[k] < n and nums[y+dy[k]][x+dx[k]]>rain and visit[y+dy[k]][x+dx[k]]==0:
                            visit[y+dy[k]][x+dx[k]] = 1
                            temp.append([y+dy[k],x+dx[k]])
    
    ans.append(res)
            
print(max(ans))



### 5014
from collections import deque
F, S, G, U, D = map(int, input().split()) 
#총높이, 현재, 목표, 위, 아래
move = [ 0 for _ in range(F+1) ]
visit = [ 0 for _ in range(F+1) ]


# 처음과 목표가 같은 경우, 불가능한 경우 제거
if S == G:
    print(0)
    exit()
    
if (S < G and U == 0) or (S > G and D == 0):
    print("use the stairs")
    exit()


# 목표와 현재를 최대한 가깝게 설정
if S<G:
    v = (G-S)//U
    S = S+U*((G-S)//U)
    move[S] = v
    
if S>G:
    v = (S-G)//D
    S = S-D*((S-G)//D)
    move[S] = v


visit[S] = 1
temp = deque([S])


# bfs
while(temp):
    tar = temp.popleft()
    # print(tar, temp, move)
    
    if tar == G:
        print(move[tar])
        exit()
    
    if tar+U<=F and visit[tar+U] == 0:
        visit[tar+U] = 1
        move[tar+U] = move[tar]+1
        temp.append(tar+U)
        
    if tar-D>=1 and visit[tar-D] == 0:
        visit[tar-D] = 1
        move[tar-D] = move[tar]+1
        temp.append(tar-D)
        
print("use the stairs")



### 2178
from collections import deque
n,m = map(int, input().split())

dy = [0,1,0,-1]
dx = [1,0,-1,0]
nums = []
for _ in range(n):
    nums.append(list(map(int, list(input()))))
    
for i in range(n):
    for j in range(m):
        temp = deque([(i,j)])
        while(temp): 
            y,x = temp.popleft()
            if y == n-1 and x ==m-1:
                print(nums[y][x])
                exit()
            for k in range(4):
                if 0<=y+dy[k]<n and 0<=x+dx[k]<m and nums[y+dy[k]][x+dx[k]] == 1 and (y+dy[k] != 0 or x+dx[k] != 0):
                    nums[y+dy[k]][x+dx[k]] = nums[y][x] + 1
                    temp.append((y+dy[k],x+dx[k]))
                    
                    
                    
### 1926
from collections import deque
n,m = map(int, input().split())

dy = [0,1,0,-1]
dx = [1,0,-1,0]
nums = []
visit = []
for _ in range(n):
    nums.append(list(map(int,input().split())))
    visit.append([0 for _ in range(m)])
    
cnt = 0
m_size = 0
for i in range(n):
    for j in range(m):
        if nums[i][j] == 1 and visit[i][j] == 0:
            visit[i][j] = 1
            temp_size = 1
            cnt += 1
            temp = deque([(i,j)])
            
            while(temp):
                y,x = temp.popleft()
                for k in range(4):
                    if 0<=y+dy[k]<n and 0<=x+dx[k]<m and nums[y+dy[k]][x+dx[k]] == 1 and visit[y+dy[k]][x+dx[k]] == 0:
                        visit[y+dy[k]][x+dx[k]] = 1
                        temp_size += 1
                        temp.append((y+dy[k],x+dx[k]))
                        
            m_size = max(m_size, temp_size)
   
print(cnt)
print(m_size)



### 4963
from collections import deque

dx = [1,1,1,0,-1,-1,-1,0]
dy = [1,0,-1,-1,-1,0,1,1]

def bfs(a,b):
    temp = deque([(a,b)])
    while(temp):
        y,x = temp.popleft()
        for i in range(8):
            if 0<=y+dy[i]<h and 0<=x+dx[i]<w and m[y+dy[i]][x+dx[i]] == 1 and visit[y+dy[i]][x+dx[i]] == 0:
                visit[y+dy[i]][x+dx[i]] = 1
                temp.append((y+dy[i],x+dx[i]))
    
while True:
    w, h = map(int, input().split())
    if w == 0:
        exit()

    m = []
    visit = []
    for _ in range(h):
        m.append(list(map(int, input().split())))
        visit.append([0 for _ in range(w)])
    
    cnt = 0
    for i in range(h):
        for j in range(w):
            if m[i][j] == 1 and visit[i][j] == 0:
                visit[i][j] = 1
                bfs(i,j)
                cnt += 1
    print(cnt)



### 1303
from collections import deque

dx = [1,0,-1,0]
dy = [0,-1,0,1]


def bfsw(i,j):
    global wv
    temp = deque([(i,j)])

    while(temp):
        y,x = temp.popleft()
        
        for k in range(4):
            if 0<=y+dy[k]<m and 0<=x+dx[k]<n and nums[y+dy[k]][x+dx[k]] == 'W' and visit[y+dy[k]][x+dx[k]] == 0:
                visit[y+dy[k]][x+dx[k]] = 1
                temp.append((y+dy[k],x+dx[k]))
                wv += 1
    
    
def bfsb(i,j):
    global bv
    temp = deque([(i,j)])

    while(temp):
        y,x = temp.popleft()
        
        for k in range(4):
            if 0<=y+dy[k]<m and 0<=x+dx[k]<n and nums[y+dy[k]][x+dx[k]] == 'B' and visit[y+dy[k]][x+dx[k]] == 0:
                visit[y+dy[k]][x+dx[k]] = 1
                temp.append((y+dy[k],x+dx[k]))
                bv += 1


n,m = map(int, input().split()) #가로높이, 세로높이

nums = []
visit = []
for _ in range(m):
    nums.append(list(input()))
    visit.append([0 for _ in range(n)])
    
resw = []
resb = []
for i in range(m):
    for j in range(n):
        if nums[i][j] == 'W' and visit[i][j] == 0:
            wv = 1
            visit[i][j] = 1
            bfsw(i,j)
            resw.append(wv ** 2)
            
        if nums[i][j] == 'B' and visit[i][j] == 0:
            bv = 1
            visit[i][j] = 1
            bfsb(i,j)
            resb.append(bv ** 2)
            
            
print(sum(resw),sum(resb))