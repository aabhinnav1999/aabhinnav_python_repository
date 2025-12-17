from typing import List

class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0]*n
    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb: 
            return False
        if self.r[ra] < self.r[rb]:
            ra, rb = rb, ra
        self.p[rb] = ra
        if self.r[ra] == self.r[rb]:
            self.r[ra] += 1
        return True

def minReassignments(link_nodes: int, link_from: List[int], link_to: List[int]) -> int:
    m = len(link_from)
    if m < link_nodes - 1:
        return -1                        

    dsu = DSU(link_nodes)
    for u, v in zip(link_from, link_to):
        dsu.union(u-1, v-1)   

    comps = len({dsu.find(i) for i in range(link_nodes)})
    return comps - 1

# Example
print(minReassignments(4, [1,1,3], [2,3,2]))  # -> 1