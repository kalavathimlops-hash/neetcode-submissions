class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict()
        res = []
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for key, v in count.items():
                res.append(key)
                sorted_res = sorted(res, reverse = True)
        return sorted_res[:k]
       

        