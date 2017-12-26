'''
给定一个list与target，然后寻找两个元素和等于target，
一个元素只允许使用一次
'''
#暴力破解:
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        while len(nums)>0:
            num1=nums.pop()
            try:     
                return [len(nums),nums.index(target-num1)]
            except ValueError :
                continue
    


#用dict来降低时间复杂度:
class Solution:
    '''
    将list的各个值存到字典中，key为value，value为index
    用空间来换时间
    '''
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsDict={}
        while len(nums)>0:
            num1=nums.pop()
            if num1 in numsDict:
                numsDict[num1].append(len(nums))
            else:
                numsDict[num1]=[len(nums)]
        
        for keys,value in numsDict.items():
            try:
                return [value.pop(),numsDict[target-keys].pop()]
            except KeyError or IndexError:
                continue



#另一种思路:
#字典不存自己的index，而是存目标值的索引
#这样遍历的是如果target-num存在字典中，则证明解存在的
#这是更快的