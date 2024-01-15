class Solution:
    def pivotInteger(self, n: int) -> int:
        return next(
            (x for x in range(1, n + 1) if (1 + x) * x == (x + n) * (n - x + 1)),
            -1,
        )
