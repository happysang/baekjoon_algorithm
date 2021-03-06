# 10430번 - 나머지
A, B, C = map(int, input().split())
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)


# 4375번 - 1
import sys
while True:
    try:
        tar = int(sys.stdin.readline())
    except:
        break

    num = 1
    cnt = 1
    while True:
        if num % tar != 0:
            num += 10**cnt ## str(num) 이런식으로 제곱하려했는데 시간아웃걸림. 참고하기.
            cnt +=1
        else:
            break
    print(len(str(num)))


# 1037번 - 약수
import sys
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))


if len(nums)%2 == 0:
    print(sorted(nums)[0] * sorted(nums)[-1])
else:
    print(sorted(nums)[n//2] ** 2)
    

# 17427번 - 약수의 합2
n = int(input())
res = 0
for k in range(1,n+1):
    res += (n//k) * k
print(res)


# 17425번 - 약수의 합 -> 시간 초과로 인해 pypy3로 해결
import sys
n = 1000000

nums = [1]*(n+1)
res  = [0]*(n+1)

for i in range(2,n+1):
    j = 1
    while i*j <= n:
        nums[i*j] += i 
        j += 1
        
for i in range(1, n+1):
    res[i] += res[i-1] + nums[i]
    

c = int(sys.stdin.readline())
for _ in range(c):
    print(res[int(sys.stdin.readline())])


# 2609번 - 최대공약수와 최소공배수
def GCD(x, y):
    while(y):
        x, y = y, x%y
    return x

def LCM(x, y):
    return (x*y) // GCD(x,y)

import sys
x, y = map(int, sys.stdin.readline().split())
print(GCD(x,y))
print(LCM(x,y))



# 1978번 - 소수 찾기
import sys
MAX = 1000

nums = [0] * (MAX+1)
nums[1] = 1

for i in range(2,MAX//2+1):
    t = i
    while(t <= MAX):
        if nums[t] == 0 and i!=t:
            nums[t] +=1
        t += i

N = int(sys.stdin.readline())
n = list(map(int, sys.stdin.readline().split()))

cnt = 0
for i in n:
    if nums[i] == 0:
        cnt += 1
print(cnt) 


# 1929번 - 소수 구하기
import sys
MAX = 1000000

nums = [0] * (MAX+1)
nums[1] = 1

for i in range(2,MAX//2+1):
    t = i
    while(t <= MAX):
        if nums[t] == 0 and i!=t:
            nums[t] +=1
        t += i

a,b = map(int,sys.stdin.readline().split())

for i in range(a,b+1):
    if not nums[i]:
        print(i)
        

# 6588번 - 골드바흐의 추측
import sys
MAX = 1000000
nums = [0] * (MAX+1)
nums[1] = 1
for i in range(2,MAX//2+1):
    t = i
    while(t <= MAX):
        if nums[t] == 0 and i!=t:
            nums[t] +=1
        t += i

while (True):
    flag = True
    tar = int(sys.stdin.readline())
    if tar == 0:
        break
    for i in range(tar-1, 1, -1):
        if nums[i] == 0:
            if nums[tar-i] == 0:
                flag = False
                print(f"{tar} = {tar-i} + {i}")
                break
    if flag:
        print("Goldbach's conjecture is wrong.")
