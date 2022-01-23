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
from collections import deque
import sys

deq = deque()
num = int(input())

for x in range(num):
    cmd = int(sys.stdin.readline())
    if cmd == 0:
        deq.pop()
    else:
        deq.append(cmd)

print(sum(list(deq)))



#9012
from collections import deque
import sys

for _ in range(int(input())):
    deq = deque()
    flag = True
    for cmd in sys.stdin.readline().strip():
        if cmd == "(":
            deq.append(cmd)
        else:
            if len(deq) == 0:
                flag = False
                break
            else:
                deq.pop()
    if len(deq) == 0 and flag:
        print("YES")
    else:
        print("NO")
    



#4949


#1874



#17298
