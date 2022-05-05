# 11723번 - 집합
import sys
input = sys.stdin.readline

t = int(input())

s = [0 for _ in range(21)]

for i in range(t):
    order = input().strip()
    if order[-1].isdigit():
        order, n = order.split()
        n = int(n)
    else:
        n = -1

    if order == 'add':
        if s[n] == 0:
            s[n] = 1
    elif order == 'remove':
        if s[n]:
            s[n] = 0
    elif order == 'check':
        if s[n]:
            print(1)
        else:
            print(0)
    elif order == 'toggle':
        if s[n]:
            s[n] = 0
        else:
            s[n] = 1
    elif order == 'all':
        s = [1 for _ in range(21)]
    elif order == 'empty':
        s = [0 for _ in range(21)]


# 1182번 - 부분수열의 합
import sys,itertools
input = sys.stdin.readline


n, s = map(int,input().split())
nums = list(map(int,input().split()))

ans = 0
for i in range(1,n+1):
    res = itertools.combinations(nums,i)
    for c in res:
        temp = sum(c)
        if temp == s:
            ans +=1
            
print(ans)



# 14889번 - 스타트와 링크
import sys
input = sys.stdin.readline

n = int(input())
nums = []

for i in range(n):
    nums.append(list(map(int, input().split())))

test = []
def combination(lis,tar,res):
    if tar == 0:
        test.append(res[1:])
    else:
        for i in lis:
            if res.count(i) == 0 and res[-1]<i:
                res.append(i)
                combination(lis,tar-1,res)
                res.pop()


combination(list(range(n)), n//2, [-1] )

gap = 101       
for i in range(len(test)//2):
    team1 = 0
    for x in test[i]:
        for y in test[i]:
            team1 += nums[x][y]
    
    
    team2 = 0
    for x in test[-1-i]:
        for y in test[-1-i]:
            team2 += nums[x][y]
            
    gap = min (gap, abs(team1-team2))
    
print(gap)


# 14391번 - 종이 조각