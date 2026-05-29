class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        n = len(s2)
        m = len(s1)
        if m > n or m == 0:
            return False

        for i in range(n):
            for j in range(i, n):
                substr = s2[i : j + m]
                substr = sorted(substr)
                if substr == s1:
                    return True
        return False
        