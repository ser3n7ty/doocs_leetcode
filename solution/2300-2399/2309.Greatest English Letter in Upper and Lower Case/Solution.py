class Solution:
    def greatestLetter(self, s: str) -> str:
        ss = set(s)
        return next(
            (c for c in ascii_uppercase[::-1] if c in ss and c.lower() in ss), ''
        )
