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