# Example usage:
nums = [1, 2, 3]
result = []

def swap(nums, j, result):
    if j == len(nums):
        result.append(nums[:])  
        return
    for i in range(j, len(nums)):
        nums[j], nums[i] = nums[i], nums[j]
        swap(nums, j + 1, result)
        nums[j], nums[i] = nums[i], nums[j]  

swap(nums, 0, result)
print(result)