class Solution:
    def threeSum(self, nums):
        dic={}
        for num in nums:
            if num in dic:
                dic[num]+=1
            else:
                dic[num]=1
        if 0 in dic and dic[0]>=3:
            ans=[[0,0,0]]
        else:
            ans=[]
        ns = sorted([x for x in dic if x<0], reverse=True)
        nns = sorted([x for x in dic if x>=0])
        for n in ns:
            for nn in nns:
                chk = -(nn + n)
                if chk in dic:
                    if chk in [n,nn] and dic[chk] > 1:
                        ans.append([n, chk, nn])
                    elif chk<n: 
                        ans.append([chk, n, nn])
                    elif nn<chk:
                        ans.append([n,nn,chk])
        return ans


mm=Solution()
mm.threeSum([-1,0,1,2,-1,-4])