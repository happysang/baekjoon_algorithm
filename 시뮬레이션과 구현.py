# 16935번 - 배열 돌리기 3
def cal1(lis):
    n = len(lis)
    m = len(lis[0])
    for i in range(n//2):
        lis[i],lis[n-1-i] = lis[n-1-i],lis[i]
        
        
def cal2(lis):
    n = len(lis)
    m = len(lis[0])
    for i in range(n):
        for j in range(m//2):
            lis[i][j], lis[i][m-1-j] = lis[i][m-1-j],lis[i][j]


import copy 
def cal3(lis):
    n = len(lis)
    m = len(lis[0])
    global nums
    cal1(lis)
    temp = [[]for _ in range(m)]
    for i in range(n):
        for j in range(m):
            temp[j].append(lis[i][j])
    nums = copy.deepcopy(temp)        


def cal4(lis):
    n = len(lis)
    m = len(lis[0])
    global nums
    cal2(lis)
    temp = [[]for _ in range(m)]
    for i in range(n):
        for j in range(m):
            temp[j].append(lis[i][j])
    nums = copy.deepcopy(temp)
    
    
def cal5(lis):
    n = len(lis)
    m = len(lis[0])
    global nums
    temp1, temp2, temp3, temp4 = [],[],[],[]
    
    for i in range(n):
        if i < n//2:
            temp1.append(nums[i][:m//2])
            temp2.append(nums[i][m//2:])
        else:
            temp4.append(nums[i][:m//2])
            temp3.append(nums[i][m//2:])
    
    temp = []
    for i in range(n//2):
        temp.append(temp4[i]+temp1[i])
    for i in range(n//2):
        temp.append(temp3[i]+temp2[i])

    nums = copy.deepcopy(temp)
                

def cal6(lis):
    n = len(lis)
    m = len(lis[0])
    global nums
    temp1, temp2, temp3, temp4 = [],[],[],[]
    
    for i in range(n):
        if i < n//2:
            temp1.append(nums[i][:m//2])
            temp2.append(nums[i][m//2:])
        else:
            temp4.append(nums[i][:m//2])
            temp3.append(nums[i][m//2:])
            
    temp = []
    for i in range(n//2):
        temp.append(temp2[i]+temp3[i])
    for i in range(n//2):
        temp.append(temp1[i]+temp4[i])

    nums = copy.deepcopy(temp)      
            
    

n,m,t = map(int,input().split()) #세로 가로

nums = []
for _ in range(n):
    nums.append(list(map(int, input().split())))
    
cal = list(map(int,input().split()))

for i in cal:
    if i == 1:
        cal1(nums)
    elif i == 2:
        cal2(nums)
    elif i == 3:
        cal3(nums)
    elif i == 4:
        cal4(nums)
    elif i == 5:
        cal5(nums)
    elif i == 6:
        cal6(nums)
    
for i in nums:
    print(*i)


# 16926번 - 배열 돌리기 1
# 16927번 - 배열 돌리기 2
# 14499번 - 주사위 굴리기
# 14890번 - 경사로
# 15662번 - 톱니바퀴 (2)
# 14503번 - 로봇 청소기
# 14890번 - 경사로
# 15685번 - 드래곤 커브
# 2290번 - LCD Test
# 16931번 - 겉넓이 구하기
# 1917번 - 정육면체 전개도
# 16967번 - 배열 복원하기
# 20327번 - 배열 돌리기 6
# 20055번 - 컨베이어 벨트 위의 로봇