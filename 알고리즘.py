# 3번-11659
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
nums = list(map(int, input().split()))

sums = [0]
tar = 0
for t in nums:
    tar += t
    sums.append(tar)
    
for _ in range(m):
    l,r = map(int, input().split())
    print(sums[r]-sums[l-1])




# 8번-1253
import sys
input = sys.stdin.readline
res = 0
n = int(input())
nums = list(map(int, input().split()))
nums.sort()

for i in range(n):
    tar = nums[i]
    l = 0
    r = n-1
    while(l<r):
        if l == i:
            l += 1
            continue
        if r == i:
            r -= 1
            continue
        
        if nums[l]+nums[r] == tar:
            res+=1
            break
        elif nums[l]+nums[r] < tar:
            l+=1
        elif nums[l]+nums[r] > tar:
            r-=1
print(res)




# 10번-11003 -> 시간초과
import sys
from collections import deque

input = sys.stdin.readline
n,l = map(int, input().split())
nums = list(map(int, input().split()))

tar = deque()

for i in range(n):
    while(tar and tar[0][0] <= i-l):
        tar.popleft()
    while(tar and tar[-1][1]>=nums[i]):
        tar.pop()
    tar.append( [i,nums[i]] )
    print(tar[0][1], end=" ")




# 15번-2750
n = int(input())
nums = []

for _ in range(n):
    nums.append(int(input()))
    
for i in range(1,n):
    for j in range(i,0,-1):
        if nums[j-1] > nums[j]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            
for t in nums:
    print(t)




# 23번-11724
### i) dfs로 풀이
import sys
sys.setrecursionlimit(10**9)

def dfs(v):
    visit[v] = 1
    for n in nums[v]:
        if visit[n] == 0:
            dfs(n)
    
cnt = 0
n,m = map(int, input().split())
nums = [[] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    nums[a].append(b)
    nums[b].append(a)
    
for i in range(1,n+1):
    if visit[i] == 0:
        cnt += 1
        dfs(i)

print(cnt)


### ii) bfs로 풀이
import sys
from collections import deque

n,m = map(int, input().split())
points = [[] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]

for _ in range(m):
    i,j = map(int, sys.stdin.readline().split())
    points[i].append(j)
    points[j].append(i)
    
cnt = 0
for v in range(1,n+1):
    if visit[v] == 0:
        cnt += 1
        lis = deque([v])
        while(lis):
            p = lis.popleft()
            visit[p] = 1
            for i in points[p]:
                if visit[i] == 0 and i not in lis:
                    lis.append(i)

print(cnt)




# 26번-1260
def dfs(v):
    print(v, end=" ")
    visit1[v] = 1
    for n in sorted(nums[v]):
        if visit1[n] == 0:
            dfs(n)

from collections import deque
def bfs(v):
    lis = deque([v])
    while(lis):
        p = lis.popleft()
        print(p, end=" ")
        visit2[p] = 1
        for i in sorted(nums[p]):
            if visit2[i] == 0 and i not in lis:
                lis.append(i)


n,m,v = map(int, input().split())
nums = [[] for _ in range(n+1)]
visit1 = [0 for _ in range(n+1)]
visit2 = [0 for _ in range(n+1)]


for _ in range(m):
    a,b = map(int, input().split())
    nums[a].append(b)
    nums[b].append(a)

for i in range(1,n+1):
    nums[i].sort()
    
dfs(v)
print()
bfs(v)



# 29번-1920
n = int(input())
nums1 = sorted(list(map(int, input().split())))

m = int(input())
nums2 = list(map(int, input().split()))


for num in nums2:
    flag = True
    start = 0
    end = n-1
    while(start<=end):
        temp = (start+end)//2
        if num == nums1[temp]:
            print(1)
            flag = False
            break
        elif num < nums1[temp]:
            end = temp-1
        elif num > nums1[temp]:
            start = temp+1
    if flag:
        print(0)
        
        
        
# 36번-1541
tar = input()

temp = ''
nums = []
cal = []

for t in tar:
    if t.isdigit():
        temp += t
    else:
        nums.append(int(temp))
        temp = ''
        cal.append(t)
nums.append(int(temp))


res = nums[0]
nums = nums[1:]
pre_mul = '+'
temp = 0
for i in range(len(cal)):
    if pre_mul == '+' and cal[i] == '+':
        res += nums[i]
    elif pre_mul == '-' and cal[i] == '+':
        temp += nums[i]
    elif pre_mul == '+' and cal[i] == '-':
        pre_mul = '-'
        temp += nums[i]
    elif pre_mul == '-' and cal[i] == '-':
        res -= temp
        temp = nums[i]
print(res-temp)


# 37번-1929
n,m = map(int, input().split())
nums = [1,1]+[0 for _ in range(m-1)]

for i in range(2,m//2+1):
    temp = i*2
    if nums[i] == 0:
        while(temp<=m):
            nums[temp] = 1
            temp += i
            
for i in range(n,len(nums)):
    if nums[i] == 0:
        print(i)
        
        
        
# 50번-1717

# 54번-1516
# 56번-1753
# 58번-1854
# 59번-11657
# 61번-11404
# 64번-1197
# 71번-2042
# 75번-11438
# 81번-1722
# 82번-1256
# 86번-2193
# 90번-9252
# 94번-11049
# 95번-2098
# 96번-14003





# 17298
# n = int(input())
# nums = list(map(int, input().split()))
# res = [-1 for _ in range(n)]

# stk = []
# for i in range(n):
#     while(stk and nums[stk[-1]] < nums[i]):
#         res[stk.pop()] = nums[i]
#     stk.append(i)
# print(*res)