#%%
'''
利用dict生成一个图，每个key对应一个node
'''
class graph(object):
    def __init__(self,V,e=0):
        '''
        初始化，必须给定点的个数
        可以不给定边数
        同时初始化对应字典
        '''
        self.V=V
        self.E=e
        self.edgeDict=dict()
    
    def genGraph(self,filePath):
        with open(filepath) as f:
            lines=f.read().splitlines()
            for line in lines:
                nodeList=line.split(' ')
                self.addEdge(nodeList)
    
    def getNodesCount(self):
        return self.V
    
    def getEdgesCount(self):
        return self.E
    
    def addEdge(self,nodeList):
        nodeList[0]=int(nodeList[0])
        nodeList[1]=int(nodeList[1])
        if nodeList[0] in self.edgeDict:
            self.edgeDict[nodeList[0]].append(nodeList[1])
        else:
            self.edgeDict[nodeList[0]]=[nodeList[1]]
        if nodeList[1] in self.edgeDict:
            self.edgeDict[nodeList[1]].append(nodeList[0])
        else:
            self.edgeDict[nodeList[1]]=[nodeList[0]]
        self.E+=1

    def getNodesEdgeList(self,v):
        return self.edgeDict[v]

#%%
'''
深度搜索的思想是，每搜索一个点，就将这个点标记为已访问
同时递归的访问这个点的邻居
'''
class DepthFirstSearch(object):
    '''
    深度优先搜索
    '''
    def __init__(self,G):
        self.marked=[False]*G.getNodesCount()
        self.count=0



    def dfs(self,G,v,isStart=False):
        '''
        v表示查找的起点,传入整数
        isStart 为true表示非递归时调用，而是第一次调用
        '''
        if isStart:
            self.count=0
        self.marked[v]=True
        self.count+=1
        for i in G.getNodesEdgeList((str)v):
            if not self.marked[int(i)]:
                self.dfs(G,i)

    def getMarked(self):
        return self.marked

    def getCount(self):
        return self.count


#%%
'''
利用深度优先搜索寻找两点之间是否存在路径
'''
class DepthFirstPaths(object):
    def __init__(self,G):
        self.marked=[False]*G.getNodesCount()
        self.edgeTo=[-1]*G.getNodesCount()
        self.s=None

    def dfs(self,G,v,isStart=False):
        '''
        v表示查找的起点,传入整数
        isStart 为true表示非递归时调用，而是第一次调用
        
        '''
        if isStart:
            self.s=v
            self.edgeTo[v]=v
        self.marked[v]=True
        for i in G.getNodesEdgeList(str(v)):
            if not self.marked[int(i)]:
                '''
                这标明到必须通过v到达i
                '''
                self.edgeTo[int(i)]=v
                self.dfs(G,int(i))
    
    def hasPathTo(self,v):
        return self.marked[v]

    def getPathsTo(self,v):
        if not self.hasPathTo(v):
            return null
        path=[]
        x=v
        
        while x!=self.s:
            path.append(x)
            x=self.edgeTo[x]
        path.append(self.s)
        return path

                
#%%
filepath='c:/Users/xg302/git/leetcodeAns/data/edges.txt'
testGraph=graph(13,0)
testGraph.genGraph(filepath)
#%%
#测试深度搜索
mm=DepthFirstSearch(testGraph)
mm.getCount()
mm.getMarked()
mm.dfs(testGraph,'0',True)

#测试利用深度搜索找到指点两点之间的路径
testSearchPath=DepthFirstPaths(testGraph)
testSearchPath.dfs(testGraph,0,True)
testSearchPath.hasPathTo(3)
path=testSearchPath.getPathsTo(3)
testSearchPath.edgeTo

#%%
print(filepath)
testdict=dict()
testKey=1
if testKey in testdict:
    testdict[testKey].append(1)
else:
    testdict[testKey]=[]
    
testdict[testKey].append(2)


'''
深度优先搜索应用一：
判断图是否存在环
'''
#%%
class DFScheckhasCircle(object):
    def __init__(self,g):
        self.g=g
        self.hasCircle=False
        self.marked=[False]*g.getNodesCount()

    def checkhasCircle(self):
        for i in range(self.g.getNodesCount()):
            if not self.marked[i]:
                self.dfs(self.g,i,i)
                if self.hasCircle:
                    return True
        return True

    def dfs(self,g,v,u):
        '''
        这里v和u是相同的，即出发点
        用于备份递归的开始,这样只要遇到一个点事先被标记过，
        但如果不是起点被标记，则可以确定是存在环的
        '''
        self.marked[v]=True
        for i in self.g.getNodesEdgeList(v):
            if not self.marked[i]:
                self.dfs(self.g,i,v)
            elif i!=u:
                self.hasCircle=True
                return




testCheckCircle=DFScheckhasCircle(testGraph)
testCheckCircle.checkhasCircle()


'''
dfs的应用之二:
判断是否为二分图:
即存在两组点集合，互补与自己组内的点相连
'''
#%%
class TwoColor(object):
    def __init__(self,g):
        self.g=g
        self.isTwoColor=True
        self.ismarked=[False]*g.getNodesCount()
        self.colors=[False]*g.getNodesCount()

    def dfs(self,g,v):
        self.ismarked[v]=True
        for i in g.getNodesEdgeList(v):
            if not self.marked[i]:
                colors[i]=colors[v]
                self.dfs(g,i)
            elif colors[i]==colors[v]:
                self.isTwoColor=False
                return

    def TwoColor(self):
        for i in range(self.g.getNodesCount()):
            if not self.marked[i]:
                self.dfs(self.g,i)
                if not self.isTwoColor:
                    return self.isTwoColor

        return self.isTwoColor     
