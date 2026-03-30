import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position[i], speed[i]) for i in range(len(speed))]
        fleets = 0
        fastest = 0
        for p,s in  sorted(pairs, reverse=True):
            time = (target - p)/s
            if fastest < time:
                fleets+=1
                fastest = time
        return fleets
            
            