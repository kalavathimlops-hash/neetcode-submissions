class Solution:
    def isDuplicate(self,nums:List[int]) -> bool:
        hashset=set()
        for num in nums:
            if num in hashset:
                return True
            hashset.append(num)
            return False    