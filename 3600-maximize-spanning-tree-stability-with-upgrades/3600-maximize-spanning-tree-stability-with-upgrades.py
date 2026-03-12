from typing import List

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
        self.comp = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        if self.rank[pa] < self.rank[pb]:
            pa, pb = pb, pa
        self.parent[pb] = pa
        if self.rank[pa] == self.rank[pb]:
            self.rank[pa] += 1
        self.comp -= 1
        return True


class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:

        def can(x):
            dsu = DSU(n)
            upgrades = 0

            # include must edges
            for u, v, s, must in edges:
                if must:
                    if s < x:
                        return False
                    if not dsu.union(u, v):
                        return False

            optional = []

            for u, v, s, must in edges:
                if not must:
                    optional.append((u, v, s))

            # first edges already >= x
            for u, v, s in optional:
                if s >= x:
                    dsu.union(u, v)

            # edges needing upgrade
            for u, v, s in optional:
                if s < x and s*2 >= x:
                    if dsu.union(u, v):
                        upgrades += 1
                        if upgrades > k:
                            return False

            return dsu.comp == 1

        lo, hi = 0, 2*10**5
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans