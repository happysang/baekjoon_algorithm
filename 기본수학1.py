# 1712번
fix, val, price = input().split()
res = int(int(fix)/(int(price)-int(val))+1) if int(price) > int(val) else -1
print(res)


# 2292번


# 1193번


# 2869번


# 10250번


# 2775번


# 2839번


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
