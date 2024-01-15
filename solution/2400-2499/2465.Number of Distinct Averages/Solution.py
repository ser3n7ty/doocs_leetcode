class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        return len({nums[i] + nums[-i - 1] for i in range(len(nums) >> 1)})
