class Solution:
    def maxArea(self, height: list[int]) -> int:
        left_max=float("-inf")
        right_max=float("-inf")
        result=float("-inf")
        i=0
        j=len(height)-1
        while i<j:
            left_max=max(height[i],left_max)
            right_max=max(height[j],right_max)                
            width=j-i
            res=width*min(left_max,right_max)
            result=max(result,res)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1    
        return result    