'''
better answers
'''
class Solution:
    def permuteUnique(self, nums):
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
            for i in range(len(results[0])+1):
                results.append(results[0][:i]+[x]+results[0][i:])
                if i<len(results[0]) and results[0][i]==x:
                    break
            del results[0]

class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results=[[]]
        for x in nums:
            self.genRe(x,results)
        nowResults=[]
        for m in results:
            if m not in nowResults:
                nowResults.append(m)
        return nowResults
    
    def genRe(self,x,results):
        length=len(results)
        for q in range(length):
            mlen=len(results[0])
            i=0
            isRepeat=False
            while i<mlen:
                if results[0][i]==x:
                    if isRepeat:
                        i+=1
                    else:
                        results.append(results[0][:i]+[x]+results[0][i:])
                        i+=2
                        isRepeat=True
                else:
                    results.append(results[0][:i]+[x]+results[0][i:])
                    isRepeat=False
                    i+=1
            if isRepeat==False:
                results.append(results[0]+[x])
            
            del results[0]            
                                        
                
        