class solution:
    def hasduplicate(self,nums:List[int]) -> bool:
        for i in nums:
            for j in i:
                i = j
            return True
        else:
           return False 
solution=solution()           