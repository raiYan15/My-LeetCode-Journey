from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ms = nums[0]
        cs = 0

        for num in nums:
            cs += num

            if cs > ms:
                ms = cs

            if cs < 0:
                cs = 0

        return ms