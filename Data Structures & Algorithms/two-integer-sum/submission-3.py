class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # store target-num
        # check if in there.
        minus = {}
        for i,num in enumerate(nums):
            if target-num in minus:
                return [minus[target-num],i]
            minus[num]=i

        