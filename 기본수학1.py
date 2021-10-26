# 1712번
fix, val, price = input().split()
res = int(int(fix)/(int(price)-int(val))+1) if int(price) > int(val) else -1
print(res)



# 2292번
num, count, a = 1,1, int(input())
while(True):
    if a <= num:
        print(count)
        break
    num += 6*count
    count += 1



# 1193번
num, count, a = 1,1, int(input())
while(True):
    if a <= num:
        if count%2 == 0:
            print(f"{a-(num-count)}/{(count+1)-(a-(num-count))}" )
            break
        else:
            print(f"{(count+1)-(a-(num-count))}/{a-(num-count)}" )
            break
    
    count += 1
    num += count



# 2869번
import math
lis = list(map(int, input().split()))
date = (lis[2]-lis[0])/(lis[0]-lis[1])
if date%1 == 0:
    print(int(date+1))
else:
    print(math.ceil(date)+1)



# 10250번
res = []
for x in range(int(input())):
    lis = list(map(int, input().split()))
    room,num = [], 100

    for _ in range(lis[0]):
        room.append([idx for idx in range(num+1, num+lis[1]+1)])
        num += 100

    if lis[2] % lis[0] == 0:
        res.append(room[lis[0]-1][lis[2]//lis[0]-1])
    else:
        res.append(room[lis[2]%lis[0]-1][lis[2]//lis[0]])

for x in res:
    print(x)



# 2775번
for _ in range(int(input())):
    h = int(input())
    w = int(input())

    r = [[0 for _ in range(w)] for _ in range(h+1)]

    for x in range(1, w+1):
        r[0][x-1] = x

    for y in range(1, h+1):
        for x in range(w):
            if x == 0:
                r[y][x] = 1
            else:
                r[y][x] = r[y][x-1] + r[y-1][x]
    
    print(r[h][w-1])


# 2775번 - 내가 해결한 재귀풀이 but 시간초과.. 재귀라고 다 좋은게 아니다..
def find(h, w):
    count = 0
    if h == 0:
        return w
    else:
        for x in range(w+1):
            count += find(h-1,x)
    return count

for _ in range(int(input())):
    h = int(input())
    w = int(input())



# 2839번
num = int(input())
if num ==4 or num == 7:
    print(-1)
else:
    a,b = divmod(num,5)
    if b == 0:
        print(a)
    elif b == 1:
        print(a-1+2)
    elif b == 2:
        print(a-2+4)
    elif b == 3:
        print(a+1)
    elif b == 4:
        print(a-1+3)



# 10757번



#1011번
num = int(input())
res = []
for _ in range(num):
    point = input().split()
    dis = int(point[1]) - int(point[0])

    if dis == 1:
        res.append(1)
    elif dis == 2:
        res.append(2)
    elif dis == 3:
        res.append(3)
    else:
        for x in range(2,dis):
            if x**2 == dis:
                res.append(x*2-1)
                break
            elif x**2 < dis < (x+1)**2:
                if dis - x**2 > x:
                    res.append(x*2+1)
                    break
                else:
                    res.append(x*2)
                    break
for x in res:
    print(x)
