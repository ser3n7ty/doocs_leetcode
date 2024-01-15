class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        x1, y1, x2, y2 = 0, 0, m - 1, n - 1
        ans = []
        while x1 <= x2 and y1 <= y2:
            ans.extend(matrix[x1][j] for j in range(y1, y2 + 1))
            ans.extend(matrix[i][y2] for i in range(x1 + 1, x2 + 1))
            if x1 < x2 and y1 < y2:
                ans.extend(matrix[x2][j] for j in range(y2 - 1, y1 - 1, -1))
                ans.extend(matrix[i][y1] for i in range(x2 - 1, x1, -1))
            x1, y1 = x1 + 1, y1 + 1
            x2, y2 = x2 - 1, y2 - 1
        return ans
