# 10972번 - 다음 순열
import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))

for i in range(n-1,0,-1):
    if nums[i] > nums[i-1]:
        x,y = i-1,i
        
        for j in range(n-1,0,-1):
            if nums[j] > nums[x]:
                nums[j], nums[x] = nums[x], nums[j]
                break
            
        nums = nums[:y] + sorted(nums[y:])
        print(*nums)
        exit()
                    
print(-1)


# 10973번 - 이전 순열



# 10974번 - 모든 순열
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
nums = [i for i in range(1,n+1)]

def sol(nums, rnums):
    if nums != rnums:
        for i in range(n-1,0,-1):
            if nums[i] > nums[i-1]:
                x,y = i-1,i
                
                for j in range(n-1,0,-1):
                    if nums[j] > nums[x]:
                        nums[j], nums[x] = nums[x], nums[j]
                        break
                    
                nums = nums[:y] + sorted(nums[y:])
                print(*nums)
                sol(nums,rnums)
                return
    else:
        return

print(*nums)
sol(nums, reversed(nums))




# 10819번 - 차이를 최대로
import itertools

n = int(input())
arr = list(map(int, input().split()))
nums = list(itertools.permutations(arr, n))

m = 0
for lis in nums:
    temp = 0
    for i in range(n-1):
        temp += abs(lis[i] - lis[i+1])
    m = max(m, temp)
print(m)



# 10971번 - 외판원 순회 2
import sys
input = sys.stdin.readline

n = int(input())
nums = []
for i in range(n):
    nums.append( list(map(int,input().split())) )
mini = 100000001

def sol(s,ans,res):
    global mini
    if ans >= mini:
        return
    
    if len(res) == n:
        if nums[res[-1]][res[0]]:
            ans += nums[res[-1]][res[0]]
        else:
            return
        mini = min (mini, ans)
        ans -= nums[res[-1]][res[0]]
        return

    else:            
        for i in range(n):
            if i not in res:
                if nums[s][i] == 0:
                    return
                else:
                    res.append(i)
                    ans += nums[s][i]
                    sol(i,ans,res)
                    res.pop()
                    ans -= nums[s][i]
            else:
                continue    
            
for s in range(n):
    sol(s,0,[s])
    
print(mini)


# 6603번 - 로또
import sys, itertools
input = sys.stdin.readline


while(True):
    cas = list(map(int,input().split()))
    if cas[0] == 0:
        break
    nums = list(itertools.combinations(cas[1:],6))
    
    for c in nums:
        print(*c)
        
    print()



# 브루트 포스 - 비트마스크
# 11723번 - 집합
# 1182번 - 부분수열의 합
# 14889번 - 스타트와 링크
# 14391번 - 종이 조각