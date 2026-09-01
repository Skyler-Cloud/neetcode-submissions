class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        out = []

        def comb(i,t, curr_list):
            if t==0:
                out.append(curr_list)
                return
            if t < 0 or i>=len(nums) or nums[i]>t:
                return
            for num_i in range(0,t//nums[i]+1):
                comb(i+1,t-nums[i]*num_i, curr_list + [nums[i]]*num_i)
        comb(0,target,[])
        return out
                

