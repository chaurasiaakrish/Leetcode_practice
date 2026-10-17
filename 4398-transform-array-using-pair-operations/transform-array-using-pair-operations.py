class Solution:
    def canTransform(self, source: list[int], target: list[int]) -> bool:
        if sum(source)==sum(target):
            return True
        else:
            return False    