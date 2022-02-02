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

#1655