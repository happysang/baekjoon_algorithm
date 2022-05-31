# 10845번 - 큐
from collections import deque
import sys

n = int(sys.stdin.readline().strip())

l = deque()
for _ in range(n):
    s = sys.stdin.readline().strip()
    if "push" in s:
        s, num = s.split()
        num = int(num)
        l.append(num)
        
    elif s == "pop":
        if l:
            print(l.popleft())
        else:
            print(-1)
        
    elif s == "size":
        print(len(l))
        
    elif s == "empty":
        if len(l) != 0:
            print(0)
        else:
            print(1)
            
    elif s == "front":
        if len(l) != 0:
            print(l[0])
        else:
            print(-1)
            
    elif s == "back":
        if len(l) != 0:
            print(l[-1])
        else:
            print(-1)



# 10866번 - 덱
from collections import deque
import sys

n = int(sys.stdin.readline().strip())

l = deque()
for _ in range(n):
    
    s = sys.stdin.readline().strip()
    
    if "push" in s:
        s, num = s.split()
        num = int(num)
        if "front" in s:
            l.appendleft(num)
        else:
            l.append(num)
        
    elif s == "pop_front":
        if len(l) != 0:
            print(l.popleft())
        else:
            print(-1)
    
    elif s == "pop_back":
        if len(l) != 0:
            print(l.pop())
        else:
            print(-1)    
    
    elif s == "size":
        print(len(l))
        
    elif s == "empty":
        if len(l) != 0:
            print(0)
        else:
            print(1)
            
    elif s == "front":
        if len(l) != 0:
            print(l[0])
        else:
            print(-1)
            
    elif s == "back":
        if len(l) != 0:
            print(l[-1])
        else:
            print(-1)
            
            
            
# 13023번 - ABCDE
# 1260번 - DFS와 BFS
# 11724번 - 연결 요소의 개수
# 1707번 - 이분 그래프
# 2667번 - 단지번호붙이기
# 2178번 - 미로 탐색
# 7576번 - 토마토
# 7562번 - 나이트의 이동