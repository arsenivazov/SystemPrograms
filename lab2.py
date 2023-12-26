def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            right = mid - 1

        else:
            left = mid + 1

    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 1
result = binary_search(arr, target)

if result != -1:
    print(f"Елемент {target} знаходиться на індексі {result}.")
else:
    print(f"Елемент {target} не знайдено в масиві.")
