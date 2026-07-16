from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #dict of k: most recent appearance.
        # store substring start.
        # For each string, check dict for character & update val
        #   if last appearance > substr start, reset substring start to last appearance.
            # aka start = max (start,last_appear)
        D = defaultdict(int)
        length = 0
        start=0
        for i,c in enumerate(s):
            if c in D:
                length = max(length,i-start)
                start = max(start,D[c]+1)
            D[c]=i
        return max(length,len(s)-start)


