class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        else:
            originalNum = x
            temp = 0
            while(x!=0):
                temp = temp * 10 + x % 10
                x = x // 10
            if(originalNum == temp):
                return True
            else: return False