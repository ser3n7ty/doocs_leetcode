class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        return [
            i
            for i in range(n)
            if any(abs(i - j) <= k and nums[j] == key for j in range(n))
        ]
