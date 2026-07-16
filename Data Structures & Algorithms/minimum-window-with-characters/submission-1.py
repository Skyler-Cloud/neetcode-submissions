from collections import Counter, defaultdict, deque
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        out = ''
        ctT = Counter(t)
        numchar = len(ctT)
        ctW = defaultdict(int)
        indices = deque() #(i,c)
        for i,c in enumerate(s):
            if c in ctT:
                ctW[c]+=1
                indices.append((i,c))
                if ctW[c]==ctT[c]:
                    numchar -= 1
            while numchar==0:
                li,lc=indices.popleft()
                print(s[li:i+1])
                if ctW[lc]==ctT[lc]:
                    if out == '' or i-li+1<len(out):
                        out = s[li:i+1]
                    numchar+=1
                ctW[lc]-=1
        return out
                    