class Solution:
    def longestPalindrome(self, s: str) -> int:
        has_odd=False
        count=0
        output=0
        s_map={}
        for i in s:
            s_map[i]=s_map.get(i,0)+1
        for char in s_map:
            if s_map[char]%2==0:
                output+=s_map[char]
            else:
                output=output+s_map[char]-1
                has_odd=True
        if has_odd==True:
            output+=1       
        return output