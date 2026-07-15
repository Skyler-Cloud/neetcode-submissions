class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        DoL = {}
        for word in strs:
            d = {}
            for l in word:
                d[l] = 1 + d.get(l,0)
            fs = frozenset({(l,d[l]) for l in d})
            if fs in DoL:
                DoL[fs].append(word)
            else:
                DoL[fs]=[word]
        return list(DoL.values())
        