class Solution:
    def replaceSpace(self, s: str) -> str:
        ans = ['%20' if c == ' ' else c for c in s]
        return ''.join(ans)
