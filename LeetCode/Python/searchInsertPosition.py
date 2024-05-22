nums = [1,3,5,6]
target = 2

# O(log n) time complexity solution
def searchInsert(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid # found target
        
        elif nums[mid] < target:
            low = mid + 1 # adjust low pointer

        else:
            high = mid - 1 # adjust high pointer

    return low # return index for insertion position




# O(n) time complexity solution
# def searchInsert(nums, target):
#     for index, value in enumerate(nums):
        
#         if value > target or value == target:
#             return index

#     return index+1


result = searchInsert(nums, target)
print(result)