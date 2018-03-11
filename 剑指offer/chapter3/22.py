# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head or k==0:
            return 
        i=0
        start=head
        while i<k and head:
            i+=1
            head=head.next
        if i<k:
            return
        while head:
            head=head.next
            start=start.next
        return start
        