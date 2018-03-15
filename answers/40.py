class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results=[]
        candidates.sort()
        self.dfs(candidates,0,target,[],results,len(candidates))
        return results
    
    def dfs(self,nums,index,target,path,results,end):
        if target==0:
            results.append(path)
            return 
        else:
            for i in range(index,end):
                if i>index and nums[i]==nums[i-1]:
                    continue
                if target<nums[i]:
                    continue
                self.dfs(nums,i+1,target-nums[i],path+[nums[i]],results,end)