class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        M = 0
        C = 0
        for n in nums:
            if C == 0:
                M = n
            C += 1 if n == M else -1
        return M
            
        