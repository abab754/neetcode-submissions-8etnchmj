class TimeMap:

    def __init__(self):
        self.hm = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hm:
            self.hm[key] = []
        self.hm[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hm:
            return ""
        lst = self.hm.get(key, [])
        res = ""
        l = 0
        r = len(lst)- 1
        while l <= r:
            m = (l+r) // 2
            if lst[m][1] <= timestamp:
                res = lst[m][0]
                l = m+1
            else:
                r = m - 1
        return res
