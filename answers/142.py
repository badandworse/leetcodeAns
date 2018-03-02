# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
solution 1:用额外的空间
'''
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        mDict={}
        while head:
            if head not in mDict:
                mDict[head]=True
                head=head.next
            else:
                return head
        return None


'''
solution2:不使用额外的空间，用两个指针
'''
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow=fast=head
        try:
            fast=fast.next.next
            slow=slow.next
            while fast is not slow:
                fast=fast.next.next
                slow=slow.next
        except:
            return None
        while head is not slow:
            head=head.next
            slow=slow.next
        return head