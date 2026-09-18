class UnionFind:
    
    def __init__(self, n: int):
        self.numComponents = n
        self.parent = [i for i in range(n+1)]
        self.rank = [1 for i in range(n+1)]

    def find(self, x: int) -> int:
        px = self.parent[x]
        while px != self.parent[px]:
            px = self.parent[px]
        return px
       
    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        if self.isSameComponent(x, y):
            return False
        px = self.find(x)
        py = self.find(y)
        if self.rank[px] >= self.rank[py]:
            self.parent[py] = px
            self.rank[px] += self.rank[py]
        else:
            self.parent[px] = py
            self.rank[py] += self.rank[px]
        self.numComponents -= 1
        return True

    def getNumComponents(self) -> int:
        return self.numComponents
        
