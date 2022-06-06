def binary_search(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (high + low) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:            
            high = mid - 1
    return False


def binary_search_recursion(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            return binary_search_recursion(data, target, low, mid - 1)
        else:
            return binary_search_recursion(data, target, mid + 1, high)


ls = [1, 2, 3, 4, 5, 6]

print(binary_search_recursion(ls, 5, 1, 6))
print(binary_search(ls, 1))