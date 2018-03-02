# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
答案一，用额外空间
'''
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        mList={}
        while head:
            if head not in mList:
                mList[head]=True
                head=head.next
            else:
                return True
        return False            

'''
答案2:不用额外空间
'''
class Solution2(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                return True
        return False