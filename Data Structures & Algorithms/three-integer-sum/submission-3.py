class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i , a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            l = i + 1
            r = len(nums) - 1
            while l < r:
                threesum = nums[i] + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    temp = [nums[i], nums[l], nums[r]]
                    res.append(temp)
                    l += 1
                    r -= 1
                if nums[l] == nums[l-1] and l < r:
                    l += 1
        return res
                        
        