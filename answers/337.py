# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        sum1=root.val
        sum2=self.rob(root.left)+self.rob(root.right)
        if  root.left:
            sum1+=self.rob(root.left.left)+self.rob(root.left.right)
        if  root.right:
            sum1+=self.rob(root.right.left)+self.rob(root.right.right)
            
        return max(sum1,sum2)