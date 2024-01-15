class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        vis = set()
        ans = 0
        for i, _ in enumerate(range(n), start=1):
            while i in vis:
                i += 1
            ans += i
            vis.add(target - i)
        return ans
