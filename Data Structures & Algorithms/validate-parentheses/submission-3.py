class Solution:
    def isValid(self, s: str) -> bool:
        L=[]
        bkts = {'(':')', '[':']','{':'}'}
        for c in s:
            if c in bkts:
                L.append(bkts[c])
            else:
                if not L or L.pop() != c:
                    return False
        return not L
