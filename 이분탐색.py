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
#1654
#2805
#2110
#1300
#12015
