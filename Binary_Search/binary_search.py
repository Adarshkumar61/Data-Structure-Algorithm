#array sorted required:
def binary_search(arr, target):
    left = 0                 # start of search
    right = len(arr) - 1     # end of search

    while left <= right:     # keep searching while range exists
        mid = (left + right) // 2   # middle position

        if arr[mid] == target:
            return mid       # found

        elif arr[mid] < target:
            left = mid + 1   # search right side

        else:
            right = mid - 1  # search left side

    return -1                # not found
# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = binary_search(arr, target)
print(result)  # Output: 4 (index of target in array)

print(binary_search(arr, 10))  # Output: -1 (not found)    