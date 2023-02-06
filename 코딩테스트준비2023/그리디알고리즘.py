### 11047
n, k = map(int, input().split())
moneys = []

for _ in range(n):
    moneys.append(int(input()))
moneys.reverse()

c = 0
for m in moneys:
    if k == 0:
        break
    elif k-m < 0:
        continue
    else:
        c += k//m
        k = k%m
print(c)



### 1931
n = int(input())

meets = []
for _ in range(n):
    s,e = map(int,input().split())
    meets.append((s,e))

meets.sort(key= lambda x:(x[1],x[0]))

cnt = 0
end_time = 0
for m in meets:
    if m[0] >= end_time:
        cnt +=1
        end_time = m[1]
print(cnt)


### 11399
n = int(input())
times = sorted(list(map(int, input().split())), reverse=True)

res = 0
for i in range(n):
    res += (i+1)* times[i]
    
print(res)



### 1541
nums = input().split('-')

res = []
for x in nums:
    temp = 0
    s = x.split('+')
    for i in s:
        temp += int(i)
    res.append(temp)
    
print(res[0]*2 - sum(res))



### 13305
import copy

n = int(input())
leng = list(map(int, input().split()))
oil = list(map(int, input().split()))
res = copy.deepcopy(oil)


for i in range(n):

    if res[i] == oil[i]:
        for j in range(i+1,n):
            if oil[i]<oil[j]:
                res[j] = oil[i]
            else:
                break
ans = 0     
for i in range(n-1):
    ans += (leng[i]*res[i])

print(ans)



### 7562
from collections import deque

dx = [1,2,2,1,-1,-2,-2,-1]
dy = [2,1,-1,-2,-2,-1,1,2]

def sol(x,y,ex,ey):
    temp =deque([(x,y)])
    while(temp):
        v= temp.popleft()
        sx, sy = v[0], v[1]
        for i in range(8):
            if 0<=sx+dx[i]<l and 0<=sy+dy[i]<l and val[sy+dy[i]][sx+dx[i]] == 0 and (sy+dy[i] != y or sx+dx[i] != x):
                val[sy+dy[i]][sx+dx[i]] = val[sy][sx]+1
                if sy+dy[i] == ey and sx+dx[i] == ex:
                    print(val[sy+dy[i]][sx+dx[i]])
                    temp.clear()
                    break
                temp.append( (sx+dx[i],sy+dy[i]) )


n = int(input())
for _ in range(n):
    l = int(input())
    val =[[0 for _ in range(l)] for _ in range(l)]
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    if sx == ex and sy == ey:
        print(0)
        continue
    sol(sx,sy,ex,ey)
    
    
    
### 1026
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

idxb = []
for i in range(n):
    idxb.append([i,b[i]])
idxb.sort(key=lambda x : -x[1]) #인덱스, 값

a.sort(reverse=True)
res = 0
while(a):
    for i in range(n):
        if a[-1] == 0 and idxb[i][0] == 0 and idxb[i][1] == -1:
            continue
        else:
            res += (a[-1] * idxb[i][1])
            a.pop()
            idxb[i][1] = -1
print(res)



### 1946
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    point = []
    n = int(input())
    for _ in range(n):
        p, m = map(int, input().split())
        point.append([p,m])
    point.sort()

    res = 1
    min_rank = point[0][1]
    for i in range(1,n):
        if point[i][1] < min_rank:
            res += 1
            min_rank = point[i][1]
    
    print(res)
    
    
    
### 16953
import sys
input = sys.stdin.readline
a,b = map(int,input().split())

res = 1
while(a != b):
    if a>b:
        print(-1)
        exit()
    
    if b%10 == 1:
        b = b//10
        res += 1
        
    elif b%2 == 0:
        b = b//2
        res += 1
    
    else:
        print(-1)
        exit()
        
print(res)