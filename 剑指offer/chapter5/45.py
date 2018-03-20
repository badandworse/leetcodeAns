#%%
class Solution:
    def PrintMinNumber(self, numbers):
        if not numbers:
            return ""
        key=cmp_to_key(lambda x,y:int(x+y)-int(y+x))
        res=sorted(map(str,numbers),key=key)
        return int(''.join(x for x in res))

