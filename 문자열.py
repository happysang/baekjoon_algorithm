#11654번
import sys
print(ord(sys.stdin.readline().strip()))



#11720번
import sys
num1 = sys.stdin.readline().strip()
num2 = sys.stdin.readline().strip()
print(sum([int(x) for x in num2]))



#10809번
from collections import defaultdict
d = defaultdict(str)
for x in range(97, 97+26):
    d[chr(x)] = str(-1)
s = input()

for idx,val in enumerate(s):
    if d[val] != "-1":
        continue
    d[val] = str(idx)
print(' '.join(d.values()))



#2675번
l = []
num = int(input())

for x in range(num):
    l.append(input().split())

for x in range(len(l)):
    res = ''
    for y in l[x][1]:
        for _ in range(int(l[x][0])):
            res += y
    print(res)



#1157번
from collections import defaultdict

s = input().upper()
d = defaultdict(int)
c = 0
for x in s:
    d[x] += 1

max_n = max(d.values())

for x in d.keys():
    if d[x] == max_n:
        res = x
        c += 1
if c == 1:
    print(res)
else:
    print("?")
    


#1157번 - 다른 사람의 좋은 풀이
n = input().upper()
nx = list(set(n))
cnt = []
for i in nx:
  cnt.append(n.count(i))

if cnt.count(max(cnt)) > 1:
  print('?')
else:
  print(nx[(cnt.index(max(cnt)))].upper())



#1152번
l = []
l.append(input().split())
print(len(l[0]))



#2908번
num1, num2 = input().split()
n1, n2 = int(''.join(list(reversed(num1)))), int(''.join(list(reversed(num2))))

res = n1 if n1 > n2 else n2
print(res)



#1316번
from collections import defaultdict

lis = []
res = 0
num = int(input())
for x in range(num):
    lis.append(input())

for s in lis:
    d = defaultdict(int)
    for i in range(len(s)):
        if i == 0:
            d[s[i]] += 1
        elif d[s[i]] != 0 and s[i] != s[i-1]:
            break
        else:
            d[s[i]] += 1
    if len(s) == sum(d.values()):
        res += 1
print(res)



# 2941번
import sys
lis = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
s = sys.stdin.readline().strip()
for x in lis:
    s= s.replace(x,'a')
print(len(s))



