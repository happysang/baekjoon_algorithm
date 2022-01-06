#11047번


#1931번


#11399번
num = int(input())
nums = list(map(int, input().split()))
nums.sort()
res = 0
for x in range(num):
    res += sum(nums)
    del nums[-1]
    
print(res)



#1541번


#13305번