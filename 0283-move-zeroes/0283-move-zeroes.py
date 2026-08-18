class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0

        for R in range(len(nums)):
            if nums[R]:
                nums[l],nums[R]=nums[R],nums[l]
                l+=1

        return nums

                