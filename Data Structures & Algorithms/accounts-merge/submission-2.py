class UnionFind():
    def __init__(self, n):
        self.numComponents = n
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

    def find(self, x):
        px = self.parent[x]
        while px != self.parent[px]:
            px = self.parent[px]
        return px

    def same(self, x, y):
        px = self.find(x)
        py = self.find(y)
        return px == py
    
    def union(self, x, y):
        if self.same(x, y):
            return False
        px = self.find(x)
        py = self.find(y)
        if self.rank[px] >= self.rank[py]:
            self.parent[py] = px
            self.rank[px] += self.rank[py]
        else:
            self.parent[px] = py
            self.rank[py] += self.rank[px]
        self.numComponents-=1
        return True

    def getComps(self):
        return self.numComponents

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        hm = {}
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                if accounts[i][j] in hm:
                    uf.union(i, hm[accounts[i][j]])
                else:
                    hm[accounts[i][j]] = i
        hm2 = defaultdict(set)
        for i in range(len(uf.parent)):
            hm2[uf.find(i)] |= set(accounts[i])
        res = []
        for v in hm2.values():
            name = list(v)[0]
            emails = [i for i in v if i != name]
            res.append([name] + sorted(emails))

        return res