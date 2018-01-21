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
        if not head.next:
            if n==1:
                return head.next
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
        if i-n+2 in nodeDict:
            nodeDict[i-n].next=nodeDict[i-n+2]
        else:
            nodeDict[i-n].next=None
        return nodeDict[0]

#%%
head=ListNode(1)
head.next=ListNode(2)
mm=Solution()
mm.removeNthFromEnd(head,1)