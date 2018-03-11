# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1 and not pHead2:
            return None
        if not pHead1:
            return pHead2
        elif not pHead2:
            return pHead1
        results=ListNode(0)
        temp=results
        while pHead1 and pHead2:
            if pHead1.val>pHead2.val:
                temp.next=pHead2
                pHead2=pHead2.next
            else:
                temp.next=pHead1
                pHead1=pHead1.next
            temp=temp.next
        if pHead1:
            while pHead1:
                temp.next=pHead1
                temp=temp.next
                pHead1=pHead1.next
        if pHead2:
            while pHead2:
                temp.next=pHead2
                temp=temp.next
                pHead2=pHead2.next
        return results.next