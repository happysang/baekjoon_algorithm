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



#11050번



#11051번



#1010번



#9375번



#1676번



#2004번