class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        memo = {} # k = index & target, v = list of lists
        def comb(i,t):
            if (i,t) in memo:
                return memo[i,t]
            if t==0:
                return [[]]
            if t < 0 or i>=len(nums):
                return []
            out = []
            for num_i in range(0,t//nums[i]+1):
                out += [[nums[i]]*num_i+sublist for sublist in comb(i+1,t-nums[i]*num_i)]
            memo[i,t]=out
            return out
        return comb(0,target)
                

