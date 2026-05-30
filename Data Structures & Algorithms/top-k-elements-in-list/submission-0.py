class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict()
        res = []
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for k, v in count.items():
            if v >= 2:
                res.append(k)
        return res[::1]
       

        