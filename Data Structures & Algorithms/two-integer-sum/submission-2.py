class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # store target-num
        # check if in there.
        minus = {}
        for i,num in enumerate(nums):
            if num in minus:
                return [minus[num],i]
            elif target-num not in minus:
                minus[target-num]=i

        