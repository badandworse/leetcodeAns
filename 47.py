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
                                        
                
        