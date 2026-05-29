class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict()
        res = []
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        sorted_dict = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        for key, v in sorted_dict.items():
            res.append(key)
        return res[:k]

       

        