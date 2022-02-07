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
import sys
num = int(sys.stdin.readline().strip())
nums = {}

for i in range(num):
    root, l, r = sys.stdin.readline().strip().split()
    nums[root] = [l, r]
    
def pre(root):
    if root != '.':
        print(root, end='')
        pre(nums[root][0])
        pre(nums[root][1])
        
def mid(root):
    if root != '.':
        mid(nums[root][0])
        print(root, end='')
        mid(nums[root][1])
        
def post(root):
    if root != '.':
        post(nums[root][0])
        post(nums[root][1])
        print(root, end='')
        
pre('A')
print()
mid('A')
print()
post('A')


#2263
#5639
#4803
