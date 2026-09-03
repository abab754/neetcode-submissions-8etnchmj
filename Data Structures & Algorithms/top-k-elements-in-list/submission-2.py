class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)
        for num in nums:
            hm[num] += 1

        freq = [[] for i in range(len(nums) + 1)]
        for key, v in hm.items():
            freq[v].append(key)
        
        res = []
        j = 0
        for i in range(len(nums), -1, -1):
            while j < k and freq[i]:
                res.append(freq[i][-1])
                freq[i].pop()
                j+=1
            if j ==k :
                return res

        return res

            
