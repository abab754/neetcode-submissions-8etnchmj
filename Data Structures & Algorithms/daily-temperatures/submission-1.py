class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = []
        for curDay in range(len(temperatures)):
            while stack and temperatures[curDay] > stack[-1][0]:
                temp, day = stack.pop()
                res[day] = curDay - day
            
            stack.append((temperatures[curDay], curDay))
        
        return res
            