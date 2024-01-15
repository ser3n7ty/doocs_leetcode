class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        target = s >> 1

        @cache
        def dfs(i, s):
            nonlocal target
            if s > target or i >= len(nums):
                return False
            return True if s == target else dfs(i + 1, s) or dfs(i + 1, s + nums[i])

        return dfs(0, 0)
