#1260
def dfs(v):
    print(v, end=' ')
    visit[v] = 1
    for i in range(1, n + 1):
        if visit[i] == 0 and s[v][i] == 1:
            dfs(i)


def bfs(v):
    lis = [v]
    visit[v] = 1
    while(lis):
        v = lis[0]
        print(v, end=' ')
        del lis[0]
        for i in range(1, n + 1):
            if visit[i] == 0 and s[v][i] == 1:
                lis.append(i)
                visit[i] = 1


n, m, v = map(int, input().split())
s = [[0] * (n + 1) for i in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    s[x][y] = 1
    s[y][x] = 1

visit = [0 for i in range(n + 1)]
dfs(v)
print()
visit = [0 for i in range(n + 1)]
bfs(v)


#2606
#2667
#1012
#2178
#7576
#7569
#1697
#2206
#7562
#1707
