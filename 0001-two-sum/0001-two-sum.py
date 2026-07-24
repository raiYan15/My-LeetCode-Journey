class Solution:
    def twoSum(self, nums: List[int], t: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            n = t - nums[i]
            if n in seen:
                return [seen[n], i]
            seen[nums[i]] = i

        