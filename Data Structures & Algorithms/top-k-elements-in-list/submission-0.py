class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        hm = {}
        res = []
        for num in nums:
            hm[num] = hm.get(num, 0) + 1
        
        for num, frq in hm.items():
            freq[frq].append(num)
        
        i = len(freq)-1
        while i >= 0:
            while len(res) < k and len(freq[i]) > 0:
                res.append(freq[i].pop())
            i-=1
        return res
           
            
