class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            comp = target - numbers[i]
            for j in range(n - 1, -1, -1):
                if comp == numbers[j]:
                    if i != j:
                        return [numbers[i], numbers[j]]
        return None
        