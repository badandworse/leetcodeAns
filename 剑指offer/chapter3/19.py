#%%
# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if not pattern:
            return not s
        first_match=bool(s) and pattern[0] in {s[0],'.'}
        if len(pattern)>=2 and pattern[1]=="*":
            return self.match(s,pattern[2:]) or first_match and self.match(s[1:],pattern)
        else:
            return first_match and self.match(s[1:],pattern[1:])


mm=Solution()
mm.match('a','.*')

