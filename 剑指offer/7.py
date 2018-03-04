#%%
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre:
            return
        
        pNode=TreeNode(pre[0])
        index=tin.index(pre[0])
        leftTree=tin[:index]
        rightTree=tin[index+1:]
        pNode.left=self.reConstructBinaryTree(pre[1:len(leftTree)+1],leftTree)
        pNode.right=self.reConstructBinaryTree(pre[len(leftTree)+1:],rightTree)
        return pNode


mm=Solution()
mm.reConstructBinaryTree([1,2,3,4,5,6,7],[3,2,4,1,6,5,7])