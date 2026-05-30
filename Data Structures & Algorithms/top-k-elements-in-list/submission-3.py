class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict()
        res = []
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for k, v in count.items():
                res.append(k)
        return sorted(res[::1], reverse = True)
       

        