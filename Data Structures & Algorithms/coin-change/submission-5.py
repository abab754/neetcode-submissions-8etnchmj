class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        res = 1
        q = deque(coins)
        visit = set()
        while q:
            lenq = len(q)
            for i in range(lenq):
                popped_amt = q.popleft()
                visit.add(popped_amt)
                if popped_amt > amount:
                    continue
                if popped_amt == amount:
                    return res
                for coin in coins:
                    to_add = popped_amt + coin
                    if to_add not in q and to_add not in visit and to_add <= amount:
                        q.append(to_add)

            res+=1
        return -1