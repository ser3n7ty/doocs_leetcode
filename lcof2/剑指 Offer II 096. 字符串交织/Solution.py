class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def dfs(i: int, j: int) -> bool:
            if i >= m and j >= n:
                return True
            k = i + j
            if i < m and s1[i] == s3[k] and dfs(i + 1, j):
                return True
            return bool(j < n and s2[j] == s3[k] and dfs(i, j + 1))

        m, n = len(s1), len(s2)
        return False if m + n != len(s3) else dfs(0, 0)
