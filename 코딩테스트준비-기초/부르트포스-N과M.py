# 15649번 - N과 M (1)
import sys
n, m = map(int, sys.stdin.readline().split())

def sol(res):
    if len(res) == m:
        print(' '.join(map(str,res)))
        return
    else:
        for i in range(1,n+1):
            if i not in res:
                res.append(i)
                sol(res)
                res.pop()
sol([])


# 15650번 - N과 M (2)
import sys
n, m = map(int, sys.stdin.readline().split())

def sol(res):
    if len(res) == m+1:
        print(' '.join(map(str,res[1:])))
        return
    else:
        for i in range(1,n+1):
            if i not in res and res[-1] < i:
                res.append(i)
                sol(res)
                res.pop()
sol([0])



# 15651번 - N과 M (3)
import sys
n, m = map(int, sys.stdin.readline().split())

def sol(lis):   
    if len(lis) == m:
        print(' '.join(map(str,lis)))
        return
    else:
        for i in range(1,n+1):
            lis.append(i)
            sol(lis)
            lis.pop()
sol([])


# 15652번 - N과 M (4)
import sys
n, m = map(int, sys.stdin.readline().split())

def sol(lis):   
    if len(lis) == m+1:
        print(' '.join(map(str,lis[1:])))
        return
    else:
        for i in range(1,n+1):
            if lis[-1] <= i:
                lis.append(i)
                sol(lis)
                lis.pop()
sol([0])


# 15654번 - N과 M (5)
import sys
n, m = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))

def sol(lis):   
    if len(lis) == m:
        print(' '.join(map(str,lis)))
        return
    else:
        for i in nums:
            if i not in lis:
                lis.append(i)
                sol(lis)
                lis.pop()
sol([])


# 15655번 - N과 M (6)
import sys
n, m = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))

def sol(lis):   
    if len(lis) == m+1:
        print(' '.join(map(str,lis[1:])))
        return
    else:
        for i in nums:
            if lis[-1] < i:
                lis.append(i)
                sol(lis)
                lis.pop()
sol([0])


# 15656번 - N과 M (7)
import sys
n, m = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))

def sol(lis):   
    if len(lis) == m:
        print(' '.join(map(str,lis)))
        return
    else:
        for i in nums:
            lis.append(i)
            sol(lis)
            lis.pop()
sol([])


# 15657번 - N과 M (8)
import sys
n, m = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))

def sol(lis):   
    if len(lis) == m+1:
        print(' '.join(map(str,lis[1:])))
        return
    else:
        for i in nums:
            if lis[-1] <= i:
                lis.append(i)
                sol(lis)
                lis.pop()
sol([0])



# 18290번 - NM과 K (1)
