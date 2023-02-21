###23971
h,w,n,m = map(int, input().split())

if h//(n+1) == h/(n+1):
    res1 = h//(n+1)
else:
    res1 = h//(n+1)+1
    
if w//(m+1) == w/(m+1):
    res2 = w//(m+1)
else:
    res2 = w//(m+1)+1

print(res1*res2)


### 5073
while(True):
    temp = sorted(list(map(int, input().split())))
    a,b,c = temp[0],temp[1],temp[2]
    
    if c == 0:
        exit()
    if a+b <= c:
        print("Invalid")
        continue
    
    if a == c:
        print("Equilateral")
    elif a == b or b == c:
        print("Isosceles")
    else:
        print("Scalene")

        
### 2292
n = int(input())

tar = 1
cnt = 1
while(tar<n):
    nums.append(tar+6*cnt)
    tar = tar+6*cnt
    cnt += 1
    
print(cnt)



### 1157
from collections import defaultdict
tar = input()

res = defaultdict(int)
for s in tar:
    s = s.upper()
    res[s] += 1
ans = sorted(list(res.items()), key=lambda x:x[1])

if len(ans)>1 and ans[-1][1] == ans[-2][1]:
    print("?")
else:
    print(ans[-1][0])
    

### 11723
import sys
input = sys.stdin.readline

n = int(input())
tar = []
for _ in range(n):
    s = input()
    if s == "all":
        tar = [i for i in range(1,21)]
    elif s == "empty":
        tar = []
    else:
        cmd, val = s.split()
        val = int(val)
        
        if cmd == "add" and val not in tar:
            tar.append(val)
        elif cmd == "remove" and val in tar:
            tar.remove(val)
        elif cmd == "check":
            if val in tar:
                print(1)
            else:
                print(0)
        elif cmd == "toggle":
            if val in tar:
                tar.remove(val)
            else:
                tar.append(val)
                
                
                
### 11723
import sys
input = sys.stdin.readline

n = int(input())
tar = [0 for _ in range(21)]

for _ in range(n):
    s = input().rstrip()
    if s == "all":
        tar = [1 for _ in range(21)]
    elif s == "empty":
        tar = [0 for _ in range(21)]
    else:
        cmd, val = s.split()
        val = int(val)
        
        if cmd == "add" and tar[val] == 0:
            tar[val] = 1
        elif cmd == "remove" and tar[val] == 1:
            tar[val] = 0
        elif cmd == "check":
            if tar[val]:
                print(1)
            else:
                print(0)
        elif cmd == "toggle":
            if tar[val]:
                tar[val] = 0
            else:
                tar[val] = 1
                
                
### 10431
n = int(input())

for k in range(1,n+1):
    s = list(map(int, input().split()))[1:]
    res = 0

    i = 1
    flag = False
    while(i<20):
        for j in range(i):
            if s[i]<s[j]:
                flag = True
                temp = s[i]
                del s[i]
                s = s[:j] + [temp] + s[j:]
                res += (i-j)
                break
        if flag :
            i = 1
        else:
            i += 1
        flag = False
    print(k, res)
    
    
    
### 8979
n,k = map(int, input().split())
res = []
for _ in range(n):
    res.append(list(map(int, input().split()))) 
res.sort(key = lambda x : (-x[1], -x[2], -x[3]))


ans = [0 for _ in range(n+1)]
ans[res[0][0]] = 1
temp = 0

for i in range(n):
    if res[i-1][1:] == res[i][1:]:
        ans[res[i][0]] = ans[res[i-1][0]]
        temp += 1
    else:
        ans[res[i][0]] = ans[res[i-1][0]]+temp+1
        temp = 0
    
    if res[i][0] == k:
        print(ans[k])
        exit()
        
        
        
### 7568
n = int(input())
nums = []

for i in range(n):
    lis = list(map(int, input().split()))
    nums.append(lis)

res = [1 for i in range(n)]

for i in range(n):
    for j in range(n):
        if nums[i][0] < nums[j][0] and nums[i][1] < nums[j][1]:
            res[i] += 1
            
print(*res)



### 4659
mo = list("aeiou")
ja = list("bcdfghjklnmpqrstvwxyz")

while(True):
    tar = input()
    if tar == "end":
        break
    
    if "a" not in tar and "e" not in tar and "i" not in tar and "o" not in tar and "u" not in tar:
        print(f'<{tar}> is not acceptable.')
        continue
    
    if len(tar) >=3:
        flag = False
        cmo,cja = 0,0
        for t in tar:
            if t in mo:
                cmo += 1
                cja = 0
            
            elif t in ja:
                cmo = 0
                cja += 1
                
            if cmo == 3 or cja == 3:
                print(f'<{tar}> is not acceptable.')
                flag = True
                break
        if flag:
            continue
        
    
    if len(tar) >= 2:
        flag2 = False
        for i in range(1,len(tar)):
            if tar[i] != 'e' and tar[i] != 'o' and tar[i-1] == tar[i]:
                flag2 = True
                print(f'<{tar}> is not acceptable.')
                break
            
        if flag2:
            continue
        
    print(f'<{tar}> is acceptable.')
    
    
### 25737
import sys
input = sys.stdin.readline

from itertools import combinations

n, t = input().split()
n = int(n)
temp = set()
for _ in range(n):
    temp.add(input())

if t == "Y":
    print(len(temp))
elif t == "F":
    print( len(temp)//2 ) 
else:
    print( len(temp)//3 )
    
    
    
### 1205
n, point, p = map(int, input().split())
# 점수 갯수, 태수의 점수, 랭킹 리스트에 올라 갈 수 있는 점수의 개수

if n == 0:
    print(1)
else:
    nums = list(map(int,input().split()))
    nums.append(point)
    nums.sort(reverse=True)

    res = [0 for _ in range(len(nums))]
    res[0] = 1

    temp = 0
    for i in range(1,len(nums)):
        if nums[i-1] == nums[i]:
            res[i] = res[i-1]
            temp += 1
        else:
            res[i] = res[i-1]+temp+1
            temp = 0
    # print(res)
    
    if (n==p and nums[p-1] > point) or (n==p and nums[p-1] == point and res[p-1] == res[p]):
        print(-1)
    else:
        print(res[nums.index(point)])
        
        
### 1244
n = int(input())
res = [-1]+list(map(int, input().split()))

for _ in range(int(input())):
    g, tar = map(int, input().split())
        
    if g == 1:
        temp = tar
        while(temp<=n):
            if res[temp]:
                res[temp] = 0
            else:
                res[temp] = 1
            temp += tar
    else:
        flag = 0
        while(1<=tar-flag and tar+flag<=n):
            if res[tar-flag] == res[tar+flag]:
                if res[tar-flag]:
                    res[tar-flag],res[tar+flag] = 0,0
                else:
                    res[tar-flag],res[tar+flag] = 1,1
            else:
                break
            
            flag += 1

if n<=20:
    print(*res[1:])
    
elif n<=40:
    print(*res[1:21])
    print(*res[21:])

elif n<=60:
    print(*res[1:21])
    print(*res[21:41])
    print(*res[41:])
    
elif n<=80:
    print(*res[1:21])
    print(*res[21:41])
    print(*res[41:61])
    print(*res[61:])
    
else:
    print(*res[1:21])
    print(*res[21:41])
    print(*res[41:61])
    print(*res[61:81])
    print(*res[81:])
    
    
    
### 9017
from collections import defaultdict

T = int(input())

for _ in range(T):
    n = int(input())
    nums = list(map(int, input().split()))
    temp = sorted(list(set(nums)))
    
    ap = []
    for t in temp:
        if nums.count(t) >= 6:
            ap.append(t)
            
    tar = []
    for v in nums:
        if v in ap:
            tar.append(v)
    
    res = defaultdict(list)
    for i in range(len(tar)):
        if len(res[tar[i]]) <= 4:
            res[tar[i]].append(i+1)
            
    ans = []
    for k,v in res.items():
        ans.append([k,sum(v[:4]),v[4]])
    ans.sort(key=lambda x:(x[1],x[2]))
    
    print(ans[0][0])