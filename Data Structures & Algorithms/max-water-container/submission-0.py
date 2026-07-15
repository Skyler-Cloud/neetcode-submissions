class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start,end = 0, len(heights)-1
        out = 0
        while start < end:
            area = (end-start)*(min(heights[start],heights[end]))
            print(f'{(start,end)=}, heights: {(heights[start],heights[end])}, {area=}')
            out = max(out, area)

            start_height,end_height = heights[start],heights[end]
            if start_height<=end_height:
                while start<end and start_height>=heights[start]:
                    start += 1
            if start_height>=end_height:
                while start<end and end_height>=heights[end]:
                    end -= 1
        return out