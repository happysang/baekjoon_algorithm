#11047번
import sys
num, money = map(int, sys.stdin.readline().split())

nums = []
for i in range(num):
    nums.append(int(sys.stdin.readline()))

nums.reverse()

flag = False
cnt = 0
for x in nums:
    cnt += (money//x)
    money -= (money//x)*x
    if money == 0:
        break
print(cnt)


#1931번
num = int(input())
time = []

for _ in range(num):
  time.append(list(map(int, input().split())))

time = sorted(time, key= lambda a: (a[1],a[0]))

last,cnt = 0 , 0

for i, j in time:
  if i >= last:
    cnt += 1
    last = j

print(cnt)



#11399번
num = int(input())
nums = list(map(int, input().split()))
nums.sort()
res = 0
for x in range(num):
    res += sum(nums)
    del nums[-1]
    
print(res)



#1541번


#13305번