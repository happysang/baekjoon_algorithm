#5086번
while(True):
    a,b = map(int, input().split())
    if a == 0 and b == 0:
        break
    
    if b>a and b%a == 0:
        print("factor")
    elif a>b and a%b == 0:
        print("multiple")
    else:
        print("neither")
        


#1037번
num = input()
nums = list(map(int, input().split()))

if len(nums) == 1:
    print(nums[0] ** 2)
else:
    print(min(nums) * max(nums))
    


#2609번
a , b = map(int, input().split())

for x in range(min(a,b),0,-1):
    if a % x == 0 and b % x == 0:
        print(x)
        print( (a*b)//x )
        break
    


#1934번
num = int(input())

for x in range(num):
    a , b = map(int, input().split())

    for x in range(min(a,b),0,-1):
        if a % x == 0 and b % x == 0:
            print( (a*b)//x )
            break
        


#2981번



#3036번
num = int(input())
nums = list(map(int, input().split()))

res = []
for x in nums[1:]:
    if str(nums[0] / x)[-1] == '0':
        print(f'{nums[0] // x}/1')
    else:
        for k in range(min(nums[0],x),0,-1):
            if nums[0] % k == 0 and x % k == 0:
                mm = k
                break
            
        print(f'{nums[0]//k}/{(x//k)}')
        


#11050번
#풀이 1)
a,b = map(int, input().split())
import itertools
print(len(list(itertools.combinations(range(a), b))))

#풀이 2)
a,b = map(int, input().split())
def fibo(num):
    if num == 1:
        return 1
    else:
        return num * fibo(num-1)

if a == 1 or b == 0 or a == b:
    print(1)

else:
    print( fibo(a)//(fibo(a-b) * fibo(b)) )



#11051번
res = [0]*1001
a,b = map(int, input().split())

if a == 1 or b == 0 or a == b:
    print(1)

else:    
    for x in range(1,a+1):
        if x == 1:
            res[1] = 1
        else:
            res[x] = res[x-1] * x
    print((res[a]//(res[a-b]*res[b])) % 10007)
    


#1010번
res = [0]*30
num = int(input())

for _ in range(num):
    b,a = map(int, input().split())

    if a == 1 or b == 0 or a == b:
        print(1)

    else:    
        for x in range(1,a+1):
            if x == 1:
                res[1] = 1
            else:
                res[x] = res[x-1] * x
        print((res[a]//(res[a-b]*res[b])))



#9375번



#1676번



#2004번