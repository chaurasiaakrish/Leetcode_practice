class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=[]
        for word in s.split():
            l.append(word)
        return len(l[-1])    