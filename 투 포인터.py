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

#1644

#1450