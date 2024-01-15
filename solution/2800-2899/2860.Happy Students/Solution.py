class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for i in range(n + 1):
            if i and nums[i - 1] >= i:
                continue
            if i < n and nums[i] <= i:
                continue
        return 0
