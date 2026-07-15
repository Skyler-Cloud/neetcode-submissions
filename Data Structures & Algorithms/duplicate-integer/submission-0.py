class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        S = set(nums)
        return len(nums)>len(S)