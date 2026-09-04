class TimeMap:

    def __init__(self):
        self.hm = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        tup = (value, timestamp)
        self.hm[key].append(tup)

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.hm or len(self.hm[key]) == 0:
            return res
        
        l = 0 
        r = len(self.hm[key]) - 1
        while l <= r:
            m = (l+r)//2
            if self.hm[key][m][1] == timestamp:
                return self.hm[key][m][0]
            elif self.hm[key][m][1] < timestamp:
                l = m+1
            else:
                r = m - 1
        
        for i in range(len(self.hm[key])- 1, -1, -1):
            if self.hm[key][i][1] <= timestamp:
                return self.hm[key][i][0]
        
        return ""

    



        