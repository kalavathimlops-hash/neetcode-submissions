class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)
        res = 0
        for n in nums:
            if n in set_nums:
                res += 1
        
        if res >= 1:
            return True
        else:
            return False




            
            
        