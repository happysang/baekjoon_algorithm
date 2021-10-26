# 1978번
num = int(input())
lis = list(map(int, input().split()))
count = 0
for x in lis:
    check = True
    if x == 1:
        continue
    for y in range(2,x):
        if x % y == 0:
            check = False
            break
    if check:
        count += 1
print(count)


# 2581번
import math
num1 = int(input())
num2 = int(input())
res = []

for x in range(num1, num2+1):
    check = True
    if x == 1:
        continue
    for y in range(2,int(math.sqrt(x))+1):
        if x % y == 0:
            check = False
            break
    if check:
        res.append(x)
if len(res) == 0:
    print(-1)
else:
    print(sum(res))
    print(res[0])




# 11653번



# 1929번



# 4948번



# 9020번



# 1085번



# 3009번



# 4153번



# 3053번



# 1002번