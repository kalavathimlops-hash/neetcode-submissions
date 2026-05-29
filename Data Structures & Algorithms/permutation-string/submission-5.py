class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        n = len(s2)
        m = len(s1)
        if m > n:
            return False
        if m == 0:
            return False
        for i in range(n - m + 1):
            substr = sorted(s2[i : i + m])
            if substr == s1:
                return True
        return False
        