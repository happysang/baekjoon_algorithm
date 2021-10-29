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
num = int(input())

if num == 1:
    pass
else:
    for x in range(2,num+1):
        if num % x == 0:
            while True:
                if num % x == 0:  
                    print(x)
                    num = num//x
                else:
                    break



# 1929번
from math import sqrt
a,b = map(int, input().split())

for x in range(a,b+1):
    flag = True
    if x == 1:
        continue
    if x == 2 or x == 3:
        print(x)
        continue

    for y in range(2,int(sqrt(x))+1):
        if x % y == 0:
            flag = False
            break
    
    if flag:
        print(x)


# 4948번
lis = [True for _ in range(123456*2+1)]
for x in range(2,int(246912**0.5)):
    for y in range(2,(123456*2)//x+1):
        lis[x*y] = False

res = []
while True:
    count = 0
    num = int(input())
    if num == 0:
        break
    for x in range(num+1, 2*num+1):
        if lis[x] == True:
            count += 1
    res.append(count)

for x in res:
    print(x)
    


# 9020번 @@@@@중요! 시간이 오래 걸릴 때는 list 말고 set을 활용하자!
lis = [True for _ in range(10000+1)]
for x in range(2,int(10000**0.5)+1):
    for y in range(2,10000//x+1):
        lis[x*y] = False

n = set()
for x in range(2,10001):
    if lis[x] == True:
        n.add(x)

for _ in range(int(input())):
    num = int(input())
    a, b = 0, 0
    gap = 10000
    for x in n:
        temp = num - x
        if temp in n:
            if gap > abs(temp-x):
                gap = abs(temp-x)
                if temp >= x:
                    a,b = x, temp
                else:
                    a,b = temp, x
    print(a,b)



# 1085번
x,y,w,h = map(int ,input().split())

if w/2 > x:
    min_x = x
else:
    min_x = w-x

if h/2 > y:
    min_y = y
else:
    min_y = h-y

print(min(min_x, min_y))




# 3009번
from collections import defaultdict

num = defaultdict(int)
front = defaultdict(int)
for x in range(3):
    a,b = map(int, input().split())
    front[a] += 1
    num[a] += 1
    num[b] += 1

for k,v in front.items():
    if v == 1:
        a = k
        num[a] += 1

for k,v in num.items():
    if v % 2 ==1:
        b = k

print(a,b)



# 4153번
while True:
    nums = list(map(int, input().split()))
    a = max(nums)
    if a == 0:
        break
    nums.remove(max(nums))

    if a**2 == nums[0]**2 + nums[1]**2:
        print("right")
    else:
        print("wrong")



# 3053번



# 1002번