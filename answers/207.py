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
            isVisited=[False]*numCourses
            if self.checkisExit(i,i,edgeDict,isVisited):
                return False
        return True
        
    def addEdge(self,a,b,edgeDict):
        if a in edgeDict:
            edgeDict[a].append(b)
        else:
            edgeDict[a]=[b]
    
    
    def checkisExit(self,a,b,edgeDict,isVisited):
        if isVisited[a]==True:
            return False
        isVisited[a]=True
        if a not in edgeDict:
            return False
        if b in edgeDict[a]:
            return True
        for m in edgeDict[a]:
            if self.checkisExit(m,b,edgeDict,isVisited)==True:
                return True
        return False         
        