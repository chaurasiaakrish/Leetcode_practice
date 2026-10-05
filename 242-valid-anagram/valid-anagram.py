class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq={}
        t_freq={}
        flag=False
        if len (s)!=len(t):
            return False
        else:

            for i in s:
                s_freq[i]=s_freq.get(i,0)+1
            for i in t:
                t_freq[i]=t_freq.get(i,0)+1    
            for i in s_freq:
                if s_freq.get(i,0)==t_freq.get(i,0):
                    continue
                else:
                    return False
            return True                  
        