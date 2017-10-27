'''
广度优先搜索
将起点加入队列
重复:
取队列中的下一个顶点v并标记它
将与v相邻的所有未被标记过的顶点加入队列
'''
#%%
import queue

class BreadthFirshPaths:
    def __init__(self,G):
        self.marked=[False]*G.getNodesCount()
        self.edgeTo=[-1]*G.getNodesCount()
        self.s=None
        self.q=None
    def bfs(self,G,s):
        '''
        s表示搜索起点
        isstart表示是否是外部第一次调用
       [k] '''
        self.s=s
        self.q=queue.Queue(G.getNodesCount())
        self.marked[s]=True
        self.q.put(s)
        while not self.q.empty():
            v = self.q.get()
            for i in G.getNodesEdgeList(v):
                if not self.marked[i]:
                    self.edgeTo[i]=v
                    self.marked[i]=True
                    self.q.put(i)
    
    def HasPathTo(self,v):
        return self.marked[v]
    
    def getPathsTo(self,v):
        if not self.HasPathTo(v):
            return null
        path=[]
        x=v
        while x!=self.s:
            path.append(x)
            x=self.edgeTo[x]
        path.append(self.s)
        return list(reversed(path))

#%%
#用到的graph类
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
filepath='c:/Users/xg302/git/leetcodeAns/data/edges.txt'
testGraph=graph(13,0)
testGraph.genGraph(filepath)
#%%
testSearchshortestPath=BreadthFirshPaths(testGraph)
testSearchshortestPath.bfs(testGraph,0)
testSearchshortestPath.getPathsTo(3)