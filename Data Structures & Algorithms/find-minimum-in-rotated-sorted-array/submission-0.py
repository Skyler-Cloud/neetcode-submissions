class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while l<r:
            m=(l+r)//2
            if nums[l]>nums[m]:
                r=m
            elif nums[m]<nums[r]:
                return nums[l]
            else:
                l=m+1
        return nums[l]