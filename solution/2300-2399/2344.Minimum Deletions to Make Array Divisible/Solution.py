class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        x = numsDivide[0]
        for v in numsDivide[1:]:
            x = gcd(x, v)
        nums.sort()
        return next((i for i, v in enumerate(nums) if x % v == 0), -1)
