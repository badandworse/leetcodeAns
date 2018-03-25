# -*- coding:utf-8 -*-
#%%
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            return 
        stack=[root]
        while True:
            a=[]
            n=0
            for node in stack:
                if node:
                    a.append(node.left)
                    a.append(node.right)
                    if node.right:
                        n+=1
                    if node.left:
                        n+=1
            if n==0:
                break
            temp=[node for node in reversed(a)]
            for i in range(len(stack)):
                node=stack[i]
                if node:
                    node.left=temp.pop()
                    node.right=temp.pop()
            stack=[l for l in reversed(a)]
        return root

#%%
node1=TreeNode(8)
node2=TreeNode(6)
node3=TreeNode(10)
node4=TreeNode(5)
node5=TreeNode(7)
node6=TreeNode(9)
node7=TreeNode(11)



#%%
node1.left=node2
node1.right=node3
node2.left=node4
node2.right=node5
node3.left=node6
node3.right=node7

m=Solution()
m.Mirror(node1)
