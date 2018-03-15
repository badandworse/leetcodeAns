#%%
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results=[[]]
        for x in nums:
            self.genRe(x,results)
            
        return results
    
    def genRe(self,x,results):
        length=len(results)
        for q in range(length):
            mlen=len(results[0])
            for i in range(mlen+1):
                results.append(results[0][:i]+[x]+results[0][i:])
            del results[0]

class Solution1:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results=[[]]
        for num in nums:
            self.genRe(results,num)
        return results
    
    def genRe(self,results,num):
        length=len(results)
        for i in range(length):
            mList=results[i]
            for j in range(len(mList)+1):
                results.append(mList[:j]+[num]+mList[j+1:])
        del results[:length]


mm=Solution1()
mm.permute([1,2,3])