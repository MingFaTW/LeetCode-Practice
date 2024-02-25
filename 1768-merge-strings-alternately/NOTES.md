#​ 解題思路

已知有兩個字串(word1,word2)輸入，將兩個字串以間隔合併(string)，並且word1為率先輸入string之字串：
> 如word1[0] word2[0] word1[1] word2[1]
```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        string = ""
        minLength = min(len(word1),len(word2)) #計算兩字串的最小值
        for i in range(minLength):             #將兩個字串逐一輸入新的字串直到超過最小值
            string = string + word1[i] + word2[i]
        string += word1[minLength:] + word2[minLength:] #將剩餘的字串輸入至string後方
        return string
```
