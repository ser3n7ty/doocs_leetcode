class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        @cache
        def dfs(x):
            return 0 if x not in s else 1 + dfs(x * x)

        s = set(nums)
        ans = max(dfs(x) for x in nums)
        return -1 if ans < 2 else ans
