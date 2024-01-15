class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        times = sorted((d - 1) // s for d, s in zip(dist, speed))
        return next((i for i, t in enumerate(times) if t < i), len(times))
