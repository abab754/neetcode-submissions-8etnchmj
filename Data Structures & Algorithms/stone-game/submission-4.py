class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            even = True if (l+r) % 2 else False
            if even:
                dp[(l, r)] = max(piles[l]+ dfs(l+1, r), piles[r] + dfs(l, r-1))
                return dp[(l, r)]
            else:
                dp[(l, r)] = max(dfs(l+1, r), dfs(l, r-1))
                return dp[(l, r)]
        
        a = dfs(0, len(piles)-1)
        return a > sum(piles) - a