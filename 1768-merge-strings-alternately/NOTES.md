#​ 解題思路

已知有兩個字串(word1,word2)輸入，將兩個字串以間隔合併(string)，並且word1為率先輸入string之字串：
> 如word1[0] word2[0] word1[1] word2[1]
```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        string = ""
        minLength = min(len(word1),len(word2))
        for i in range(minLength):
            string = string + word1[i] + word2[i]
        string += word1[minLength:] + word2[minLength:]
        return string
```
