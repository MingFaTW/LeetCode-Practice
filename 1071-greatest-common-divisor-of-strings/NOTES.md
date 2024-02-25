​# Greatest Common Divisor of Strings

## 問題描述

給定兩個字串 `str1` 和 `str2`，撰寫一個函式判斷它們的最大公因子（最長的共同首碼字串）。

## 解決方案

使用一個循環從較小的字串長度開始遞減，檢查是否存在一個長度 `l`，使得 `str1` 和 `str2` 都是以 `l` 爲週期的字串。如果找到符合條件的 `l`，則返回 `str1` 的前 `l` 個字元作爲最大公因子，否則返回空字串。

## 代碼實現

```python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        def isDivisor(l):
            if len1 % l or len2 % l:
                return False
            f1, f2 = len1 // l, len2 // l
            return str1[:l] * f1 == str1 and str1[:l] * f2 == str2

        for l in range(min(len1, len2), 0, -1):
            if isDivisor(l):
                return str1[:l]
        return ""
