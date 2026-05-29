class Solution:
    def maxArea(self, heights: List[int]) -> int:
       n = len(heights)
       l = 0
       r = n - 1
       res = 0
       while l < r:
            h = min(heights[l], heights[r])
            w = r -l
            area = w * h
            res = max(res, area)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
       return res
    
    
        