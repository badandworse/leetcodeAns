# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        results=[]
        self.findResults(root,results)
        return results
    def findResults(self,root,results):
        if root.left:
            self.findResults(root.left,results)
        if root.right:
            self.findResults(root.right,results)
        results.append(root.val)


'''
非递归版本
'''
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        results=[]
        stack=[root]
        while len(stack)>0:
            node=stack.pop()
            if node:
                results.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return results[::-1]