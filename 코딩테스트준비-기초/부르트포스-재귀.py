# 9095번 - 1, 2, 3 더하기
def sol(k):
    if k == 1:
        return 1
    if k == 2:
        return 2
    if k == 3:
        return 4
    else:
        return sol(k-3) + sol(k-2) + sol(k-1)
    
import sys
n = int(sys.stdin.readline())

for _ in range(n):
    print(sol(int(sys.stdin.readline())))


# 1759번 - 암호 만들기
import sys
input = sys.stdin.readline

l, c = map(int, input().split())
alp = sorted(list(input().split()))
mm = ['a', 'e', 'i', 'o', 'u']

def call(res,flag1, flag2):
    if len(res) == l+1 and flag1 >= 1 and flag2 >= 2:
        print(''.join(res[1:]))
        return
    else:
        for i in alp:
            if i not in res and res[-1] < i:
                if i in mm:
                    flag1 += 1
                else:
                    flag2 += 1
                    
                res.append(i)
                call(res,flag1,flag2)
                if i in mm:
                    flag1 -= 1
                else:
                    flag2 -= 1
                res.pop()

call(['1'],0,0)


# 14501번 - 퇴사
# 14889번 - 스타트와 링크
# 15661번 - 링크와 스타트
# 2529번 - 부등호
# 1248번 - 맞춰봐