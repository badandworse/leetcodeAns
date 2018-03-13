#%%
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        path1=[]
        path2=[]
        start1=root
        self.findPath(root,p,path1)
        self.findPath(root,q,path2)
        node1=path1[-1]
        i=len(path1)-1
        j=len(path2)-1
        while i>0 and j>0:
            if path1[i-1]==path2[j-1]:
                node1=path1[i-1]
                i-=1
                j-=1
            else:
                return node1
        return node1
                
        
        
    
    def findPath(self,start,p,path):
        if not start:
            return False
        if start==p:
            path.append(start)
            return True
        if self.findPath(start.left,p,path) or self.findPath(start.right,p,path):
            path.append(start)
            return True
        else:
            return False


node1=TreeNode(1)
node1.right=TreeNode(2)
mm=Solution()
nodeC=mm.lowestCommonAncestor(node1,node1,node1.right)
nodeC.val