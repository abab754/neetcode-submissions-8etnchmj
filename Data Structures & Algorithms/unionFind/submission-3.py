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
        px = self.find(x)
        py = self.find(y)
        return px == py

    def union(self, x: int, y: int) -> bool:
        if self.isSameComponent(x, y):
            return False
        px = self.find(x)
        py = self.find(y)
        if self.rank[px] >= self.rank[py]:
            self.rank[px] += self.rank[py]
            self.parent[py] = px
            self.numComponents-=1
        else:
            self.rank[py] += self.rank[px]
            self.parent[px] = py
            self.numComponents-=1
        return True
        
    def getNumComponents(self) -> int:
        return self.numComponents
