class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # at most n/k
        freq = {}
        for x in nums:
            freq[x] = 1 + freq.get(x,0)
        L = [[] for _ in range(len(nums)+1)]
        for num,ct in freq.items():
            L[ct].append(num)
        out = [x for l in L for x in l]
        return out[-k:]