class Solution(object):
    def findMaxAverage(self, nums, k):
        c = ms = sum(nums[:k])

        for i in range(k, len(nums)):
            c += nums[i] - nums[i-k]
            ms = max(ms, c)

        return ms / float(k)