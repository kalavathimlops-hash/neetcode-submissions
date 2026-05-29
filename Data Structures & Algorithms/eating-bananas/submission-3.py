

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            hours = 0
            for pile in piles:
                # integer ceiling: ceil(pile / k) == (pile + k - 1) // k
                hours += math.ceil(pile / k)
                if hours > h:  # early exit: k is too slow
                    break

            if hours <= h:
                res = k        # feasible; try smaller k
                r = k - 1
            else:
                l = k + 1      # too slow; try larger k

        return res
