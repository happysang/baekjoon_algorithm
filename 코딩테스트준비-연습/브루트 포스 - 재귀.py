# 6603번 - 로또
from itertools import combinations

while(True):
    t = input()
    if t == "0":
        exit()
    else:
        nums = list(map(int,t.split()))
        k = nums[0]
        nums = nums[1:]
        lis = list(combinations(nums,6))
        for l in lis:
            print(*l)
    print()
    
    
# 1182번 - 부분수열의 합
from itertools import combinations

n,s = map(int,input().split())
nums = list(map(int,input().split()))

cnt = 0
for i in range(1,n+1):
    lis = list(combinations(nums, i))
    for l in lis:
        if sum(l) == s:
            cnt += 1
            
print(cnt)


# 14225번 - 부분수열의 합
from itertools import combinations

n = int(input())
nums = list(map(int, input().split()))


res = []
for i in range(1,n+1):
    temp = list(map(sum,combinations(nums,i)))
    res += temp
    
res = sorted(list(set(res)))

for i in range(len(res)):
    if res[i] == i+1:
        continue
    else:
        print(i+1)
        exit()

print(res[-1]+1)


# 14888번 - 연산자 끼워넣기
n = int(input())
nums = list(map(int, input().split()))
pl, mi, mu, di = map(int, input().split())

ans = []
def sol (deep, res, pl, mi, mu, di):
    if deep == n:
        ans.append(res)
        return
    if pl:
        sol(deep+1, res+nums[deep],pl-1,mi,mu,di)
    if mi:
        sol(deep+1, res-nums[deep],pl,mi-1,mu,di)
    if mu:
        sol(deep+1, res*nums[deep],pl,mi,mu-1,di)
    if di:
        if res >=0:
            sol(deep+1, res//nums[deep],pl,mi,mu,di-1)
        else:
            sol(deep+1, -(abs(res)//nums[deep]),pl,mi,mu,di-1)
            
            
sol(1,nums[0],pl,mi,mu,di)

print(max(ans))
print(min(ans))



# 15658번 - 연산자 끼워넣기 (2)
n = int(input())
nums = list(map(int, input().split()))
pl, mi, mu, di = map(int, input().split())

ans = []
def sol (deep, res, pl, mi, mu, di):
    if deep == n:
        ans.append(res)
        return
    if pl:
        sol(deep+1, res+nums[deep],pl-1,mi,mu,di)
    if mi:
        sol(deep+1, res-nums[deep],pl,mi-1,mu,di)
    if mu:
        sol(deep+1, res*nums[deep],pl,mi,mu-1,di)
    if di:
        if res >=0:
            sol(deep+1, res//nums[deep],pl,mi,mu,di-1)
        else:
            sol(deep+1, -(abs(res)//nums[deep]),pl,mi,mu,di-1)
            
            
sol(1,nums[0],pl,mi,mu,di)

print(max(ans))
print(min(ans))


# 14500번 - 테트로미노
# 16197번 - 두 동전
# 16198번 - 에너지 모으기
# 9663번 - N-Queen
# 2580번 - 스도쿠
# 4574번 - 스도미노쿠