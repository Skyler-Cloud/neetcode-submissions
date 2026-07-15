class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # at most n/k
        freq = {}
        for x in nums:
            freq[x] = 1 + freq.get(x,0)
        L = sorted([(freq[x],x) for x in freq])
        return [x for _,x in L[-k:]]