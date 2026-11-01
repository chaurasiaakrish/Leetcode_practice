class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        x=0;y=0
        merge_str=""
        while x<len(word1) and y<len(word2):
            merge_str=merge_str + word1[x] + word2[y]
            x+=1
            y+=1
        while x<len(word1):
            merge_str=merge_str +  word1[x] 
            x+=1
        while y<len(word2):
            merge_str=merge_str +  word2[y]
            y+=1        
        return   merge_str  