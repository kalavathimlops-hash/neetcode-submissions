class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            c = target - nums[i]
            for j in range(1, len(nums)):
                if nums[j] == c and i != j:
                    return [i, j]
        