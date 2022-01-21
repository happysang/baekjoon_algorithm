#2630
num = int(input())

lis = []
for x in range(num):
    lis.append(list(map(int,input().split())))


def sol(num,lis,flag):
    temp = set()
    for x in lis:
        for i in x:
            temp.add(i)
            if len(temp) == 2:
                flag = 2
                break
            
    if flag == 2:
        lis1, lis2, lis3, lis4 = [],[],[],[]
        for x in range(num):
            if x < num//2:
                lis1.append(lis[x][:num//2])
                lis2.append(lis[x][num//2:])
            else:
                lis3.append(lis[x][:num//2])
                lis4.append(lis[x][num//2:])
        return sol(num//2,lis1,0)+sol(num//2,lis2,0)+sol(num//2,lis3,0)+sol(num//2,lis4,0)
    elif list(temp)[0] == 1:
        return "b"
    else:
        return "r"

res1,res2 = 0,0
for x in sol(num,lis,0):
    if x == 'b':
        res2 += 1
    else:
        res1 += 1
print(res1)
print(res2)



#1992
num = int(input())

lis = []
for x in range(num):
    temp = []
    for i in input():
        temp.append(int(i))
    lis.append(temp)


def sol(num,lis,flag):
    temp = set()
    for x in lis:
        for i in x:
            temp.add(i)
            if len(temp) == 2:
                flag = 2
                break
            
    if flag == 2:
        lis1, lis2, lis3, lis4 = [],[],[],[]
        for x in range(num):
            if x < num//2:
                lis1.append(lis[x][:num//2])
                lis2.append(lis[x][num//2:])
            else:
                lis3.append(lis[x][:num//2])
                lis4.append(lis[x][num//2:])
        return "("+sol(num//2,lis1,0)+sol(num//2,lis2,0)+sol(num//2,lis3,0)+sol(num//2,lis4,0)+")"
    elif list(temp)[0] == 1:
        return "1"
    else:
        return "0"

print(sol(num,lis,0))



#1780

#1629

#11401

#2740

#10830

#11444

#6549

#2261