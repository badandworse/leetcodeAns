# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        self.CloneNodes(pHead)
        self.ConnectSiblingNodes(pHead)
        return self.ReconnectNodes(pHead)
    def CloneNodes(self, pHead):
        pNode = pHead
        while pNode is not None:
            pCloned = RandomListNode(0)
            pCloned.label = pNode.label
            pCloned.next = pNode.next
            pCloned.random = None

            pNode.next = pCloned
            pNode = pCloned.next

    def ConnectSiblingNodes(self, pHead):
        pNode = pHead
        while pNode is not None:
            pCloned = pNode.next
            if pNode.random is not None:
                pCloned.random = pNode.random.next
            pNode = pCloned.next

    def ReconnectNodes(self, pHead):
        pNode = pHead
        pCloneHead = None
        if pNode is not None:
            pCloneHead = pCloneNode = pNode.next
            pNode.next = pCloneNode.next
            pNode = pNode.next
        while pNode is not None:
            pCloneNode.next = pNode.next
            pCloneNode = pCloneNode.next
            pNode.next = pCloneNode.next
            pNode = pNode.next
        return pCloneHead