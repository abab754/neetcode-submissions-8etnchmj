class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        hm = {str(i): [str(i+1), str(i-1)] for i in range(1, 9)}
        hm["0"] = ["1", "9"]
        hm["9"] = ["0", "8"]
        
        q = deque(["0000"])
        res = 0
        visit = set()
        while q:
            lenq = len(q)
            for _ in range(lenq):
                pop = q.popleft()
                if pop == target:
                    return res
                if pop in visit or pop in deadends:
                    continue
                visit.add(pop)
                for i in range(len(pop)):
                    for num in hm[pop[i]]:
                        combo = pop[:i] + num + pop[i+1:]
                        
                        if combo not in deadends and combo not in visit:
                            q.append(combo)
            res+=1

        return -1
                 
