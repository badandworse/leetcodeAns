class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        height=len(matrix[0])
        heights=[0 for x in range(height)]
        maxA=0
        for m in range(len(matrix)):
            for n in range(height):
                if matrix[m][n]=='1':
                    heights[n]+=1
                else:
                    heights[n]=0
            maxA=max(maxA,self.getCurrentMaxA(heights))
        return maxA
    
    def getCurrentMaxA(self,heights):
        if sum(heights)==0:
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