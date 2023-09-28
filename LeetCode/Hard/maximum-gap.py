class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0

        nums.sort()

        m = 0

        for i in range(len(nums) - 1):
            a = nums[i + 1] - nums[i]
            if a > m: m = a
        
        return m
