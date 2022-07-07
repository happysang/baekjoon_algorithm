# 16929번 - Two Dots
n,m = map(int, input().split())
lis = []


for _ in range(n):
    lis.append(list(input()))


#start = [시작좌표]
#state = [아래,오른쪽,위,왼쪽]

def sol(start,i,j):
    visit[i][j] = 1
    
    # for a in visit:
    #     print(a)
    # print(f"포인트{i,j}")

    
    if 0 not in state and ( (i<=n-2 and lis[i][j] == lis[i+1][j] and visit[i+1][j]==1 and [i+1,j]==start) or 
                           (j<=m-2 and lis[i][j] == lis[i][j+1] and visit[i][j+1]==1 and [i, j+1]==start) or 
                           (1<=i and lis[i][j] == lis[i-1][j] and visit[i-1][j]==1 and [i-1,j]==start) or 
                           (1<=j and lis[i][j] == lis[i][j-1] and visit[i][j-1]==1 and [i,j-1]==start) ):
        print("Yes")
        exit() 
    
    if i<=n-2 and lis[i][j] == lis[i+1][j] and visit[i+1][j] == 0:
        state[0] = 1
        sol(start,i+1,j)
        state[0] = 0
            
        
    if j<=m-2 and lis[i][j] == lis[i][j+1] and visit[i][j+1] == 0:
        state[1] = 1
        sol(start,i,j+1)
        state[0] = 0
            
        
    if 1 <= i and lis[i][j] == lis[i-1][j] and visit[i-1][j] == 0:
        state[2] = 1
        sol(start,i-1,j)
        state[0] = 0
            

    if 1 <= j and lis[i][j] == lis[i][j-1] and visit[i][j-1] == 0:
        state[3] = 1
        sol(start,i,j-1)
        state[0] = 0
        
    visit[i][j] = 0
            
    
           
for i in range(n):
    for j in range(m):
        visit = [[0 for _ in range(m)] for _ in range(n)]
        state = [0,0,0,0]
        sol([i,j],i,j)
        
print("No")


# 16947번 - 서울 지하철 2호선
# 12946번 - 육각 보드
# 16940번 - BFS 스페셜 저지
# 16964번 - DFS 스페셜 저지