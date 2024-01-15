class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        return next((i for i, x in enumerate(nums) if i != x), len(nums))
