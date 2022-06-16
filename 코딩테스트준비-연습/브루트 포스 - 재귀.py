# 6603번 - 로또
from itertools import combinations

while(True):
    t = input()
    if t == "0":
        exit()
    else:
        nums = list(map(int,t.split()))
        k = nums[0]
        nums = nums[1:]
        lis = list(combinations(nums,6))
        for l in lis:
            print(*l)
    print()
    
    
# 1182번 - 부분수열의 합
from itertools import combinations

n,s = map(int,input().split())
nums = list(map(int,input().split()))

cnt = 0
for i in range(1,n+1):
    lis = list(combinations(nums, i))
    for l in lis:
        if sum(l) == s:
            cnt += 1
            
print(cnt)


# 14225번 - 부분수열의 합
# 14888번 - 연산자 끼워넣기
# 15658번 - 연산자 끼워넣기 (2)
# 14500번 - 테트로미노
# 16197번 - 두 동전
# 16198번 - 에너지 모으기
# 9663번 - N-Queen
# 2580번 - 스도쿠
# 4574번 - 스도미노쿠