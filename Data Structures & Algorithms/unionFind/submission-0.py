class UnionFind:
    
    def __init__(self, n: int):
        self.rank = [1] * (n+1)
        self.parent = [i for i in range(n+1)]
        self.components = n

    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        if self.isSameComponent(x, y):
            return False
        root_x = self.find(x)
        root_y = self.find(y)
        if self.rank[root_x] >= self.rank[root_y]:
            self.parent[root_y] = root_x
            self.rank[root_x]+= self.rank[root_y]
        else:
            self.parent[root_x] = root_y
            self.rank[root_y]+=self.rank[root_x]
        self.components-=1
        return True
        

    def getNumComponents(self) -> int:
        return self.components
