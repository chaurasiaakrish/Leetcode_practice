from bisect import bisect_left
class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        count=0
        for i in arr1:
            x=bisect_left(arr2,(i-d))
            if x<len(arr2) and arr2[x]<=i+d:
                continue
            else:
                count+=1  
        return count          