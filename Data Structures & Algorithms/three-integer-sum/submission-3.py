from collections import Counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        front = 0
        mid=1
        back = len(nums)-1
        triples = set()
        while front +1 < len(nums) and nums[front]<=0:
            while mid<back and nums[back]>=0:
                total = nums[front]+nums[mid]+nums[back]
                if total<0:
                    mid +=1
                elif total >0:
                    back -= 1
                else:
                    triples.add((nums[front],nums[mid],nums[back]))
                    mid += 1
                    back -= 1
            front+=1
            mid = front+1
            back = len(nums)-1
        return [list(s) for s in triples]

            
