# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        results=[]
        aList=[root]
        while aList:
            b=[]
            c=[]
            for node in aList:
                if node:
                    c.append(node.val)
                    b.append(node.left)
                    b.append(node.right)
            if len(c)>0:
                results.append(c)
            aList=b
        return results