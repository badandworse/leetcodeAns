# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return 
        pA=headA
        pB=headB
        lenA=0
        lenB=0
        while pA is not pB:
            if pA.next:
                pA=pA.next
            else:
                pA=headB
                lenA+=1
                if lenA>1:
                    return
            if pB.next:
                pB=pB.next
            else:
                pB=headA
                lenB+=1
                if lenB>1:
                    return 
        return pA
            