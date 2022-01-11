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



#1934번



#2981번



#3036번



#11050번



#11051번



#1010번



#9375번



#1676번



#2004번