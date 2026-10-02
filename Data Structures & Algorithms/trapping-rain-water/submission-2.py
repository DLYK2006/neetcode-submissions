class Solution:
    def trap(self, height: List[int]) -> int:
        water=0
        stack=[]
        for i in range(len(height)):
            while stack and height[i]>=height[stack[-1]]:
                bottom=height[stack.pop()]
                if stack:
                    right=height[i]
                    left=height[stack[-1]]
                    length=min(left,right)-bottom
                    width=i-stack[-1]-1
                    water+=length*width
            stack.append(i)
        return water