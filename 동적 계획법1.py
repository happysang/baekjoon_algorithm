# 1003번
import sys
res = [[0,0] for _ in range(41)]
nums = [0 for _ in range(41)]

def fibo(n):
    if n == 0:
        nums[0] = 0
        res[0][0] = 1
        return 0
    
    elif n == 1:
        nums[1] = 1
        res[1][1] = 1
        return 1
        
    elif nums[n] != 0:
        return nums[n]
    
    else:
        nums[n] = nums[n-1] + nums[n-2]
        res[n][0] = res[n-1][0] + res[n-2][0]
        res[n][1] = res[n-1][1] + res[n-2][1] 
        return fibo(n-1) + fibo(n-2)


num = int(sys.stdin.readline())
inp = []
for _ in range(num):
    inp.append(int(sys.stdin.readline()))
    
for i in range(max(inp)+1):
    fibo(i)
    
for i in inp:
    print(res[i][0], res[i][1])
    
    

# 9184번
def w(a,b,c):
    if  a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20,20,20)
    if dp[a][b][c]:
        return dp[a][b][c]
    
    if a < b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dp[a][b][c]
    
dp = [[[0]*(21) for _ in range(21)] for _ in range(21)]

while(True):
    a, b, c = map(int, input().split()) 
    if a==-1 and b==-1 and c==-1: 
        break
    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')


# 1904번



# 9461번



# 1149번
num = int(input())

nums = []
for x in range(num):
    nums.append(list(map(int, input().split())))
    
for i in range(1,num):
    temp = []
    for j in range(3):
        if j == 0:
            nums[i][j] += min(nums[i-1][1], nums[i-1][2])
        elif j ==1:
            nums[i][j] += min(nums[i-1][0], nums[i-1][2])
        else:
            nums[i][j] += min(nums[i-1][0], nums[i-1][1])
            
            
print(min(nums[-1]))



# 1932번
num = int(input())

nums = []
for x in range(num):
    nums.append(list(map(int, input().split())))

for i in range(1,num):
    for j in range(i+1):
        if j == 0:
            nums[i][j] += nums[i-1][j]
        elif j == i:
            nums[i][j] += nums[i-1][j-1]
        else:
            nums[i][j] += max(nums[i-1][j-1], nums[i-1][j])
            
print(max(nums[-1]))

        


# 2579번
import sys
num = int(input())

up = []
res = []
for _ in range(num):
    up.append(int(sys.stdin.readline()))
    
if num == 1:
    print(up[0])
elif num == 2:
    print(up[0] + up[1])
elif num == 3:
    print(max( up[0]+up[2] , up[1]+up[2] ))
else:
    res.append(up[0])
    res.append(up[0] + up[1])
    res.append(max( up[0]+up[2] , up[1]+up[2] ))

    for i in range(3,num):
        res.append(max( res[i-2]+up[i], res[i-3] + up[i-1] +up[i] ))
        
    print(res.pop())



# 1463번



# 10844번



# 2156번



# 11503번
num = int(input())
nums = list(map(int,input().split()))

res = [1] * num
for i in range(1,num):
    for j in range(i):
        if nums[i] > nums[j]:
            res[i] = max(res[i], res[j]+1)
            
print(max(res))



# 11054번
num = int(input())

nums = list(map(int, input().split()))
reverse_nums = nums[::-1]

increase = [1] *(num)
decrease = [1] *(num)

for i in range(num):
    for j in range(i):
        if nums[i] > nums[j]:
            increase[i] = max(increase[i], increase[j]+1)
        if reverse_nums[i] > reverse_nums[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)
    
res = []
decrease = decrease[::-1]
for x in range(num):
    res.append(increase[x] + decrease[x] - 1)
print(max(res))



# 2565번
num = int(input())

lis = []
for _ in range(num):
    lis.append(list(map(int, input().split())))

lis.sort()
nums = [lis[x][1] for x in range(num)]

res = [1]*num
for i in range(num):
    for j in range(i):
        if nums[i] > nums[j]:
            res[i] = max(res[j]+1, res[i])

print(num - max(res))



# 9251번



# 1912번



# 12865번