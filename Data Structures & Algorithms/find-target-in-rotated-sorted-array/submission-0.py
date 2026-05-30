class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[r] >= nums[l]:
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    return mid
            
            if nums[mid] >= target or nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
            if  nums[mid] <= target or  nums[mid] <= nums[r]:
                r = mid - 1
            else:
                l = mid + 1
            if nums[mid] == target:
                return mid
        return  -1
            

                

        