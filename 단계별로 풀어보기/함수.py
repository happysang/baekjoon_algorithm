#15596번
def solve(a):
    ans = 0
    for x in a:
        ans += x
    return ans



#4673번
nums = [x for x in range(1,10001)]

def check(num):
    n_sum = num + sum([int(x) for x in str(num)])
    if n_sum in nums:
        nums.remove(n_sum)
    

for num in range(1,10001):
    check(num)

for x in nums:
    print(x)



# 1065번
num = input()
if int(num) <= 99:
    res = num
else:
    res = 99
    for n in range(100,int(num)+1):
        n = str(n)
        if int(n[2]) - int(n[1]) == int(n[1]) - int(n[0]):
            res += 1
print(res)