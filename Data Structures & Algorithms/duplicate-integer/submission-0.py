class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)
        for n in nums:
            if n in set_nums:
                return true
            else:
                return false



            
            
        