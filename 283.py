class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        for j in range(0, n):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
        for j in range(i, n):
            nums[j] = 0

        return nums
