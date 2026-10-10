# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l=0
        h=mountainArr.length()-1
        while l<h:
            mid=(l+h)//2
            if mountainArr.get(mid)<mountainArr.get(mid+1):
                l=mid+1
            else:
                h=mid 

        middle=h        
        low=0

        while low<=middle:
            mid=(low+middle)//2
            if target==mountainArr.get(mid):
                return mid
            elif target<mountainArr.get(mid):
                middle=mid-1
            else:
                low=mid+1 
        high=mountainArr.length()-1
        peak=h+1
        while peak<=high:
            mid=(high+peak)//2
            if target==mountainArr.get(mid):
                return mid
            elif target<mountainArr.get(mid):
                peak=mid+1
            else:
                high=mid-1   
        return -1
        