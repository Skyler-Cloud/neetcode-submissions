class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #check if 2 target/2's 
        half = [i for i,x in enumerate(nums) if x*2==target]
        if len(half)>=2:
            return half

        n=len(nums)-1
        out = {target-nums[n-i]:n-i for i in range(n+1) if nums[n-i]*2!=target}
        for i,x in enumerate(nums):
            if x in out:
                return [i,out[x]]
        