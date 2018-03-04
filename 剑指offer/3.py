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


mm=Solution()
mm.Find(15,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]])