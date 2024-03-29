#정렬 알고리즘

arr = [23,5,1,56,13]
print("주어진 리스트:",arr)



#선택 정렬 - 시간복잡도 : O(n^2)
#장점 : 구현이 쉽다
#단점 : 시간이 오래 걸린다.
def selection_sort(arr):
    for x in range(len(arr)-1):
        min_index = x
        for y in range(x+1, len(arr)):
            if arr[min_index] > arr[y]:
                min_index = y
        arr[x],arr[min_index] = arr[min_index],arr[x]
        print(arr)
    return arr
#selection_sort(arr)



#삽입 정렬 - 시간복잡도 : O(n^2) (최악의 경우)
#장점 : 최선의 경우 O(N) 이라는 엄청나게 빠른 효율성을 갖고 있다, 성능이 좋다
#단점 : 데이터의 상태 및 데이터의 크기에 따라서 성능의 편차가 심하다.
def insertion_sort(arr):
    for x in range(1, len(arr)):
        for y in range(x, 0, -1):
            if arr[y] < arr[y-1]:
                arr[y],arr[y-1] = arr[y-1],arr[y]
        print(arr)
    return arr
#insertion_sort(arr)



#버블 정렬 - 시간복잡도 : O(n^2)
#장점 : 구현이 쉽다, 직관적인 코드
#단점 : 비효율적이다.
def bubble_sort(arr):
    for x in range(len(arr)-1,0,-1):
        for y in range(x):
            if arr[y] > arr[y+1]:
                arr[y],arr[y+1] = arr[y+1],arr[y]
    return arr
#bubble_sort(arr)



#병합 정렬 - 시간복잡도 : O(NlogN)
#장점 : 항상 O(NlogN) 이라는 준수한 시간복잡도를 갖는다.(분할 과정에서 logN, 최종적으로 NlogN)
#단점 : 가장 큰 단점은 추가적인 메모리 필요는 점이다.
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    m = len(arr)//2
    arr1 = merge_sort(arr[:m])
    arr2 = merge_sort(arr[m:])
    return merge(arr1,arr2)
            
def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    print(result)
    return result
#merge_sort(arr)



#퀵 정렬 - 시간복잡도 : O(n^2) (최악의 경우)
#장점 : 분할 과정에서 logN 이라는 시간이 걸리고 보통 NlogN 정도의 준수한 시간이 걸린다.
#단점 : 기준값 (pivot)에 따라서 시간복잡도가 크게 달라진다.
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    left_arr, pivot, right_arr = [],[arr[len(arr)//2]],[]
    for val in arr:
        if val < pivot[0]:
            left_arr.append(val)
        elif val > pivot[0]:
            right_arr.append(val)
    print(left_arr, right_arr)
    return quick_sort(left_arr)+pivot+quick_sort(right_arr)
# quick_sort(arr)



#힙 정렬 - 시간복잡도 O(NlogN)
#장점 : 추가적인 메모리를 필요로 하지 않으면서 항상 O(NlongN) 이라는 시간 복잡도를 가지는 효율적인 정렬법이다.
#단점 : 실제 속도를 측정해보면 퀵정렬보다 느리다.
def heap_sort(arr):
    for i in range(len(arr)//2-1, -1, -1):
        heapify(arr, i, len(arr))
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)
    return arr

def heapify(arr, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and arr[left_index] > arr[largest]:
        largest = left_index
    if right_index < heap_size and arr[right_index] > arr[largest]:
        largest = right_index
    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        heapify(arr, largest, heap_size)
# heap_sort(arr)