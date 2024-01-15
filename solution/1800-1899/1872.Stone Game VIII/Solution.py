class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        @cache
        def dfs(i: int) -> int:
            return s[-1] if i >= len(stones) - 1 else max(dfs(i + 1), s[i] - dfs(i + 1))

        s = list(accumulate(stones))
        return dfs(1)
