class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l  <=  r:
            k = (l + r) // 2

            hours = 0
            for pile in piles:
                hours += ( pile + k - 1) // k



                if hours > h:  # early exit: k is too slow
                    break


                
            if hours <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
            return res

        