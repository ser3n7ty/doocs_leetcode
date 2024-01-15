class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def dfs(nums: List[float]):
            n = len(nums)
            if n == 1:
                return abs(nums[0] - 24) < 1e-6
            ok = False
            for i in range(n):
                for j in range(n):
                    if i != j:
                        nxt = [nums[k] for k in range(n) if k not in [i, j]]
                        for op in ops:
                            match op:
                                case "/":
                                    if nums[j] == 0:
                                        continue
                                    ok |= dfs(nxt + [nums[i] / nums[j]])
                                case "*":
                                    ok |= dfs(nxt + [nums[i] * nums[j]])
                                case "+":
                                    ok |= dfs(nxt + [nums[i] + nums[j]])
                                case "-":
                                    ok |= dfs(nxt + [nums[i] - nums[j]])
                            if ok:
                                return True
            return ok

        ops = ("+", "-", "*", "/")
        nums = [float(x) for x in cards]
        return dfs(nums)
