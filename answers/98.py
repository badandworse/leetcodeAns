# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        inOrderLists=[]
        stacks=[]
        while root or len(stacks)>0:
            while root:
                stacks.append(root)
                root=root.left
            root=stacks.pop()
            inOrderLists.append(root.val)
            root=root.right
        for i in range(len(inOrderLists)-1):
            if inOrderLists[i]>=inOrderLists[i+1]:
                return False
        return True