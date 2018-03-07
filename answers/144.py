# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        results=[]
        stacks=[root]
        while len(stacks)>0:
            node=stacks.pop()
            if node:
                results.append(node.val)
                stacks.append(node.right)
                stacks.append(node.left)
        return results