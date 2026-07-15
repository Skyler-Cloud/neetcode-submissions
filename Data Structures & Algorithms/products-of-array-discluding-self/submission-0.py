class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod=[]
        right_prod=[]
        curr = 1
        for x in nums: # [1,a,ab,abc] for [a,b,c,d]
            left_prod.append(curr)
            curr *= x

        curr=1
        for x in nums[::-1]:
            right_prod.append(curr)
            curr *=x
        return [x*y for x,y in zip(left_prod,right_prod[::-1])]
