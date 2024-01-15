class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @cache
        def dfs(i: int) -> bool:
            if i == 0:
                return False
            j = 1
            while j**2 <= i:
                if not dfs(i - j**2):
                    return True
                j += 1
            return False

        return dfs(n)
