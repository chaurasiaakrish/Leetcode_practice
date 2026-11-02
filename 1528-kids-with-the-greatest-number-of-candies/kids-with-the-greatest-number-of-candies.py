class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maxx=max(candies)
        l=[]
        for i in candies:
            if (i+extraCandies)>=maxx:
                l.append(True)
            else:
                l.append(False)  
        return l          
