class Solution:
    def minQueenMoves(self, source: list[int], target: list[int]) -> int:
        if abs(source[0]-target[0])==abs(source[1]-target[1]):
            diff=abs(source[0]-target[0])
            if diff==0:
                return 0
            else:
                return 1    
            return 1
        elif source[0]==target[0] or source[1]==target[1]:
            return 1 
        else:
            return 2        