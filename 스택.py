#10828
from collections import deque
import sys

deq = deque()
num = int(input())


for x in range(num):
    cmd = list(sys.stdin.readline().split())
    
    if cmd[0] == "push":
        deq.append(int(cmd[-1]))
    elif cmd[0] == "pop":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())
    elif cmd[0] == "size":
        print(len(deq))
    elif cmd[0] == "empty":
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == "top":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])
            

#10773


#9012


#4949


#1874



#17298
