class TreeNode:
    def __init__(self,x,index):
        self.val=x
        self.left=None
        self.right=None
        self.index=index
        self.count=0
        self.leftsize=0
class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        length=len(nums)
        root=TreeNode(nums[-1],length-1)
        results=[0 for x in range(length)]
        for i in range(length-2,-1,-1):
            results[i]=self.insertNode(root,TreeNode(nums[i],i))
        return results
    
    def insertNode(self,root,node):
        
        if node.val>root.val:
            node.count+=root.leftsize+1
            if not root.right:
                root.right=node
            else:
                self.insertNode(root.right,node)
        else:
            root.leftsize+=1                
            if not root.left:
                root.left=node
            else:
                self.insertNode(root.left,node)
        return node.count
            
    def addRightCount(self,node):
        if not node:
            return
        node.count+=1
        self.addRightCount(node.left)
        self.addRightCount(node.right)
        