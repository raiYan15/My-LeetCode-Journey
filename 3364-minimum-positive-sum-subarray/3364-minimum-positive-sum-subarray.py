class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        min_sum = float('inf')
        
        # Iterate over all possible starting points
        for i in range(n):
            current_sum = 0
            
            # Expand the subarray, but STOP once the length exceeds 'r'
            for j in range(i, min(i + r, n)):
                current_sum += nums[j]
                
                # If the length is at least 'l' and the sum is positive, update min_sum
                if j - i + 1 >= l and current_sum > 0:
                    if current_sum < min_sum:
                        min_sum = current_sum
                        
        return min_sum if min_sum != float('inf') else -1