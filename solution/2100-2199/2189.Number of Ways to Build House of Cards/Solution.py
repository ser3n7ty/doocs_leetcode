class Solution:
    def houseOfCards(self, n: int) -> int:
        @cache
        def dfs(n: int, k: int) -> int:
            x = 3 * k + 2
            if x > n:
                return 0
            return 1 if x == n else dfs(n - x, k + 1) + dfs(n, k + 1)

        return dfs(n, 0)
