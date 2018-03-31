class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses==0 or not prerequisites:
            return True
        edgeDict={}
        
        for edge in prerequisites:
            self.addEdge(edge[0],edge[1],edgeDict)
        
        for i in edgeDict.keys():
            if self.checkisExit(i,i,edgeDict):
                return False
        return True
        
    def addEdge(self,a,b,edgeDict):
        if a in edgeDict:
            edgeDict[a].append(b)
        else:
            edgeDict[a]=[b]
    
    
    def checkisExit(self,a,b,edgeDict):
        if a not in edgeDict:
            return False
        if b in edgeDict[a]:
            return True
        for m in edgeDict[a]:
            if self.checkisExit(m,b,edgeDict)==True:
                return True
        return False

mm=Solution()
mm.canFinish(4,[[0,1],[3,1],[1,3],[3,2]])