class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        for i in range(n >> 1):
            ans.extend((i + 1, -(i + 1)))
        if n & 1:
            ans.append(0)
        return ans
