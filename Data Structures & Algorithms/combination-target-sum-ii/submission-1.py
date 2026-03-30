class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(i, curSum, cur):
            if curSum == target:
                res.append(sorted(cur.copy()))
                return
            if i>=len(candidates) or curSum > target:
                return
            cur.append(candidates[i])
            dfs(i+1, curSum + candidates[i], cur)
            cur.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1, curSum, cur)
        
        dfs(0, 0, [])
        return res