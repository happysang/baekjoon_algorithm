# 1978번
num = int(input())
lis = list(map(int, input().split()))
count = 0
for x in lis:
    check = True
    if x == 1:
        continue
    for y in range(2,x):
        if x % y == 0:
            check = False
            break
    if check:
        count += 1
print(count)


# 2581번



# 11653번



# 1929번



# 4948번



# 9020번



# 1085번



# 3009번



# 4153번



# 3053번



# 1002번