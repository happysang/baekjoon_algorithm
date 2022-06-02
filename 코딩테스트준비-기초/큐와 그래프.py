# 10845번 - 큐
from collections import deque
import sys

n = int(sys.stdin.readline().strip())

l = deque()
for _ in range(n):
    s = sys.stdin.readline().strip()
    if "push" in s:
        s, num = s.split()
        num = int(num)
        l.append(num)
        
    elif s == "pop":
        if l:
            print(l.popleft())
        else:
            print(-1)
        
    elif s == "size":
        print(len(l))
        
    elif s == "empty":
        if len(l) != 0:
            print(0)
        else:
            print(1)
            
    elif s == "front":
        if len(l) != 0:
            print(l[0])
        else:
            print(-1)
            
    elif s == "back":
        if len(l) != 0:
            print(l[-1])
        else:
            print(-1)



# 10866번 - 덱
from collections import deque
import sys

n = int(sys.stdin.readline().strip())

l = deque()
for _ in range(n):
    
    s = sys.stdin.readline().strip()
    
    if "push" in s:
        s, num = s.split()
        num = int(num)
        if "front" in s:
            l.appendleft(num)
        else:
            l.append(num)
        
    elif s == "pop_front":
        if len(l) != 0:
            print(l.popleft())
        else:
            print(-1)
    
    elif s == "pop_back":
        if len(l) != 0:
            print(l.pop())
        else:
            print(-1)    
    
    elif s == "size":
        print(len(l))
        
    elif s == "empty":
        if len(l) != 0:
            print(0)
        else:
            print(1)
            
    elif s == "front":
        if len(l) != 0:
            print(l[0])
        else:
            print(-1)
            
    elif s == "back":
        if len(l) != 0:
            print(l[-1])
        else:
            print(-1)
            
            
            
# 13023번 - ABCDE
import sys

def dfs(v,cnt):
    visit[v] = 1
    cnt += 1
    if cnt >= 5:
        print(1)
        exit()
    
    for i in points[v]:
        if visit[i] == 0:
            dfs(i,cnt)
            visit[i] = 0

n,m = map(int, input().split())
points = [[]for _ in range(n)]
visit = [0]*n


for _ in range(m):
    i,j = map(int, sys.stdin.readline().split())
    points[i].append(j)
    points[j].append(i)
    
for i in range(n):
    dfs(i,0)
    visit[i] = 0

print(0)



# 1260번 - DFS와 BFS
def dfs(v):
    print(v, end=' ')
    visit1[v] = 1
    for i in sorted(points[v]):
        if visit1[i] == 0:
            dfs(i)
            

from collections import deque
def bfs(v):
    lis = deque([v])
    visit2[v] = 1
    while(lis):
        p = lis.popleft()
        print(p, end=' ')
        for i in sorted(points[p]):
            if visit2[i] == 0:
                lis.append(i)
                visit2[i] = 1
                

n,m,v = map(int, input().split())
points = [[]for _ in range(n+1)]

for i in range(m):
    i,j = map(int, input().split())
    points[i].append(j)
    points[j].append(i)

visit1 = [0 for _ in range(n+1)]
dfs(v)

print()

visit2 = [0 for _ in range(n+1)]
bfs(v)



# 11724번 - 연결 요소의 개수
import sys
sys.setrecursionlimit(10**9)

def dfs(v):
    visit[v] = 1
    for a in points[v]:
        if visit[a] == 0:
            dfs(a)
    
from collections import deque
def bfs(v):
    lis = deque([v])
    visit[v] = 1
    while(lis):
        p = lis.popleft()
        for i in points[p]:
            if visit[i] == 0:
                lis.append(i)
                visit[i] = 1
    
    
n,m = map(int, input().split())
points = [[]for _ in range(n+1)]
visit = [0 for _ in range(n+1)]

for _ in range(m):
    i,j = map(int, sys.stdin.readline().split())
    points[i].append(j)
    points[j].append(i)
    
cnt = 0
for i in range(1,n+1):
    if visit[i] == 0:
        cnt += 1
        dfs(i) # 혹은 bfs(i)
        
print(cnt)


# 1707번 - 이분 그래프
# 2667번 - 단지번호붙이기
# 2178번 - 미로 탐색
# 7576번 - 토마토
# 7562번 - 나이트의 이동