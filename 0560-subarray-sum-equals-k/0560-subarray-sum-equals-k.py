class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0:1}
        ans = 0
        ps = 0
        for num in nums:
            ps += num
            if ps - k in count:
                ans += count[ps - k]
            count[ps] = count.get(ps,0) + 1
        return ans


        