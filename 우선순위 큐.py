#11279
import sys,heapq

heap = []
heapq.heapify(heap)

num = int(sys.stdin.readline().strip())

for x in range(num):
    tar = sys.stdin.readline().strip()
    
    if tar == '0':
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-int(tar),int(tar)))
        
        
        
#1927
import sys,heapq

num = int(input())
heap = []
heapq.heapify(heap)

for x in range(num):
    tar = sys.stdin.readline().strip()
    
    if tar == '0':
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, int(tar))
        
        
        
#11286
import sys,heapq

heap = []
heapq.heapify(heap)

num = int(sys.stdin.readline().strip())

for x in range(num):
    tar = sys.stdin.readline().strip()
    
    if tar == '0':
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(int(tar))+(int(tar)*(0.0000000000000000000001)),int(tar)))
        
        


#1655
import sys,heapq
num = int(sys.stdin.readline().strip())
lheap, rheap = [], []
heapq.heapify(lheap)
heapq.heapify(rheap)


flag = True
for x in range(num):
    tar = int(sys.stdin.readline().strip())
    if flag:
        heapq.heappush(lheap, (-tar, tar))
        flag = False
    else:
        heapq.heappush(rheap, tar)
        flag = True
        
    if len(rheap) > 0 and len(lheap):
        if lheap[0][1] > rheap[0]:
            r = heapq.heappop(rheap)
            l = heapq.heappop(lheap)
            heapq.heappush(lheap, (-r,r))
            heapq.heappush(rheap, l[1])
    print(lheap[0][1])