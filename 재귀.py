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



# 11729번