class Solution:
    def maxArea(self, heights: List[int]) -> int:
        j=len(heights)-1
        i=0
        biggest=0
        while j>i:
            height=(j-i)*min(heights[i],heights[j])
            biggest=max(biggest,height)
            if(heights[i]>heights[j]):
                j-=1
            else:
                i+=1
            if(biggest<height):
                biggest=height
        return biggest