class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ind=set(nums)
        maxct = 0
        for x in ind:
            ct = 1
            while x+ct in ind:
                ct += 1
            maxct = max(maxct,ct)
        return maxct
            
            