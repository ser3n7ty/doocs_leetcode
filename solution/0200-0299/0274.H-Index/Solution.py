class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        return next(
            (h for h in range(len(citations), 0, -1) if citations[h - 1] >= h), 0
        )
