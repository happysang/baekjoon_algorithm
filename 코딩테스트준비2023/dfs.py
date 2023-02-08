### 13023
def dfs(p,res):
    if res >= 5:
        print(1)
        exit()
        
    for a in r[p]:
        if visit[a] == 0:
            visit[a] = 1
            dfs(a,res+1)
            visit[a] = 0
    

n, m = map(int, input().split())
r = [[] for _ in range(n)]

for _ in range(m):
    i,j = map(int, input().split())
    r[i].append(j)
    r[j].append(i)

visit = [0 for _ in range(n)]
for i in range(n):
    visit[i] = 1
    dfs(i,1)
    visit[i] = 0
    
print(0)



### 4963
import sys
sys.setrecursionlimit(10**6)

dx = [1,1,1,0,-1,-1,-1,0]
dy = [1,0,-1,-1,-1,0,1,1]

def dfs(y,x):
    for i in range(8):
        if 0<=y+dy[i]<h and 0<=x+dx[i]<w and m[y+dy[i]][x+dx[i]] == 1 and visit[y+dy[i]][x+dx[i]] == 0:
            visit[y+dy[i]][x+dx[i]] = 1
            dfs(y+dy[i],x+dx[i])
        
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
                dfs(i,j)
                cnt += 1
    print(cnt)


### 24479
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(p):
    global res
    visit[p] = res
    res+=1
    for v in sorted(nums[p]):
        if visit[v] == 0:
            dfs(v)

n,e,r = map(int,input().split())

visit = [0 for _ in range(n+1)]
nums = [ [] for _ in range(n+1) ]

for _ in range(e):
    a,b = map(int, input().split())
    nums[a].append(b)
    nums[b].append(a)
    
res = 1
dfs(r)

for a in visit[1:]:
    print(a)