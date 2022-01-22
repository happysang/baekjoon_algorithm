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
num = int(input())

lis = []
for x in range(num):
    lis.append(list(map(int, input().split())))

def sol(num,lis):
    if num==1:
        res = ""
        for x in lis:
            for i in x:
                if i == -1:
                    res+="a"
                elif i == 0:
                    res+="b"
                else:
                    res+="c"
        return res
                    
    else:
        temp = lis[0][0]
        flag = True
        p = False
        for x in lis:
            for i in range(len(x)):
                if temp != x[i]:
                    p = True
                    break
            if p:
                flag = False
                break
                
        if flag:
            if temp == -1:
                return "a"
            elif temp == 0:
                return "b"
            else:
                return "c"
        
        else:
            lis1,lis2,lis3,lis4,lis5,lis6,lis7,lis8,lis9 = [],[],[],[],[],[],[],[],[]
                    
            for x in lis:
                lis1.append(x[:len(x)//3])
                lis2.append(x[len(x)//3:(len(x)//3)*2])
                lis3.append(x[(len(x)//3)*2:])
            lis7 = lis1[(len(x)//3)*2:]
            lis4 = lis1[len(x)//3:(len(x)//3)*2]
            lis1 = lis1[:len(x)//3]
            lis8 = lis2[(len(x)//3)*2:]
            lis5 = lis2[len(x)//3:(len(x)//3)*2]
            lis2 = lis2[:len(x)//3]
            lis9 = lis3[(len(x)//3)*2:]
            lis6 = lis3[len(x)//3:(len(x)//3)*2]
            lis3 = lis3[:len(x)//3]
            
            return sol(num//3,lis1)+sol(num//3,lis2)+sol(num//3,lis3)+sol(num//3,lis4)+sol(num//3,lis5)+sol(num//3,lis6)+sol(num//3,lis7)+sol(num//3,lis8)+sol(num//3,lis9)


res1, res2, res3 = 0,0,0
for x in sol(num,lis):
    if x == "a":
        res1+=1
    elif x == "b":
        res2+=1
    else:
        res3+=1

print(res1)
print(res2)
print(res3)



#1629

#11401

#2740

#10830

#11444

#6549

#2261