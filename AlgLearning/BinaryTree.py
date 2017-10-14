#%%
#实现一个二叉树
class Node(object):
    def __init__(self,data):
        '''
        节点结构
        '''
        self.left=None
        self.right=None
        self.data=data

    def insert(self,data):
        '''
        插入节点数据
        '''
        if data<self.data:
            if self.left is None:
                self.left=Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right=Node(data)
            else:
                self.right.insert(data)
    
    def lookup(self,data,parent=None):
        '''
        查找数据
        '''
        if data <self.data:
            if self.left is None:
                return None,None
            return self.left.lookup(data,self)
        elif data>self.data:
            if self.right is None:
                return None,None
            return self.right.lookup(data,self)
        else:
            return self,parent
    def Preorder(self,s):
        '''
        前序遍历
        '''
        if self.data:
            s.append(self.data)
        if self.left:
            self.left.Preorder(s)
        if self.right:
            self.right.Preorder(s)

    def midOrder(self,s):
        '''
        中序遍历
        '''
        if self.left:
            self.left.midOrder(s)
        if self.data:
            s.append(self.data)
        if self.right:
            self.right.midOrder(s)
    
    def lastOrder(self,s):
        '''
        后序遍历
        '''
        if self.left:
            self.left.lastOrder(s)
        if self.right:
            self.right.lastOrder(s)
        if self.data:
            s.append(self.data)

    def findMin(self):
        if self.left:
            return self.left.findMin()
        else:
            return self
    def findMax(self):
        if self.right:
            return self.right.findMax()
        else:
            return self

    def delete(self,data):
        '''
        删除节点
        如果没有子节点，直接删除
        如果有一个子节点，将下一个子节点转移到当前节点
        如果有两个子节点，要对子节点的数据进行判断，并从新安排节点排序
        '''
        node,parent=self.lookup(data)
        if parent is None:
            n=node.right.findMin()
            node.delete(n.data)
            node.data=n.data
        if node is not None:
            child_cnt=node.children_count()
            if child_cnt==0:
                if parent.left is node:
                    parent.left=None
                else:
                    parent.right=None
            elif child_cnt==1:
                if node.left:
                    n=node.left
                else:
                    n=node.right
                if parent:
                    if parent.left is node:
                        parent.left=n
                    else:
                        parent.right=n
            else:
                #如果节点有两个儿子，则将其右子树的
                #最小数据代替此节点的数据，
                #并将其右子树的最小数据(不可能有左儿子)删除。
                n=node.right.findMin()
                node.delete(n.data)
                if parent.left is node:
                    parent.left.data=n.data
                else:
                    parent.right.data=n.data
                    
    
    def children_count(self):
        '''
        子节点个数
        '''
        cnt=0
        if self.left:
            cnt+=1
        if self.right:
            cnt+=1
        return cnt

#%%
m=Node(1)
ll=[5,2,3,4]
while ll:
    m.insert(ll.pop())
m.delete(1)
#%%
s=[]
m.Preorder(s)
print(s)

