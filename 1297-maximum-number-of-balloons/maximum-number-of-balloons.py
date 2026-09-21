class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ans=float("inf")
        word="balloon"
        freq1={}
        freq2={}
        for i in range(len(word)):
            freq1[word[i]]=freq1.get(word[i],0)+1
        for i in range(len(text)):
            freq2[text[i]]=freq2.get(text[i],0)+1
        for value in freq1:
            count = freq2.get(value, 0) // freq1[value]
            ans = min(ans, count)

        return ans
