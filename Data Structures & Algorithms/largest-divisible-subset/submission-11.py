class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        memo = {} # curr i, last val
        def memoSubset(i,val):
            if (i,val) in memo:
                return memo[i,val]
            if i>=len(nums):
                return []
            memo[i,val]=[]
            # first val excluding i st divides val
            for k in range(len(nums)-1,i,-1):
                if nums[k]%val==0:
                    wo=memoSubset(k,val)
                    if len(wo)>len(memo[i,val]):
                        memo[i,val]=wo
            # first val including i that divides i
            w=[nums[i]]
            for k in range(i+1,len(nums)):
                if nums[k]%nums[i]==0:
                    w.extend(memoSubset(k,nums[i]))
                    break
            if len(w)>len(memo[i,val]):
                memo[i,val]=w
            return memo[i,val]
        return memoSubset(0,1)