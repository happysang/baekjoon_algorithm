# 2798번
n,m = map(int, input().split())
nums = list(map(int, input().split()))

if n == 3:
    print(sum(nums))

gap = 300001
for x in range(n-2):
    for y in range(x+1,n-1):
        for z in range(y+1,n):
            if m - (nums[x]+nums[y]+nums[z]) < 0:
                continue
            if gap > m - (nums[x]+nums[y]+nums[z]):
                gap = m - (nums[x]+nums[y]+nums[z])
                res = nums[x]+nums[y]+nums[z]
print(res)



# 2231번




# 7568번




# 1018번




# 1436번