class Solution:
    def combinationSum(secandidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results=[]
        path=[]
        self.dfs(candidates,target,0,path,results)
        return results

    def dfs(self,nums,target,index,path,result):
        if target<0:
            return 
        if target==0:
            result.append(path)
            return 
        for i in range(index,len(nums)):
            if nums[i] >target:
                continue
            self.dfs(nums,target-nums[i],i,path+[nums[i]],result)
            
    
    