def majorityElement(nums) -> int:
        print(nums)
        nums.sort()
        n = len(nums)

        return nums[n//2] 



k = majorityElement([3,2,3])

print(k)