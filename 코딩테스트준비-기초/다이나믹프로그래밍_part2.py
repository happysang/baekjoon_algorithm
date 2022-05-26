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
# 11055번 - 가장 큰 증가 부분 수열
# 11722번 - 가장 긴 감소하는 부분 수열
# 11054번 - 가장 긴 바이토닉 부분 수열
# 13398번 - 연속합 2
# 2133번 - 타일 채우기