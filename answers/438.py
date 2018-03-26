#%%
class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if not s or not p or len(s)<len(p):
            return []
        setDict={}
        for m in p:
            setDict[m]=setDict.get(m,0)+1
        length1=len(p)
        length2=len(s)
        i=0
        results=[]
        tempDict={}
        while i<=length2-length1:
            
            i,tempDict=self.getTest(i,i+length1,s,p,results,setDict,tempDict)
        return results
        
    def getTest(self,start,end,s,p,results,setDict,tempDict):
        if not tempDict:        
            for i in range(start,end):
                if s[i] not in setDict:
                    return i+1,{}
                else:
                    if s[i] not in tempDict:
                        tempDict[s[i]]=[i]
                    else:
                        tempDict[s[i]].append(i)
                    if len(tempDict[s[i]])>setDict[s[i]]:
                        mm=tempDict[s[i]][0]+1
                        return mm,{}
            results.append(start)
            del tempDict[s[start]][0]
            return start+1,tempDict
        else:
            if s[start-1]==s[end-1]:
                tempDict[s[start-1]].append(end-1)
                results.append(start)
                del tempDict[s[start]][0]
                return start+1,tempDict
            elif s[end-1] not in setDict:
                return end,{}
            else:
                mm=tempDict[s[end-1]][0]+1
                return mm,{}


'''
better anwser
'''
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        n, m = len(s), len(p)
        if n < m: return res
        phash, shash = [0]*123, [0]*123
        for x in p:
            phash[ord(x)] += 1
        for x in s[:m-1]:
            shash[ord(x)] += 1
        for i in range(m-1, n):
            shash[ord(s[i])] += 1
            if i-m >= 0:
                shash[ord(s[i-m])] -= 1
            if shash == phash:
                res.append(i - m + 1)
        return res

        