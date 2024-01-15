class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        return 0 if n == 0 else n ^ self.minimumOneBitOperations(n >> 1)
