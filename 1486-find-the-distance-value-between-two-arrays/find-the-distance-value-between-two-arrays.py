class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count =len(arr1)
        i=0;j=0
        while i <len(arr1):
            j=0
            while j<len(arr2):
                if abs(arr1[i]-arr2[j])>d:
                    j+=1
                else:
                    count-=1
                    break    
            i+=1
        return count            
