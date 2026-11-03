class Solution:
    def reverseWords(self, s: str) -> str:
        l=[]
        st=""
        for i in s.split():
            l.append(i)
        l=l[::-1]
        return " ".join(l)