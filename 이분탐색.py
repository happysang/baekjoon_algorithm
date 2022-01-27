#1920
import sys

num1 = int(input())
lis = sorted(list(map(int, sys.stdin.readline().split())))

num2 = int(input())
num_list = list(map(int,sys.stdin.readline().split()))


def sol(x):
    l,r = 0,num1-1
    
    while(l<=r):
        mid = (l+r)//2
        if x == lis[mid]:
            print(1)
            return
        elif x < lis[mid]:
            r = mid-1
        else:
            l = mid+1
    print(0)
    return

for x in num_list:
    sol(x)
    
    
    
#10816
for x in range(tar_num):
    flag = False
    
    l = 0
    r = len(lis)-1
    while(l<r):
        mid = (l+r)//2
        print(tar_lis[x], res, lis, mid, l , r)

        if tar_lis[x] < lis[mid]:
            r = mid
        elif tar_lis[x] > lis[mid]:
            l = mid+1
        else:

            while(True):    
                if mid == len(lis):
                    flag = True
                    break
                if tar_lis[x] != lis[mid] or mid == len(lis):
                    flag = True
                    break
                del lis[mid]
                res[x] += 1
                
            if(flag):
                break
        
print(res)

#1654
#2805
#2110
#1300

#12015
import sys
input = sys.stdin.readline

n = int(input())
lis = list(map(int, input().split()))
res = [0]

for x in lis:
    if res[-1] < x:
        res.append(x)
    else:
        left = 0
        right = len(res)

        while left < right:
            mid = (right+left) // 2
            if res[mid] < x:
                left = mid+1
            else:
                right = mid
        res[left] = x

print(len(res)-1)