# 11723번 - 집합
import sys
input = sys.stdin.readline

t = int(input())

s = [0 for _ in range(21)]

for i in range(t):
    order = input().strip()
    if order[-1].isdigit():
        order, n = order.split()
        n = int(n)
    else:
        n = -1

    if order == 'add':
        if s[n] == 0:
            s[n] = 1
    elif order == 'remove':
        if s[n]:
            s[n] = 0
    elif order == 'check':
        if s[n]:
            print(1)
        else:
            print(0)
    elif order == 'toggle':
        if s[n]:
            s[n] = 0
        else:
            s[n] = 1
    elif order == 'all':
        s = [1 for _ in range(21)]
    elif order == 'empty':
        s = [0 for _ in range(21)]


# 1182번 - 부분수열의 합
# 14889번 - 스타트와 링크
# 14391번 - 종이 조각