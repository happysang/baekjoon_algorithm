# 15988번 - 1, 2, 3 더하기 3
import sys
input = sys.stdin.readline
ans = [0] * 1000001
ans[1] = 1
ans[2] = 2
ans[3] = 4

for i in range(4,len(ans)):
     ans[i] = ans[i-3]% 1000000009 + ans[i-2]% 1000000009 + ans[i-1]% 1000000009


n = int(input())
for _ in range(n):
    tar = int(input())
    print(ans[tar] % 1000000009)



# 1149번 - RGB거리
import sys
input = sys.stdin.readline

n = int(input())

res = [[0,0,0] for _ in range(n+1)]

for i in range(1,n+1):
    r, g, b = map(int, input().split())
    
    res[i][0] = min(res[i-1][1]+r , res[i-1][2]+r)
    res[i][1] = min(res[i-1][0]+g , res[i-1][2]+g)
    res[i][2] = min(res[i-1][0]+b , res[i-1][1]+b)
    
print(min(res[-1]))



# 1309번 - 동물원
n = int(input())
ans = [[0] * 3 for i in range(100001)]
ans[1] = [1,1,1]

for i in range(2, 100001):
    ans[i][0] = ans[i - 1][1] % 9901 + ans[i - 1][2] % 9901
    ans[i][1] = ans[i - 1][0] % 9901 + ans[i - 1][2] % 9901
    ans[i][2] = ans[i - 1][0] % 9901 + ans[i - 1][1] + ans[i - 1][2] % 9901

print(sum(ans[n]) % 9901)



# 11057번 - 오르막 수
n = int(input())
ans = [[0,0,0,0,0,0,0,0,0,0] for _ in range(n+1)]

ans[1] = [1,1,1,1,1,1,1,1,1,1]

for i in range(2,n+1):
    temp = 0
    for j in range(10):
        for k in range(10):
            if k >= j:
                ans[i][k] += ans[i-1][j] % 10007

print(sum(ans[-1]) % 10007)



# 2156번 - 포도주 시식
# 1932번 - 정수 삼각형
n = int(input())
nums = []

for i in range(n):
    nums.append(list(map(int,input().split())))
nums.reverse()

res = nums[0]
for i in range(1,n):
    for j in range(len(nums[i])):
        nums[i][j] += max(res[j], res[j+1])
    res = nums[i]
    
print(*nums[-1])



# 11055번 - 가장 큰 증가 부분 수열
import copy
n = int(input())
nums = list(map(int,input().split()))
res = copy.deepcopy(nums)

for i in range(1,len(nums)):
    for j in range(i):
        if nums[i] > nums[j]:
            res[i] = max( res[i] , res[j]+nums[i] )

print(max(res))



# 11722번 - 가장 긴 감소하는 부분 수열
n = int(input())
nums = list(map(int,input().split()))
res = [1] * n

for i in range(1,len(nums)):
    for j in range(i):
        if nums[i] < nums[j]:
            res[i] = max( res[i] , res[j]+1 )

print(max(res))



# 11054번 - 가장 긴 바이토닉 부분 수열
n = int(input())
nums = list(map(int,input().split()))
res1 = [1] * n
res2 = [1] * n

for i in range(1,len(nums)):
    for j in range(i):
        if nums[i] > nums[j]:
            res1[i] = max( res1[i] , res1[j]+1 )

nums.reverse()
for i in range(1,len(nums)):
    for j in range(i):
        if nums[i] > nums[j]:
            res2[i] = max( res2[i] , res2[j]+1 )
res2.reverse()

ans = 0
for i in range(len(res1)):
    ans = max(ans, res1[i]+res2[i]-1)
    
print(ans)



# 13398번 - 연속합 2
# 2133번 - 타일 채우기