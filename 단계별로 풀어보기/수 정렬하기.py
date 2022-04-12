# 2750번
num = int(input())

lis = []
for x in range(num):
    lis.append(int(input()))
    
lis.sort()

for x in lis:
    print(x)



# 2751번
import sys
num = int(sys.stdin.readline())

lis = []
for x in range(num):
    lis.append(int(sys.stdin.readline()))

for x in sorted(lis):
    print(x)



# 10989번
import sys
from collections import defaultdict

num = int(sys.stdin.readline())
dic = defaultdict(int)
for x in range(num):
    dic[int(sys.stdin.readline())] += 1
    
for x in range(10001):
    if dic[x] != 0:
        for _ in range(dic[x]):
            print(x)



# 2108번
import sys
from collections import defaultdict
num = int(sys.stdin.readline())
nums = []

for x in range(num):
    nums.append(int(sys.stdin.readline()))

print(round(sum(nums)/num))
print(sorted(nums)[num//2])

dic_nums = defaultdict(int)
for x in sorted(nums):
    dic_nums[x]+=1
temp = []
for k,v in dic_nums.items():
    if v == max(list(dic_nums.values())):
        temp.append(k)

if len(temp) == 1:
    print(temp[0])
else:
    print(temp[1])
    
print(max(nums) - min(nums))



# 1427번
import sys

num = list(sys.stdin.readline().strip())
print(''.join(reversed(sorted(num))))



# 11650번
import sys
num = int(sys.stdin.readline().strip())
lis = []
for x in range(num):
    lis.append(list( map(int,sys.stdin.readline().split()) ))
    
for x in sorted(lis):
    print(x[0], x[1])
    


# 11651번
import sys
num = int(sys.stdin.readline().strip())
lis = []
for x in range(num):
    temp = list(map(int,sys.stdin.readline().split()))
    lis.append([temp[1],temp[0]])
    
for x in sorted(lis):
    print(x[1], x[0])



# 1181번
import sys
num = int(sys.stdin.readline())

s = set()
for x in range(num):
    s.add(sys.stdin.readline().strip())

lis = list(sorted(s,key = len))
lis.append("")

temp,res = [],[]
for x in range(len(lis)-1):
    if len(lis[x]) == len(lis[x+1]):
        temp.append(lis[x])
    else:
        if len(temp) == 0:
            res.append(lis[x])
        else:
            temp.append(lis[x])
            for i in sorted(temp):
                res.append(i)
            temp.clear()

for x in res:
    print(x)
    


# 10814번
import sys
num = int(sys.stdin.readline())

lis = []
for x in range(num):
    n1, n2 = sys.stdin.readline().split()
    temp = [int(n1), n2, x]
    lis.append(temp)

for i in sorted(lis, key= lambda x : (x[0], x[2]) ):
    print(i[0], i[1])
    


# 18870번
import sys
from collections import defaultdict
num = int(sys.stdin.readline())

lis = list(map(int, sys.stdin.readline().split()))

s_lis = sorted(lis)
s_lis.append(1000000001)

count = 0
for x in range(num):
    if s_lis[x] != s_lis[x+1]:
        s_lis[x] = [s_lis[x], count]
        count += 1
    else:
        s_lis[x] = [s_lis[x], count]
del s_lis[-1]

dic = defaultdict(int)
for x in s_lis:
    dic[x[0]] = x[1]
    
        
res = []
for x in lis:
    res.append(dic[x])
    
print(res)