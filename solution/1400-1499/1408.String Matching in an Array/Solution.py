class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        return [
            s
            for i, s in enumerate(words)
            if any(i != j and s in t for j, t in enumerate(words))
        ]
