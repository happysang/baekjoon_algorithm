# 10872번
def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)

num = int(input())
if num == 0:
    print(1)
else:
    print(fac(num))



# 10870번
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(int(input())))




# 2447번
def star(l): 
    if l == 1: 
        return ['*']

    stars = star(l//3) 
    res = [] 
    for x in stars: 
        res.append(x*3) 
    for x in stars: 
        res.append(x+' '*(l//3)+x) 
    for x in stars: 
        res.append(x*3)
    print(res)
    return res
    
    
n = int(input()) 
print('\n'.join(star(n)))



# 11729번
count = 0
pack = []
def hanoi(block, start, res, mid):
    global count, pack
    if block == 1:
        count += 1
        pack.append([start, res])
        return
    hanoi(block-1, start, mid, res)
    count += 1
    pack.append([start, res])
    hanoi(block-1, mid, res, start)
    
hanoi(int(input()),1,3,2)
print(count)
for x in pack:
    print(x[0], x[1])