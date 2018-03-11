# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead:
            return
        if pHead.next and pHead.next.next:
            fast=pHead.next.next
            slow=pHead.next
        else:
            return 
        while fast!=slow :
            if fast.next and fast.next.next:
                fast=fast.next.next
                slow=slow.next
            else:
                return 
        while slow!=pHead:
            slow=slow.next
            pHead=pHead.next
        return pHead
         