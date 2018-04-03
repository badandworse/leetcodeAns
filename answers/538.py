# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        results=[]
        self.preOrder(root,results)
        sum1=0
        for node in results:
            node.val+=sum1
            sum1=node.val
        return root
    def preOrder(self,root,results):
        if not root:
            return 
        self.preOrder(root.right,results)
        results.append(root)
        self.preOrder(root.left,results)