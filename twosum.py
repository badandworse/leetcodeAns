'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1==None:
            return l2
        if l2==None:
            return l1
        result=ListNode(0)
        flag=0
        tempNode=result
        while l1 and l2:
            tempNode.next=ListNode((l1.val+l2.val+flag)%10)
            flag=(l1.val+l2.val+flag)/10
            tempNode=tempNode.next
            l1=l1.next
            l2=l2.next
        return result.next       


10%10