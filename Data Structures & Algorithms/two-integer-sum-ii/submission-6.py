class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l = 0
        r = n - 1
        while l < r:
            mid = l +(r -l) // 2
            for i in range(n):
                tmp = target - numbers[i]
                if tmp == numbers[mid]:
                    retun [ i + 1, mid +1]
                if tmp > numbers[mid]:
                    r = mid - 1
                if tmp < numbers[mid]:
                    l = mid + 1
        return []


        