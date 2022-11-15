## 1 3 4 7 9
## 1 1 2 3 4 6 7 9 10

def quick_sort(arr, low, high):
    print(low, high)
    print(arr)
    if low >= high: 
        return
    
    pivot = high
    i = low
    # * Move the `j` pointer to the low of the `pivot`.
    j = high - 1
    #> i: n>pivot, j: n<=pivot
    while i < j:
        while i < j:
            if arr[i] > arr[pivot]:
                break
            else:
                i += 1
        while i < j:
            if arr[j] <= arr[pivot]:
                break
            else:
                j -= 1
        
        arr[i], arr[j] = arr[j], arr[i] 
    #> i >= j

    if arr[i] > arr[pivot]:
        arr[i], arr[pivot] = arr[pivot], arr[i]
        pivot = i
    # * else: `arr[low, high]` is sorted.

    quick_sort(arr, low=low, high=pivot-1)
    quick_sort(arr, low=pivot+1, high=high)
    return arr


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    result = quick_sort(arr, 0, len(arr)-1)
    print(result)