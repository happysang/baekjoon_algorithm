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


#1157번 - 다른 사람의 좋은 풀이
if c == 1:
    print(res)
else:
    print("?")
    


n = input().upper()
nx = list(set(n))
cnt = []
for i in nx:
  cnt.append(n.count(i))

if cnt.count(max(cnt)) > 1:
  print('?')
else:
  print(nx[(cnt.index(max(cnt)))].upper())