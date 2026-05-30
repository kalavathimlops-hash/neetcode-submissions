class Solution:
    def isAnagram(self,s:str,t:str)->bool:
        if len(s)!=len(t):
            return False
        countS,countT={},{}
        for i in range(len(s)):
            countSs[i] = 1+countS.get(s[i],0)
            countTs[i] =1+countT.get(t[i],0)
        return countS ==countT      