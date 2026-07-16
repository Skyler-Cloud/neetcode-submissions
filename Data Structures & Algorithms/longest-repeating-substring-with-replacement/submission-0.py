from collections import Counter
def count(s,k,i):
        j=i
        ch = s[i]
        while j<len(s):
            if s[j]!=ch:
                if k==0:
                    return j-i
                k-=1
            j+=1
        return min(j-i+k,len(s))
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        most = 0
        if not s:
            return 0
        prev = ''
        for i,c in enumerate(s):
            if prev != c:
                most = max(most,count(s,k,i))
        return most