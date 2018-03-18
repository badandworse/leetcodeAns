# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return pRootOfTree
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        self.Convert(pRootOfTree.left)
        left=pRootOfTree.left
        if left:
            while left.right:
                left=left.right
            pRootOfTree.left,left.right=left,pRootOfTree
        self.Convert(pRootOfTree.right)
        right=pRootOfTree.right
        if right:
            while right.left:
                right=right.left
            pRootOfTree.right,right.left=right,pRootOfTree
        
        while pRootOfTree.left:
            pRootOfTree=pRootOfTree.left
        return pRootOfTree