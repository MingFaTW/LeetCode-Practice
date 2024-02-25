class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        string = ""
        minLength = min(len(word1),len(word2))
        for i in range(minLength):
            string = string + word1[i] + word2[i]
        string += word1[minLength:] + word2[minLength:]
        return string
        
        