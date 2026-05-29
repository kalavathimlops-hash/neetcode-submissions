class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #base case
        if len(nums) == 0:
            return [[]]
        
        #recursion
        perm = self.permute(nums[1:])

        #back tracking
        res = []
        for p in perm:
            for i in range(len(p)+1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        return res
        