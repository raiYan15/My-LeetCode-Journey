class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rem_count = {0:1}
        ans = 0
        ps = 0
        for num in nums:
            ps += num
            rem = ps % k
            ans += rem_count.get(rem,0) 
            rem_count[rem] = rem_count.get(rem,0) + 1
        return ans 
        