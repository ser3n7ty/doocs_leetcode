class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        f = [[1]]
        for _ in range(numRows - 1):
            g = [1] + [a + b for a, b in pairwise(f[-1])] + [1]
            f.append(g)
        return f
