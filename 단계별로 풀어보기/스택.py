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
from collections import deque
import sys

while(True):
    inp = sys.stdin.readline()
    if inp[0] == ".":
        break
    else:
        deq = deque()
        flag = True
        for cmd in inp:
            if cmd == "(" or cmd == "[":
                deq.append(cmd)
            elif cmd == ")":
                if len(deq) == 0 or deq[-1] == "[":
                    flag = False
                    break
                if deq[-1] == "(":
                    deq.pop()
            elif cmd == "]":
                if len(deq) == 0 or deq[-1] == "(":
                    flag = False
                    break
                else:
                    deq.pop()
                    
        if len(deq) == 0 and flag:
            print("yes")
        else:
            print("no")
            
            

#1874
from collections import deque
import sys

num = int(sys.stdin.readline())
stack = deque([0])
cnt = 1
res = []
lis = []

for x in range(num):
    lis.append(int(sys.stdin.readline()))


for tar in lis:
    if stack[-1] < tar:
        while(stack[-1] < tar):
            stack.append(cnt)
            res.append("+")
            cnt += 1
    
    if stack[-1] == tar:
        
        stack.pop()
        res.append("-")
            
    else:
        while(stack[-1] > tar):
            if stack.pop() in lis:
                print("NO")
                exit()
            res.append("-")

for x in res:
    print(x)
    


#17298
from collections import deque
import sys

num = int(sys.stdin.readline().rstrip())
lis = list(map(int,sys.stdin.readline().split()))
stack = deque()
stack.append(0)
res = [-1] * num

for x in range(1, num):
    while(stack and lis[stack[-1]] < lis[x]):
        res[stack.pop()] = lis[x]
    stack.append(x)
print(*res)