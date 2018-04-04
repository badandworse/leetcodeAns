# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.Diameter=1
        self.depth(root)
        return self.Diameter-1
    
    def depth(self,node):
        if not node:
            return 0
        L=self.depth(node.left)
        R=self.depth(node.right)
        self.Diameter=max(self.Diameter,L+R+1)
        return max(L,R)+1
    