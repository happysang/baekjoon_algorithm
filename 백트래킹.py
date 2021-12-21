#15649번
n,m = list(map(int,input().split()))
a = []

def dfs():
    if len(a) == m:
        print(' '.join(map(str,a)))
        return
    
    else:
        for i in range(1,n+1):
            if i not in a:
                a.append(i)
                dfs()
                a.pop()
dfs()



#15650번
n,m = list(map(int,input().split()))
res = []
res_list = []

def check():
    if len(res) == m:
        if sorted(res) not in res_list:
            res_list.append(sorted(res))
            print(' '.join(map(str,sorted(res))))
        return
    
    for i in range(1,n+1):
        if i not in res:
            res.append(i)
            check()
            res.pop()
check()



#15651번
n,m = list(map(int,input().split()))
res = []

def check():
    if len(res) == m:
        print(' '.join(map(str,res)))
        return
    
    else:
        for i in range(1,n+1):
            res.append(i)
            check()
            res.pop()
check()



#15652번
n,m = list(map(int,input().split()))
res = []

def check():
    if len(res) == m:
        print(' '.join(map(str,res)))
        return
    
    else:
        for i in range(1,n+1):
            if len(res) == 0 or res[-1] <= i:
                res.append(i)
                check()
                res.pop()
check()




#9663번
answer = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]
print(answer[int(input())])


# 파이썬으로 시간복잡도를 통과할 수 없음..
def check(x):
    for i in range(x):
        if col[x] == col[i] or abs(col[x] - col[i]) == x - i:
            return False
    return True
        
        
def dfs(x):
    global res
    
    if x == n:
        res += 1

    else:
        for i in range(n):
            col[x] = i
            if check(x):
                dfs(x + 1)


n = int(input())
col = [0] * n
res = 0
dfs(0)
print(res)



#2580번




#14888번
import sys

input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))

maximum = -1e9
mininum = 1e9

def dfs (depth, total ,plus, minus, mul, div):
    global maximum, mininum
    if depth == n:
        maximum = max(maximum, total)
        mininum = min(mininum, total)
        return
    
    if plus:
        dfs (depth + 1, total + num[depth], plus-1, minus, mul, div)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, mul, div)
    if mul:
        dfs(depth + 1, total * num[depth], plus, minus, mul - 1, div)
    if div:
        dfs(depth + 1, int(total / num[depth]), plus, minus, mul, div - 1)
        
dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maximum)
print(mininum)



#14889번
num = int(input())
res = set()
point = []
flag = [True]*num
for i in range(num):
    point.append(list(map(int, input().split())))


def dfs (depth,a,b,numflag,flag):
    if depth == num//2:
        print("!!",abs(a-b))
        res.add(abs(a-b))
        return
    if numflag:
        for i in range(num):
            for j in range(i,num):
                if i==j:
                    continue
                if flag[i] and flag[j]:
                    a = point[i][j] + point[j][i]
                    cflag = flag.copy()
                    cflag[i],cflag[j] = False,False
                    print(f'{numflag} i: {i} j: {j} depth: {depth} a: {a} b: {b}')
                    dfs(depth+1,a,b,False,cflag)
                
    else:
        for i in range(num):
            for j in range(i,num):
                if i==j:
                    continue
                if flag[i] and flag[j]:
                    b = point[i][j] + point[j][i]
                    cflag = flag.copy()
                    cflag[i],cflag[j] = False,False
                    print(f'{numflag} i: {i} j: {j} depth: {depth} a: {a} b: {b}')
                    dfs(depth+1,a,b,True,cflag)

dfs(0,0,0,True,flag)
print(min(res))

