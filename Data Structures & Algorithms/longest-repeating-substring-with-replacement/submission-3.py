from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        most = 1 # in a window excluding k
        l=0 #move l if substring can't all be 1 color. ie length > most+k
        r=0
        freq = defaultdict(int) #k: # appearances in window
        while r<len(s):
            freq[s[r]]+=1
            most = max(most,freq[s[r]])
            # move l
            if r-l+1 > most+k:
                freq[s[l]]-=1
                l+=1
            r+=1
        return min(most+k,len(s))

        
                


