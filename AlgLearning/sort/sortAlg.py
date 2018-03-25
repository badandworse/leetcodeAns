import numpy as np

#%%
def less(a,b):
    if a<b:
        return -1
    elif a==b:
        return 0
    else:
        return 1
def exchange(aList,i,j):
    temp=aList[i]
    aList[i]=aList[j]
    aList[j]=temp

# '''
# 选择排序
# '''
# class SelectSort(object):
#     def SelectF(self,aList):
#         length=len(aList)
#         for i in range(length):
#             for j in range(i+1,length):
#                 nowMin=i
#                 if less(aList[j],aList[nowMin])==-1:
#                     nowMin=j
#                 if nowMin!=i:
#                     exchange(aList,i,nowMin)
# #%%
# '''
# 插入排序
# '''
# class InsertSort(object):
#     def InsertF(self,a):
#         length=len(a)
#         for i in range(1,length):
#             for j in range(i):
#                 if less(a[i],a[j])<0:
#                     temp=a[i]
#                     for m in reversed(range(j+1,i+1)):
#                         a[m]=a[m-1]
#                     a[j]=temp


# #%%
# '''
# 希尔排序
# '''
# class ShellSort(object):
#     def shellF(self,a):
#         length=len(a)
#         h=1
#         while h<length/3:
#             h=3*h+1
#         while h>=1:
#             for i in range(h,length):
#                 for j in reversed(range(h,i+1,h)):
#                     if less(a[j],a[j-h])==-1:
#                         exchange(a,j,j-h)
#             h=int(h/3)
#             print(h)

#%%
'''
归并排序:将两个有序的数组合并成一个数组
递归的过程
因为python中的数组主要用list，而这一般不会事先确定大小
所以归并在复制的时候是不同的。
'''
class MergeSort(object):
    def MergeF(self,aList):
         length=len(aList)
         self.sortL(aList,0,length-1)
    
    def sortL(self,a,begin,end):
        if begin>=end:
            return
        mid=begin+int((end-begin)/2)
        self.sortL(a,begin,mid)
        self.sortL(a,mid+1,end)
        self.Merge(a,begin,mid,end)
    
    def Merge(self,a,begin,mid,end):
        b=[]
        lo=begin
        j=mid+1
        for i in range(end+1):
            b.append(a[i])
        
        for k in range(begin,end+1):
            if lo>mid:
                a[k]=b[j]
                j+=1
            elif j>end:
                a[k]=b[lo]
                lo+=1
            elif less(b[lo],b[j])==-1:
                a[k]=b[lo]
                lo+=1
            else:
                a[k]=b[j]
                j+=1


#%%
'''
快速排序
'''   
class QuickSort(object):
    def QuickS(self,aList):
        np.random.shuffle(aList)
        self.sortL(aList,0,len(aList)-1)

    def sortL(self,a,begin,end):
        if begin>=end:
            return
        j=self.partions(a,begin,end)
        self.sortL(a,begin,j-1)
        self.sortL(a,j+1,end)
    
    def partions(self,a,begin,end):
        mm=a[begin]
        i=begin+1
        j=end
        while True:
            while less(a[i],mm)==-1:
                i+=1
                if i==end:
                    break
            while less(mm,a[j])==-1:
                j-=1
            #跳出循环不仅是因为出现需要交换的i,j
            #也有可能是需要跳出循环，因此先检查是否需要跳出循环
            #然后再交换   446688

            if i>=j:
                break
            exchange(a,i,j)
        print(i,j)
        exchange(a,begin,j)            
        return j

#%%
'''
堆排序：
'''
                


#%%
np.random.seed(1)

aList=np.random.randint(100,size=20)
aList
# #%%
# selectS=SelectSort()
# selectS.SelectF(aList)
# aList

# #%%
# insertS=InsertSort()
# insertS.InsertF(aList)
# aList

#%%
# shellS=ShellSort()
# shellS.shellF(aList)
# aList

#%%
# mergeS=MergeSort()
# mergeS.MergeF(aList)

#%%
quikS=QuickSort()
quikS.QuickS(aList)
aList

'''
冒泡排序
'''
#%%
class BubbleSort:
    def Sort(self,a):
        length=len(a)
        for i in reversed(range(length)):
            for j in range(i):
                if a[j]>a[j+1]:
                    a[j],a[j+1]=a[j+1],a[j]

#%%
def insert_sort(lst):
    '''
    插入排序
    '''
    n=len(lst)
    if n==1: return lst
    for i in range(1,n):
        for j in range(i,0,-1):
            if lst[j]<lst[j-1]: 
                lst[j],lst[j-1]=lst[j-1],lst[j]
            else:break
    return lst

