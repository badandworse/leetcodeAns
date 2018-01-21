#%%
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        nodeDict={}
        i=0
        temp=head
        while temp:
            i+=1
            nodeDict[i]=temp
            temp=temp.next
        '''
        有1~i个节点，倒着数第n个，则编号是i-n+1
        '''
        if i-n not in nodeDict and i-n+2 not in nodeDict:
            return None
        if i-n+2 in nodeDict:
            nodeDict[i-n].next=nodeDict[i-n+2]
        else:
            nodeDict[i-n].next=None
        return nodeDict[1]

    def betterRemoveNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        first=head
        second=head
        for i in range(n):
            first=first.next
        if first is None:
            return head.next
        else:
            first=first.next
        while first:
            first=first.next
            second=second.next
        second.next=second.next.next
        return head
