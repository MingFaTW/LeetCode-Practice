class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1,len2 = len(str1),len(str2)
        
        def isGCD(l):
            if len1 % l or len2 % l:
                return False
            n1 , n2 = len1//l , len2//l
            return str1[:l] * n1 == str1 and str1[:l] * n2 == str2

        for l in range(min(len1,len2),0,-1):
            if isGCD(l):
                return str1[:l]
        return ""