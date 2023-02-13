### 2805
def sol(c):
    res = 0
    for v in nums:
        if v>c:
            res += v-c
    return res    

n,m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

start,end = 0, nums[-1]
tar = (start+end)//2

while(start < end):
    # print(start, tar, end)
    if start == tar or end == tar:
        print(tar)
        break
    
    if sol(tar)>=m:
        start = tar
        tar = (start+end)//2
    else:
        end = tar
        tar = (start+end)//2
        
    

### 1654
def sol(v):
    res = 0
    for n in nums:
        res += n//v
    return res

k,n = map(int, input().split())
nums = []

for _ in range(k):
    nums.append(int(input()))
nums.sort()

start,end = 1, nums[-1]
tar = (start+end)//2

while(start < end):
    if sol(tar)<n:
        end = tar-1
    else:
        if (sol(tar+1)) <n:
            print(tar)
            exit()
        start = tar+1
    tar = (start+end)//2
    
print(tar)



### 2512
def sol(v):
    res = 0
    for n in nums:
        if n<=v:
            res += n
        else:
            res += v
    return res

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
start,end = 1, max(nums)
tar = (start+end) // 2


while(start<=end):
    if sol(tar) <= m :
        if sol(tar+1)>m:
            print(tar)
            exit()
        start = tar+1
    else:
        end = tar-1
    tar = (start+end)//2
print(tar)