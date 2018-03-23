class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        maxL=0
        start=0
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            else:
                if len(stack)==0:
                    start=i+1
                else:
                    stack.pop()
                    if len(stack)==0:
                        maxL=maxL if i-start+1<maxL else i-start+1
                    else:
                        maxL=maxL if i-stack[-1]<maxL else i-stack[-1]
        
        return maxL