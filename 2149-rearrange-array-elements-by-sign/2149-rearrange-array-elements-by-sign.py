class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        p = 0
        n = 1
        for x in nums:
            if x > 0:
                ans[p] = x
                p += 2
            else:
                ans[n] = x
                n += 2
        return ans

        