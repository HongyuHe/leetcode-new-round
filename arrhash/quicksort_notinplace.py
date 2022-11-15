def quick_sort(arr):
    if len(arr) < 2: return arr
    
    pivot = arr.pop()
    smaller = []
    larger = []
    for n in arr:
        if n > pivot:
            larger.append(n)
        else:
            smaller.append(n)
    result = quick_sort(smaller) + [pivot] + quick_sort(larger)
    return result

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    result = quick_sort(arr=arr)
    print(result)