#%%
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if not array:
            return False
        height=len(array)
        width=len(array[0])
        for i in range(height):
            begin=0
            end=width-1
            mid=int((end-begin)/2)+begin
            while mid>=begin and mid<=end:
                if array[i][mid]==target:
                    return True
                elif array[i][mid]>target:
                    end=mid-1
                else:
                    begin=mid+1
                mid=int((end-begin)/2)+begin
        return False

'''
更好的答案，target每次和矩阵的右上角元素比较，如果大于，则去掉该行，
如果小于则去掉该列
'''
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if not array:
            return False
        i=0
        j=len(array[0])-1
        while i<len(array) and j>=0:
            if target==array[i][j]:
                return True
            elif target>array[i][j]:
                i+=1
            else:
                j-=1
        return False


mm=Solution()
mm.Find(15,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]])