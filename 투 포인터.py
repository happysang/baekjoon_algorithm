#3273
import sys
from collections import deque

num = int(input())
nums = list(map(int, sys.stdin.readline().split()))
tar = int(input())
nums.sort()
deq = deque(nums)
cnt = 0
while(len(deq) != 1 and len(deq) != 0):
    res = deq[0] + deq[-1]
    if res > tar:
        deq.pop()
    elif res < tar:
        deq.popleft()
    else:
        deq.pop()
        deq.popleft()
        cnt += 1

print(cnt)


#2470
import sys
from collections import deque

num = int(input())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
deq = deque(nums)
min = 10000000000000

while(len(deq) != 1 and len(deq) != 0):
    res = deq[0] + deq[-1]
    if abs(res) < abs(min):
        ans = [deq[0],deq[-1]]
        min = res
    if res > 0:
        deq.pop()
    elif res < 0:
        deq.popleft()
    else:
        break

print(*ans)


#1806
####부분합으로 풀이
import sys
n,s = map(int, sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))

pref = [0]
temp = 0
for x in nums:
    temp += x
    pref.append(temp)

start,end = 0,1
temp = 1000000
while(start<n):
    if pref[end]-pref[start] >= s:
        if end-start != 0:
            temp = min(temp, end-start)
        start += 1
        
    else:
        if end == n:
            break
        elif end < n:
            end += 1
        else:
            start += 1
            
if temp == 1000000:
    print(0)
else:
    print(temp)

###투포인터 풀이
import sys
n,s = map(int, sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))
if s == 0:
    print(1)
    exit()
start, end, cur = 0,0,0
ans = 1000001
while (True):
    print(start, end, cur)
    if cur >= s:
        ans = min(ans, end-start)
        cur -= nums[start]
        start += 1
    else:
        if end == n:
            break
        cur += nums[end]
        end += 1
    
if ans == 1000001:
    print(0)
else:
    print(ans)
    
    

#1644

#1450