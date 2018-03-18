# -*- coding:utf-8 -*-
#%%
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None
        oldStart=pHead
        nodeDict={}
        while pHead:
            newNode=RandomListNode(pHead.label)
            nodeDict[pHead]=newNode
            newNode.next=pHead.next
            pHead=pHead.next
            newNode=newNode.next
        newStart=nodeDict[oldStart]
        while oldStart:
            nodeDict[oldStart].random=oldStart.random
            oldStart=oldStart.next
        return newStart

nodeList=[]
for i in range(5):
    node=RandomListNode(i)
    nodeList.append(node)

for i in range(4):
    nodeList[i].next=nodeList[i+1]

nodeList[0].random=nodeList[3]
nodeList[1].random=nodeList[4]
nodeList[2].random=nodeList[1]

mm=Solution()
newStart=mm.Clone(nodeList[0])
newStart.random.label


