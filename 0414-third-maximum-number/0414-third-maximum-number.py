class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))

        if len(nums) <3:
            return max(nums)
        

        first_max = max(nums)
        nums.remove(first_max)

        second_max = max(nums)
        nums.remove(second_max)

        third_max = max(nums)
        return third_max