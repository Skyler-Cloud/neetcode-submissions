from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        D = defaultdict(list)
        for s in strs:
            ctr = Counter(s)
            D[str(sorted(Counter(s).items()))].append(s)
        return list(D.values())