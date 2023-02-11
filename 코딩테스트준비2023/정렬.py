### 10815
import sys
input = sys.stdin.readline

def sol():
    input()
    nums1 = set(input().split())
    input()
    nums2 = input().split()

    res = ""
    for n in nums2:
        if n in nums1:
            res += "1 "
        else:
            res += "0 "
    print(res)
            
sol()



### 1764
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
name = set()

for _ in range(n):
    name.add(input().rstrip())

res = []
for _ in range(m):
    tar = input().rstrip()
    if tar in name:
        res.append(tar)
        

print(len(res))
for n in sorted(res):
    print(n)
    
    
    
### 1744
from collections import deque
import sys
input = sys.stdin.readline


n = int(input())
temp = []
for _ in range(n):
    temp.append(int(input()))
nums = deque(sorted(temp))


res = 0
while(nums and nums[0]<=0):
    if len(nums) == 1:
        print(res+nums[0])
        exit()
    else:
        if nums[0] < 0:
            if nums[1]>0:
                res += nums[0]
            elif nums[1] == 0:
                nums.popleft()
            else:
                res += nums[0]*nums[1]
                nums.popleft()              
        nums.popleft()

            
if len(nums) % 2 == 1:
    res += nums[0]
    nums.popleft()
    
if len(nums) == 1:
    print(res+nums[0])
    exit()
else:
    while(nums and nums[0] == 1):
        res += nums[0]+nums[1]
        nums.popleft()
        nums.popleft()

for i in range(0,len(nums),2):
    res += nums[i]*nums[i+1]

print(res)


