class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq={}
        l=[]
        for i in strs:
            l.append("".join(sorted(i)))
        for j in strs:
            s="".join(sorted(j))
            if s in freq:
                freq[s].append(j)
            else:
                freq[s]=[j]
        return list(freq.values())        
                    