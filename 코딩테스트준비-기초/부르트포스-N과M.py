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
# 15652번 - N과 M (4)
# 15654번 - N과 M (5)
# 15655번 - N과 M (6)
# 15656번 - N과 M (7)
# 15657번 - N과 M (8)
# 18290번 - NM과 K (1)