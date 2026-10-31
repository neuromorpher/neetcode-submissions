class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        countS, countT= {}, {}

        if len(s) != len(t):

            return False

        for i in range(len(s)):

            countS[s[i]] = countS.get(s[i], 1) + 1
            countT[t[i]] = countT.get(t[i], 1) + 1
        
        if countS == countT:

            return True 
        return False

        

             