n = int(input())
arr = list(map(int, input().split()))

def counting_sort(arr):
    sorted_array = [0] * (10**5)
    for i in arr:
        sorted_array[i]+=1
    for i in range(len(sorted_array)):
        if sorted_array[i]!=0:
            print(i, sorted_array[i])
counting_sort(arr)
