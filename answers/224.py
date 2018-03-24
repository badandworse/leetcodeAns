import math
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        rows=len(matrix)
        cols=len(matrix[0])
        heights=[0 for i in range(cols)]
        maxA=0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]=='1':
                    heights[j]+=1
                else:
                    heights[j]=0
            maxA=max(self.findMaxA(heights,cols),maxA)
            
        return int(math.sqrt(maxA))*int(math.sqrt(maxA))
    
    def findMaxA(self,heights,cols):
        stack=[]
        maxA=0
        for i in range(cols):
            while stack and heights[stack[-1]]>=heights[i]:
                if heights[stack[-1]]==0:
                    stack=[]
                    break
                else:
                    index=stack.pop()
                    curA=math.pow(min(heights[index],i),2) if not stack else math.pow(min(i-stack[-1]-1,heights[index]),2)
                    maxA=max(curA,maxA)
            stack.append(i)
        while stack:
            if heights[stack[-1]]==0:
                return maxA
            else:
                index=stack.pop()
                curA=curA=math.pow(min(heights[index],cols),2) if not stack else math.pow(min(cols-stack[-1]-1,heights[index]),2)
                maxA=max(curA,maxA)
        return maxA
        