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
#풀이1)
def check(num):
    res = []
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    for e in range(10):
                        for f in range(10):
                            if num == int(str(a)+str(b)+str(c)+str(d)+str(e)+str(f))+a+b+c+d+e+f:
                                return int(str(a)+str(b)+str(c)+str(d)+str(e)+str(f))
    return 0

print( check(int(input())) )

#풀이2
def check(n):
    min_n = n - len(str(n))*9
    for x in range(min_n, n):
        if x < 0:
            continue
        s = x
        for i in str(x):
            s += int(i)
        if s == n:
            return x
    return 0
print(check(int(input())))




# 7568번




# 1018번




# 1436번