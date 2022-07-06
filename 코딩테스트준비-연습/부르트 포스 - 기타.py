# 2003번 - 수들의 합 2
n, m = map(int,input().split())
nums = list(map(int,input().split()))

l,r = 0,1
res = 0
while l<=r and r<n+1:
    tar = sum(nums[l:r])
    if tar < m:
        r += 1
    elif tar == m:
        res += 1
        r += 1
    elif tar > m:
        l += 1
        
print(res)


# 1806번 - 부분합
n, m = map(int,input().split())
nums = list(map(int,input().split()))


if sum(nums) < m:
    print(0)
else:
    l,r = 0,0
    res = n+1
    temp = nums[l]
    while True:
        if temp < m:
            r += 1
            if r<n:
                temp += nums[r]
            else:
                break
        elif temp >= m:
            res = min(res, r-l+1)
            temp -= nums[l]
            if l<=r:
                l += 1
            else:
                break
    print(res)



# 1644번 - 소수의 연속합
n = int(input())
if n == 1:
    print(0)
    exit()

nums = [True for _ in range(n+1)]
nums[0] = False
nums[1] = False

for i in range(2, int(n**0.5)+1):
    if nums[i]:
        t = 2
        
    while i*t < n+1:
        nums[i*t] = False
        t += 1
        
pn = []
for i in range(n+1):
    if nums[i]:
        pn.append(i)
        

l,r,res = 0,0,0
tar = pn[l]

while(l<=r):
    if tar == n:
        res += 1
        tar -= pn[l]
        l+=1
        
    elif tar > n:
        tar -= pn[l]
        l+= 1
        
    elif tar < n:
        r+=1
        if r<len(pn):
            tar += pn[r]
        else:
            break
        
print(res)


# 1208번 - 부분수열의 합 2
# 2143번 - 두 배열의 합