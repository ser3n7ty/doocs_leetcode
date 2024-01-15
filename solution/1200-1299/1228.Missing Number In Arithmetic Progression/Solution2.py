class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)
        d = (arr[-1] - arr[0]) // n
        return next(
            (arr[i - 1] + d for i in range(1, n) if arr[i] != arr[i - 1] + d),
            arr[0],
        )
