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