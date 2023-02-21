### 2156
n = int(input())

nums =[]
for _ in range(n):
    nums.append(int(input()))
    
res = [0 for _ in range(n)]
visit = [1 for _ in range(n)] # 마시지 않은 경우를 1 마신 경우를 0으로 설정

for i in range(n):
    if i == 0 : # 잔이 1개 인 경우
        res[i] = nums[i]
        visit[i] = 0
    elif i == 1: # 잔이 2개인 경우
        res[i] = res[i-1] + nums[i]
        visit[i] = 0
    else:
        if visit[i-1] == 0 and visit[i-2] == 0:
            res[i] = max(res[i-1], res[i-2]+nums[i], res[i-3]+nums[i-1]+nums[i])            
            if res[i] == res[i-1]:
                pass
            elif res[i] == res[i-2]+nums[i]:
                visit[i-1] = 1
                visit[i] = 0
            else:
                visit[i-2] = 1
                visit[i] = 0
                
        else:
            res[i] = res[i-1]+nums[i]
            visit[i] = 0
print(res[-1])