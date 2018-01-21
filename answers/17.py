class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits)==0:
            return []
        letterDict={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],
                    '6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        result=[''] 
        for s in digits:
            i=len(result)-1
            while i>=0:
                t=result[i]
                del result[i]
                for mm in letterDict[s]:
                    result.append(t+mm)
                i-=1
        
        return result
            