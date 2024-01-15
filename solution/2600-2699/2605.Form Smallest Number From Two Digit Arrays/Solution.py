class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 100
        for a in nums1:
            for b in nums2:
                ans = min(ans, a) if a == b else min(ans, 10 * a + b, 10 * b + a)
        return ans
