class Node:
    def __init__(self):
        self.l = 0
        self.r = 0
        self.v = 0


class SegmentTree:
    def __init__(self, n):
        self.tr = [Node() for _ in range(4 * n)]
        self.build(1, 1, n)

    def build(self, u, l, r):
        self.tr[u].l = l
        self.tr[u].r = r
        if l == r:
            return
        mid = (l + r) >> 1
        self.build(u << 1, l, mid)
        self.build(u << 1 | 1, mid + 1, r)

    def modify(self, u, x, v):
        if self.tr[u].l == x and self.tr[u].r == x:
            self.tr[u].v += v
            return
        mid = (self.tr[u].l + self.tr[u].r) >> 1
        if x <= mid:
            self.modify(u << 1, x, v)
        else:
            self.modify(u << 1 | 1, x, v)
        self.pushup(u)

    def pushup(self, u):
        self.tr[u].v = self.tr[u << 1].v + self.tr[u << 1 | 1].v

    def query(self, u, l, r):
        if self.tr[u].l >= l and self.tr[u].r <= r:
            return self.tr[u].v
        mid = (self.tr[u].l + self.tr[u].r) >> 1
        v = self.query(u << 1, l, r) if l <= mid else 0
        if r > mid:
            v += self.query(u << 1 | 1, l, r)
        return v


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        n = max(instructions)
        tree = SegmentTree(n)
        ans = 0
        for num in instructions:
            a = tree.query(1, 1, num - 1)
            b = tree.query(1, 1, n) - tree.query(1, 1, num)
            ans += min(a, b)
            tree.modify(1, num, 1)
        return ans % int((1e9 + 7))
