class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i =0
        j =0
        x = 0
        while i<len(t) and j<len(s) :
            if t[i]==s[j] :
                j+=1
                x+=1
            i+=1
        if x == len(s) :
            return True
        return False
