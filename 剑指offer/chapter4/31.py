# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        mList=[]
        while pushV:
            i=pushV[0]
            del pushV[0]
            if i==popV[0]:
                del popV[0]
            else:
                mList.append(i)
        
        while mList and popV:
            if mList.pop()==popV[0]:
                del popV[0]
            else:
                return False
        if not mList and not popV:
            return True
        else:
            return False

mm=Solution()
mm.IsPopOrder([1,2,3,4,5],[3,5,4,2,1])