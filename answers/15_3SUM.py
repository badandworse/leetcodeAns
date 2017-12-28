# '''
# 超时了，想复杂了，
# 明天修改的时候。先sort，然后再想这从左至右
# 内层则是从两边往中间
# '''
# class Solution:
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         numDict={}
#         i=0
#         while i<len(nums):
#             if nums[i] not in numDict:
#                 numDict[nums[i]]=[i]
#             else:
#                 numDict[nums[i]].append(i)
#             i+=1
#         j=0
#         anwsers=[]
#         while j<len(nums)-2:
#             q=j+1
#             while q<len(nums)-1:
#                 theN=0-nums[q]-nums[j]
#                 if theN in numDict:
#                     lenS=0
#                     print([theN,nums[q],nums[j]])
#                     for n in set([theN,nums[q],nums[j]]):
#                         lenS+=len(numDict[n])
#                     if lenS>=3:
#                         newA=sorted([nums[j],nums[q],theN])
#                         if newA not in anwsers:
#                             anwsers.append(newA)
#                 q+=1
#             numDict[nums[j]].remove(j)
#             j+=1
#         return anwsers

#%%
'''
在最开始的时候，总是超时，因此尝试优化
开始判定和是否为0的时候，总是用运算式去判定
这就会导致重复运算，因此先将：
s=nums[i]+nums[j]+nums[k]
然后再s>0:
这样勉强被accepted

'''
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums=sorted(nums)
        i=0
        anwsers=[]
        while i<len(nums)-2:
            j=i+1
            k=len(nums)-1
            if i>0 and nums[i-1]==nums[i]:
                i+=1
                continue
            while k>j:
                if nums[i]+nums[j]+nums[k]==0:
                    anwsers.append([nums[i],nums[j],nums[k]])
                    while k>j and nums[j]==nums[j+1]:
                        j+=1
                    while k<j and nums[k]==nums[k-1]:
                        k-=1
                    j+=1
                    k-=1
                elif nums[i]+nums[j]+nums[k]>0:
                    k-=1
                else:
                    j+=1
            i+=1
        return anwsers
