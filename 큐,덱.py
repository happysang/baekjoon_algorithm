#18258
from collections import deque
import sys
que = deque()

num = int(sys.stdin.readline())

for _ in range(num):
    tar = list(sys.stdin.readline().split())
    
    if tar[0] == "push":
        que.append(int(tar[1]))
    elif tar[0] == "pop":
        if len(que) == 0:
            print(-1)
        else:
            print(que.popleft())
    elif tar[0] == "size":
        print(len(que))
    elif tar[0] == "empty":
        if (len(que)) == 0:
            print(1)
        else:
            print(0)
    elif tar[0] == "front":
        if (len(que)) == 0:
            print(-1)
        else:
            print(que[0])
    elif tar[0] == "back":
        if (len(que)) == 0:
            print(-1)
        else:
            print(que[-1])
            
            

#2164
from collections import deque
import sys

num = int(sys.stdin.readline())
que = deque([x for x in range(1,num+1)])

while(len(que) > 1):
    que.popleft()
    que.append(que[0])
    que.popleft()
    
print(que[-1])



#11866
from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())
que = deque([x for x in range(1,n+1)])
lis = []



while(len(que) > 1):
    for _ in range(k-1):
        que.append(que.popleft())
    lis.append(str(que.popleft()))
lis.append(str(que.pop()))
print("<"+", ".join(lis)+">")



#1966
from collections import deque
import sys

for _ in range(int(input())):
    n, k = map(int, sys.stdin.readline().split())
    que = deque(list(map(int,sys.stdin.readline().split())))
    idx_que = deque([x for x in range(n)])
    cnt = 0
    
    while(len(que) > 0):
        if que[0] != max(que):
            que.append(que.popleft())
            idx_que.append(idx_que.popleft())
        else:
            que.popleft()
            cnt += 1
            if k == idx_que.popleft():
                print(cnt)
                break



#10866
from collections import deque
import sys
deq = deque()

for x in range(int(sys.stdin.readline())):
    tar = list(sys.stdin.readline().split())
    
    if tar[0] == "push_front":
        deq.appendleft(tar[1])
    elif tar[0] == "push_back":
        deq.append(tar[1])
    elif tar[0] == "pop_front":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())
    elif tar[0] == "pop_back":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())
    elif tar[0] == "size":
        print(len(deq))
    elif tar[0] == "empty":
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif tar[0] == "front":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    elif tar[0] == "back":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])


#1021
from collections import deque
import sys

n , m = map(int, sys.stdin.readline().split())
lis = list(map(int, sys.stdin.readline().split()))
deq = deque([x for x in range(1,n+1)])

res = 0
for x in lis:
    cnt = 0
    while(deq[0] != x):
        deq.append(deq.popleft())
        cnt+=1
    if len(deq)/2 < cnt:
        cnt = len(deq) - cnt
    res += cnt
    deq.popleft()

print(res)



#5430