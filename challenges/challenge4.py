def find_magic_index(arr):
    low = 0
    high = len(arr)
    while low < high:
        mid = (low + high)//2
        if arr[mid] < mid:
            low = mid + 1
        elif arr[mid] > mid:
            high = mid - 1
        else:
            low = mid
    return low

print(find_magic_index([-1, 0, 1, 2, 4, 10]))
