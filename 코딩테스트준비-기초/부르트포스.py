# 2309번 - 일곱 난쟁이
import sys

nums = []
for _ in range(9):
    nums.append(int(sys.stdin.readline().strip()))

gap = sum(nums)-100


for i in nums:
    for j in nums:
        if i == j:
            continue
        if gap == i+j:
            nums.remove(i)
            nums.remove(j)
            
            for i in sorted(nums):
                print(i)
            exit()


# 3085번 - 사탕 게임
import sys

n = int(sys.stdin.readline())
candy = []

for _ in range(n):
    candy.append(list(sys.stdin.readline().strip()))


def sol():
    m = -1
    
    for i in range(n):
        for j in range(n):
             
            c1, c2, c3, c4, c5, c5_1, c6, c6_1, c7, c7_1, c8, c8_1 = -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1
            c1 = count1(candy,i,j)
            c2 = count2(candy,i,j)
    
            if i == n-1 and j == n-1:
                break
            
            elif i == n-1:
                if candy[i][j] != candy[i][j+1]:
                    candy[i][j+1],candy[i][j] = candy[i][j],candy[i][j+1]
                    c3 = count1(candy,i,j)
                    c4 = count2(candy,i,j)
                    candy[i][j+1],candy[i][j] = candy[i][j],candy[i][j+1]
            
            
            elif j == n-1:
                if candy[i][j] != candy[i+1][j]:
                    candy[i+1][j], candy[i][j] = candy[i][j], candy[i+1][j]
                    c3 = count1(candy,i,j)
                    c4 = count2(candy,i,j)
                    candy[i+1][j], candy[i][j] = candy[i][j], candy[i+1][j]
                    
                    
            else:
                if candy[i][j] != candy[i][j+1]:
                    candy[i][j+1],candy[i][j] = candy[i][j],candy[i][j+1]
                    c5 = count1(candy,i,j)
                    c6 = count2(candy,i,j)
                    c5_1 = count1(candy,i+1,j)
                    c6_1 = count2(candy,i,j+1)
                    candy[i][j+1],candy[i][j] = candy[i][j],candy[i][j+1]
                    
                if candy[i][j] != candy[i+1][j]:
                    candy[i+1][j], candy[i][j] = candy[i][j], candy[i+1][j]
                    c7 = count1(candy,i,j)
                    c8 = count2(candy,i,j)
                    c7_1 = count1(candy,i+1,j)
                    c8_1 = count2(candy,i,j+1)
                    candy[i+1][j], candy[i][j] = candy[i][j], candy[i+1][j]
            
            m = max(m, c1, c2, c3, c4, c5, c6, c7, c8, c5_1, c6_1, c7_1, c8_1 )
            
            if m == n:
                print(n)
                exit()
    return m
            
def count1(candy,i,j):
    cnt1 = 0
    ii = i
    jj = j
    while(jj>0):
        if candy[ii][jj] == candy[ii][jj-1]:
            cnt1 += 1
            jj -= 1
        else:
            break
    
    cnt2 = 0
    ii = i
    jj = j
    while(jj<n-1):
        if candy[ii][jj] == candy[ii][jj+1]:
            cnt2 += 1
            jj += 1
        else:
            break
    return cnt1 + cnt2 + 1

def count2(candy,i,j):
    ii = i
    jj = j
    cnt1 = 0
    while(ii>0):
        if candy[ii][jj] == candy[ii-1][jj]:
            cnt1 += 1
            ii -= 1
        else:
            break
    
    ii = i
    jj = j
    cnt2 = 0
    while(ii<n-1):
        if candy[ii][jj] == candy[ii+1][jj]:
            cnt2 += 1
            ii += 1
        else:
            break
    return cnt1 + cnt2 + 1

if sol() == -1:
    print(1)
else:
    print(sol())


# 1476번 - 날짜 계산
import sys
e,s,m = map(int, sys.stdin.readline().split())
year = 0

while(True):
    if year % 15 + 1 == e and year % 28 + 1 == s and year % 19 + 1 == m:
        print(year+1)
        break
    else:
        year += 1


# 1107번 - 리모컨



# 14500번 - 테트로미노



# 6064번 - 카잉 달력
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    M, N, x, y = map(int,sys.stdin.readline().split())
    flag = True
    while x <= M*N:
        if (x-y) % N == 0:
            print(x)
            flag =False
            break
        else:
            x += M
    
    if flag:
        print(-1)


# 1748번 - 수 이어 쓰기 1
import sys
n = sys.stdin.readline().strip()
num = int(n)

res = 0
for i in range(len(n)):
    k = 9 * (10**i) * (i+1)
    res += k
    if i==len(n)-1:
        res -= k
        if i != 0:
            temp = num - ((10**i)-1)
        else:
            temp = num
        res += temp*(i+1)
        
print(res)



# 9095번 - 1, 2, 3 더하기
def sol(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return sol(n-3)+sol(n-2)+sol(n-1)

t = int(input())

for _ in range(t):
    print(sol(int(input())))