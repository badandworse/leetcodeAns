# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        results=[]
        nodeList=[root]
        i=0
        while nodeList:
            aa=[]
            bb=[]
            for node in nodeList:
                aa.append(node.val)
                if node.right:
                    bb.append(node.right)
                if node.left:
                    bb.append(node.left)
            if i%2==0:
                aa=aa[::-1]
            i+=1 
            results.append(aa)
            nodeList=bb
        return results