class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        maxNum = m + n
        temp = m;
        for i in range(n):
            if(temp<=maxNum):
                nums1[temp+i] = nums2[i]
        nums1.sort()
                
        