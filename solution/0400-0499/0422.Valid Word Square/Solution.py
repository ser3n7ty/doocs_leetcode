class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        m = len(words)
        n = max(len(w) for w in words)
        if m != n:
            return False
        return all(
            words[j] == "".join(w[j] for w in words if j < len(w))
            for j in range(n)
        )
