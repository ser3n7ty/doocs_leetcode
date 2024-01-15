class Solution:
    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:
        def check(w: str) -> bool:
            return all(d[c] == num[i] for i, c in enumerate(w))

        d = dict(zip(ascii_lowercase, "22233344455566677778889999"))
        return [w for w in words if check(w)]
