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



#2580번



#14888번



#14889번