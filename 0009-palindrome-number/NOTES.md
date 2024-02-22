​這道題目是判斷數字x是否為回文數字(Palindrome Number)，有兩種做法：
1.  ＃將x轉為str型態，使用x[::-1]將字串反轉來進行對比
    ```python
    class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x[::-1] == x:
                return True
        return False
    ```
2.  ＃使用數學來將x反轉成temp
    ```
    如果輸入的數字小於0，則直接返回False，因為負數不可能是回文數。
    如果輸入的數字不小於0，則進行如下處理：
    創建一個變量 originalNum 來保存輸入的原始數字。
    創建一個變量 temp 並初始化為0，用來保存反向重建的數字。
    進入一個 while 迴圈，該迴圈在 x 不為0時持續運行：
    在每一次迴圈中，將 temp 乘以10，以便為下一位數字留出空間，然後加上 x 的個位數字（x % 10）。
    將 x 除以10以去掉已處理的最後一位數字（x // 10）。
    迴圈結束後，檢查 originalNum 是否等於 temp，如果是，則返回True，否則返回False。
    ```
    ```python
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
    ```
