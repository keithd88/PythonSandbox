def removeElement(nums) -> int:
        print(nums)
        unique_nums = []
        for index, num in enumerate(nums):
            if num not in unique_nums:
                unique_nums.append(num)
            else:
                nums[index] = 100

        nums.sort()

        return len(unique_nums)



k = removeElement([0,0,1,1,1,2,2,3,3,4])

print(k)