class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        doubles = defaultdict(list)
        singles = defaultdict(list)
        for i,x in enumerate(nums):
            singles[x].append(i)
            for j in range(i+1,len(nums)):
                doubles[-x-nums[j]].append((i,j))
        out = set()
        for k,pairs in (doubles).items():
            start = 0 # pair indices
            for i in singles[k]:
                while start < len(pairs) and pairs[start][0] <= i:
                    start +=1
                if start>= len(pairs):
                    break
                out.update({tuple(sorted([nums[i],nums[j],nums[k]])) for j,k in pairs[start:]})
        return [list(x) for x in out]
