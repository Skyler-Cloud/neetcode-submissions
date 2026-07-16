from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        most = 1 # in a window excluding k
        most_window=0
        l=0 #move l if substring can't all be 1 color. ie length > most+k
        r=0
        freq = defaultdict(int) #k: # appearances in window
        while r<len(s):
            freq[s[r]]+=1
            most_window = max(most_window,freq[s[r]])
            print(most_window)
            # move l
            if r-l+1 > most_window+k:
                most = max(most_window,most)
                remax = most_window == freq[s[l]]
                freq[s[l]]-=1
                l+=1
                if remax:
                    most_window=max(freq.values())
            r+=1
        return min(max(most,most_window)+k,len(s))

        
                


