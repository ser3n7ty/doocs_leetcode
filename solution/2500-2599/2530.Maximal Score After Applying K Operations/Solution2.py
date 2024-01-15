class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        for i, v in enumerate(nums):
            nums[i] = -v
        heapify(nums)
        return 0 - sum(heapreplace(nums, -ceil(-nums[0] / 3)) for _ in range(k))
