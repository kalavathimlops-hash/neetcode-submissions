class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        h = defaultdict(int)
        for i, num in enumerate(numbers):
            h[num] = i
        for i, num in enumerate(numbers):
            comp = target - num
            if comp in h and h[comp] != i:
                return [i + 1, h[comp] + 1]
        