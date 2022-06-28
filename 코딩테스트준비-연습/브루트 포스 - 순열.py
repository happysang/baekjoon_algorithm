# 2529번 - 부등호
n = int(input())
cals = list(input().split())

import copy
ans = []
def sol(lis,t):
    if t == n:
        temp = copy.deepcopy(lis)
        ans.append(temp)
        return
    else:
        for i in range(10):
            if cals[t] == '>' and lis[-1] > i and i not in lis:
                lis.append(i)
                sol(lis, t+1)
                lis.pop()
            if cals[t] == '<' and lis[-1] < i and i not in lis:
                lis.append(i)
                sol(lis, t+1)
                lis.pop()

for i in range(10):
    temp = [i]
    sol(temp,0)
    temp.pop()
    
print(''.join(map(str,ans[-1])))
print(''.join(map(str,ans[0])))


# 1339번 - 단어 수학
from collections import defaultdict
nums = defaultdict(int)

n = int(input())

for _ in range(n):
    temp = list(input())
    temp.reverse()
    for i in range(len(temp)):
        nums[temp[i]] += 10**(i)

nums = sorted(nums.items(),key=lambda x:x[1], reverse=True)

res = 0
w = 9
for i in range(len(nums)):
    res += nums[i][1] * (w-i)
    
print(res)


# 14888번 - 연산자 끼워넣기
n = int(input())
nums = list(map(int, input().split()))
pl, mi, mu, di = map(int, input().split())


ans = []
def sol(i, res, pl, mi, mu, di):
    if i == n:
        ans.append(res)
        return() 
    
    if pl:
        temp = res + nums[i]
        sol(i+1, temp, pl-1, mi, mu, di)
    if mi:
        temp = res - nums[i]
        sol(i+1, temp, pl, mi-1, mu, di)
    if mu:
        temp = res * nums[i]
        sol(i+1, temp, pl, mi, mu-1, di)
    if di:
        if res >= 0:
            temp = res//nums[i]
            sol(i+1, temp, pl, mi, mu, di-1)
        else:
            temp = -(abs(res)//nums[i])
            sol(i+1, temp, pl, mi, mu, di-1)
    
    
sol(1,nums[0], pl, mi, mu, di)

print(max(ans))
print(min(ans))


# 14889번 - 스타트와 링크
from itertools import combinations

n = int(input())
p = []
for _ in range(n):
    p.append(list(map(int, input().split())))


cc = list(combinations(range(n), n//2))
nums = []
for i in range(len(cc)//2):
    nums.append([cc[i],cc[-1-i]])

ans = 99999999
for n in nums:
    res1 = 0
    res2 = 0
    temp1 = list(combinations(n[0],2))
    temp2 = list(combinations(n[1],2))
    
    for t,k in zip(temp1,temp2):
        res1 += p[t[0]][t[1]] + p[t[1]][t[0]]
        res2 += p[k[0]][k[1]] + p[k[1]][k[0]]
    ans = min(ans, abs(res1-res2))
    
print(ans)