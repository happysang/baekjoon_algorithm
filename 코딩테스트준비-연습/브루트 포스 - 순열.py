# 2529번 - 부등호
n = int(input())
cals = list(input().split())

import copy
ans = []
def sol(lis,t):
    if t == n:
        temp = copy.deepcopy(lis)
        ans.append(temp)
        return
    else:
        for i in range(10):
            if cals[t] == '>' and lis[-1] > i and i not in lis:
                lis.append(i)
                sol(lis, t+1)
                lis.pop()
            if cals[t] == '<' and lis[-1] < i and i not in lis:
                lis.append(i)
                sol(lis, t+1)
                lis.pop()

for i in range(10):
    temp = [i]
    sol(temp,0)
    temp.pop()
    
print(''.join(map(str,ans[-1])))
print(''.join(map(str,ans[0])))


# 1339번 - 단어 수학
# 14888번 - 연산자 끼워넣기
# 14889번 - 스타트와 링크