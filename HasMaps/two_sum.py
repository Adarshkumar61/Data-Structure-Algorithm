def twosum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return (seen[need], i)
        seen[num] = i

nums = [3,3, 4,5,6]
target = 7

result = twosum(nums, target)
print(result)


# Output: (1, 2) # Explanation: nums[1] + nums[2] = 3 + 4 = 7