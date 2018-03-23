class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        maxA=0
        stack=[]
        for i in range(len(heights)):
            while stack and heights[i]<=heights[stack[-1]]:
                index=stack.pop()
                curArea=i*heights[index] if not stack else (i-stack[-1]-1)*heights[index]
                maxA=max(curArea,maxA)
            stack.append(i)
        while stack:
            index=stack.pop()
            curArea=len(heights)*heights[index] if not stack else (len(heights)-stack[-1]-1)*heights[index]
            maxA=max(curArea,maxA)
        
        return maxA
            