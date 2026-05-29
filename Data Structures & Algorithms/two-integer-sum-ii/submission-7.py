class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            l = 0
            r = n - 1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r - l) // 2
                if tmp == numbers[mid]:
                    return [i + 1, mid + 1]
                if tmp > numbers[mid]:
                    l = mid + 1
                if tmp < numbers[mid]:
                    r = mid - 1
        return []


        