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



# 1904번



# 9461번



# 1149번



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




# 1463번



# 10844번



# 2156번



# 11054번



# 2565번



# 9251번



# 1912번



# 12865번