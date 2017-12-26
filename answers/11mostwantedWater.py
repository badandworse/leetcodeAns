'''
初版类似与暴力破解，但是有如下优化的地方
对于开头元素，都是从结尾元素开始忘前遍历，一旦高比起点高大，
那可以直接和目前最大面积比较，如果大就可以结束当前元素的比较，进如下一个
然后就是下一个元素的高如果没有前一个的大，即可不用比较，它的最大面积不会有上一个的大
因此可以成功通过online test
不过还有待优化
'''

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxA=0
        i=0
        nowMaxH=0
        while i<len(height):
            j=len(height)-1
            if i>0:
                if height[i]<=nowMaxH:
                    i+=1
                    continue
            nowMaxH=height[i] 
            
            while j>i:
                if height[j]>=nowMaxH:
                    nowA=nowMaxH*(j-i)
                    maxA=nowA if nowA>maxA else maxA
                    break
                else:
                    nowH=height[j]
                    nowA=nowH*(j-i)
                    maxA=nowA if nowA>maxA else maxA
                    j-=1
            i+=1
        return maxA