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


#1966


#10866


#1021


#5430