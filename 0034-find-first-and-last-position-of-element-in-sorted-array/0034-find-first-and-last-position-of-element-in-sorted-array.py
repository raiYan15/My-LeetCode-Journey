class Solution:
    def searchRange(self, nums: List[int], t: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        f = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == t:
                f = mid
                r = mid - 1
            elif nums[mid] < t:
                l = mid + 1
            else:
                r = mid - 1
        if f == -1:
            return [-1, -1]
        l = 0
        r = len(nums) - 1
        last = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == t:
                last = mid
                l = mid + 1
            elif nums[mid] < t:
                l = mid + 1
            else:
                r = mid - 1
        return [f, last]
