class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        area=0
        popped=0
        width=0
        heights.append(0)

        for i in range(len(heights)):
        
            while stack and heights[stack[-1]]> heights[i]:
                popped=stack.pop()
                if len(stack)==0:
                    width=i
                else:
                    width=i-stack[-1]-1

                area=max(area,heights[popped]*width)
            stack.append(i)

        return area

