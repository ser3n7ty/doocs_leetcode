class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        mi, mx = min(nums), max(nums)
        return next((x for x in nums if x not in [mi, mx]), -1)
