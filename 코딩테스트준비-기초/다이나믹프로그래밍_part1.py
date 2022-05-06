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
# 16194번 - 카드 구매하기 2
# 15990번 - 1, 2, 3 더하기 5
# 10844번 - 쉬운 계단 수
# 2193번 - 이친수
# 11053번 - 가장 긴 증가하는 부분 수열
# 14002번 - 가장 긴 증가하는 부분 수열 4
# 1912번 - 연속합
# 1699번 - 제곱수의 합
# 14501번 - 퇴사
# 2225번 - 합분해