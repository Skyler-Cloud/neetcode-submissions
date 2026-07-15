class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        hl,hr=0,0
        area = 0
        while l<r:
            if heights[l]>hl or heights[r]>hr:
                hl=max(hl,heights[l])
                hr=max(hr,heights[r])
                area = max(area, min(hl,hr)*(r-l))
            if heights[l]<heights[r]:
                l+=1
            elif heights[l]>heights[r]:
                r-=1
            else:
                l+=1
                r-=1
        return area

        
        