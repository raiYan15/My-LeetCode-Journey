class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        r = nums[0]
        f = nums[0]
        for i in range(1 , len(nums)):
            r = max(nums[i], r + nums[i])
            f = max(r,f)
        return f
        