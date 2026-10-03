class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(i, cur):
            if (i, cur) in dp:
                return dp[(i, cur)]
            if i >= len(coins) or cur > amount:
                return 0
            if cur == amount:
                return 1
            res = dfs(i, cur+coins[i]) + dfs(i+1, cur) 
            dp[(i, cur)] = res
            return dp[(i, cur)]
        
        return dfs(0, 0)