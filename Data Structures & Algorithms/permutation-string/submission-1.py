class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        n = len(s2)
        for i in range(n):
            for j in range(i, n):
                substr = s2[i : j]
                substr = sorted(substr)
                if substr == s1:
                    return True
        return False
        