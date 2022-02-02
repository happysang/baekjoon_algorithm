#11279

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