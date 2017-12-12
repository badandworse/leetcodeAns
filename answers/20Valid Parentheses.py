class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        listP=[set(['(',')']),set(['[',']']),set(['{','}'])]
        leftP=['(','[','{']
        rightP=[')',']','}']
        allP=[]
        for m in s:
            if m in rightP:
                if len(allP)==0:
                    return False
                elif set([m,allP[len(allP)-1]]) not in listP:
                    return False
                else:
                    allP.pop()
            elif m in leftP:
                allP.append(m)
        
        return True if len(allP)==0 else False