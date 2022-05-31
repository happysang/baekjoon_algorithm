# 1463번 - 1로 만들기
n = int(input())

if n == 1:
    print(0)
elif n == 2 or n == 3:
    print(1)

else:
    res = [0] * (n+1)
    res[2] = 1
    res[3] = 1
    for x in range(4,n+1):
        if x % 3 == 0:
            res[x] = min(res[x//3]+1, res[x-1]+1)
        if x % 2 == 0:
            if res[x] == 0:
                res[x] = min(res[x//2]+1, res[x-1]+1)
            else:
                res[x] = min(res[x//2]+1, res[x])
        if x%3 != 0 and x%2 != 0:
            res[x] = res[x-1]+1 
    print(res[-1])


# 11726번 - 2×n 타일링
n = int(input())
res = [0] * 1001

res[1] = 1
res[2] = 2 

for i in range(3,n+1):
    res[i] = res[i-1] + res[i-2]
        
print(res[n] % 10007)


# 11727번 - 2×n 타일링 2
n = int(input())
res = [0] * 1001

res[1] = 1
res[2] = 3

for i in range(3,n+1):
    res[i] = res[i-1] + res[i-2]*2
    
print(res[n] % 10007)


# 9095번 - 1, 2, 3 더하기
nums = [0] * 11
nums[1],nums[2],nums[3] = 1,2,4
for i in range(4,11):
    nums[i] = nums[i-3] + nums[i-2] + nums[i-1]
    
t = int(input())
for _ in range(t):
    tar = int(input())
    print(nums[tar])
    
    
    
# 11052번 - 카드 구매하기
n = int(input())
nums = [0] + list(map(int,input().split()))
res = [0] *(n+1)


res[1] = nums[1]
for i in range(2,n+1):
    for j in range(i+1):
        if res[i] < res[i-j]+nums[j]:
            res[i] = res[i-j]+nums[j]
            
            
print(res[-1])



# 16194번 - 카드 구매하기 2
n = int(input())
nums = [0]+list(map(int,input().split()))
res = [0] + [10001] * (n)

res[1] = nums[1]
for i in range(2,n+1):
    for j in range(i+1):
        if res[i] > res[i-j] + nums[j]:
            res[i] = res[i-j] + nums[j]
            
print(res[-1])



# 15990번 - 1, 2, 3 더하기 5
t = int(input())

nums = []
for _ in range(t):
    nums.append(int(input()))
    
res = [[0 for _ in range(3)] for _ in range(max(nums)+1)]

res[1] = [1,0,0]
res[2] = [0,1,0]
res[3] = [1,1,1]

for i in range(4, max(nums)+1):
    res[i][0] = res[i-1][1] % 1000000009 + res[i-1][2] % 1000000009
    res[i][1] = res[i-2][0] % 1000000009 + res[i-2][2] % 1000000009
    res[i][2] = res[i-3][0] % 1000000009 + res[i-3][1] % 1000000009
    

for k in nums:
    print(sum(res[k])% 1000000009)
    
    
    
# 10844번 - 쉬운 계단 수
n = int(input())

res = [[0 for _ in range(10)] for _ in range(n+1)]

res[1] = [0,1,1,1,1,1,1,1,1,1]


for i in range(2,n+1):
    for j in range(10):
        if j == 0:
            res[i][j] = res[i-1][1] % 1000000000
        elif j == 9:
            res[i][j] = res[i-1][8] % 1000000000
        else:
            res[i][j] = (res[i-1][j-1]) % 1000000000 + (res[i-1][j+1]) % 1000000000
            
print(sum(res[-1]) % 1000000000)



# 2193번 - 이친수
n = int(input())
res = [[0,0] for _ in range(n+1)]
res[1] = [0,1]


for i in range(2, n+1):
    res[i][0] = res[i-1][0] + res[i-1][1]
    res[i][1] = res[i-1][0]
    
    
print(sum(res[-1]))



# 11053번 - 가장 긴 증가하는 부분 수열
n = int(input())
nums = [0] + list(map(int,input().split()))
res = [0] + [1 for _ in range(n)]

for i in range(2,n+1):
    for j in range(1,i+1):
        if nums[i] > nums[j]:
            res[i] = max(res[i], res[j]+1)

print(max(res))


# 14002번 - 가장 긴 증가하는 부분 수열 4
n = int(input())
nums = [0] + list(map(int,input().split()))
res = [1 for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,i+1):
        if nums[j] < nums[i]:
            res[i] = max(res[i], res[j]+1)

ans = max(res)
ans2 = []
for i in range(n,0,-1):
    if res[i] == ans:
        ans2.append(nums[i])
        ans -= 1

print(max(res))   
print(*reversed(ans2))



# 1912번 - 연속합
n = int(input())

nums = list(map(int, input().split()))
res = [0] * len(nums)
res[0] = nums[0]

for i in range(1,n):
    res[i] = max (nums[i], res[i-1]+nums[i])
    
print(max(res))



# 1699번 - 제곱수의 합
n = int(input())

tar = [i * i for i in range(1, 317)]
res = [0 for i in range(n+1)]

for i in range(1, n+1):
    
    if i in tar:
        res[i] = 1
        continue
    else:
        temp = []
        for j in tar:
            if j > i:
                break
            else:
                temp.append(res[j]+res[i-j])
        res[i] = min(temp)
print(res[-1])



# 14501번 - 퇴사
import sys
input = sys.stdin.readline

n = int(input())
days = []
money = []

for _ in range(n):
    d, m = map(int, input().split())
    days.append(d)
    money.append(m)

res = [0]*(n+1)

for i in range(n-1, -1, -1):
    if i + days[i] > n:
        res[i] = res[i+1]
    else:
        res[i] = max( res[i+1], res[i+days[i]]+money[i] )
    
    print(res)

# 2225번 - 합분해