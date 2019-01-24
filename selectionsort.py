def selection_sort(arr):
    min = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min = j
        arr[min],arr[i] = arr[i], arr[min]
                
    return arr
                



arr= list(map(int, input().split()))

print(selection_sort(arr))
