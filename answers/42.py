class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        left=0
        right=len(height)-1
        leftmax=0
        rightmax=0
        result=0
        while left<right:
            if height[left]<height[right]:
                if height[left]>=leftmax:
                    leftmax=height[left]
                else:
                    result+=leftmax-height[left]
                left+=1
            else:
                if height[right]>=rightmax:
                    rightmax=height[right]
                else:
                    result+=rightmax-height[right]
                right-=1
        return result