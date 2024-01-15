class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def dfs(i: int, j: int) -> int:
            return 0 if i > j else max(nums[i] - dfs(i + 1, j), nums[j] - dfs(i, j - 1))

        return dfs(0, len(nums) - 1) >= 0
