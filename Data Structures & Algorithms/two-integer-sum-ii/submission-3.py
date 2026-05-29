class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            comp = target - numbers[i]
            for j in range(i + 1, n):
                if i < j:
                    if comp == numbers[j]:
                        return [i + 1 , j + 1]
        return []
        