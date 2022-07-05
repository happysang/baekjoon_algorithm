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
# 1208번 - 부분수열의 합 2
# 2143번 - 두 배열의 합