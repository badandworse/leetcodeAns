#%%
def getNext(t):
    next_T=[]
    #-1表示需要重新开始匹配，即在查找串中i+1
    next_T.append(-1)
    i=0
    j=-1
    while(i<len(t)-1):
        #只要i不等于0，那重新匹配最差都是从i=0的位置开始匹配
        #t[i]表示后缀的单个字符
        #t[j]表示前缀的单个字符
        if j==-1 or t[i]==t[j]:
            i+=1
            j+=1
            next_T.append(j)
        else:
            #若字符不同，则j值回溯
            #因为随着移动，p[i-j]到p[i-1]与p[0]到p[j-1]是相等的
            #因此需要去寻找新的前缀与当前后缀相比，因此在p[0]-p[j]中寻找后缀
            #因此要用到j=next_T[j]
            #递归查找
            j=next_T[j]
    return next_T

#KMP优化:针对next数据的优化，对于字符串'aaaab'型的数组:
#逐步回溯显得没有价值，因为a[0]=a[1]=a[2]=a[3]=a[4]
def getbetterNext(t):
    next_T=[]
    #-1表示需要重新开始匹配，即在查找串中i+1
    next_T.append(-1)
    i=0
    j=-1
    while(i<len(t)-1):
        #只要i不等于0，那重新匹配最差都是从i=0的位置开始匹配
        #t[i]表示后缀的单个字符
        #t[j]表示前缀的单个字符
        if j==-1 or t[i]==t[j]:
            i+=1
            j+=1
            if t[i]!=t[j]:
                next_T.append(j)
            else:
                #因为两个元素相等，故就算在i出回溯到j
                #还会再次回溯，因为不可能匹配，故在此之前
                #先直接得出应回溯的地址
                next_T.append(next_T[j])
        else:
            #若字符不同，则j值回溯
            #因为随着移动，p[i-j]到p[i-1]与p[0]到p[j-1]是相等的
            #因此需要去寻找新的前缀与当前后缀相比，因此在p[0]-p[j]中寻找后缀
            #因此要用到j=next_T[j]
            #递归查找
            j=next_T[j]
    return next_T


def KMPSerach(s,t):
    i=0
    k=0
    next_T=getNext(t)
    #i必须大于len(s)-len(t) 如果不大于，显然不会再有匹配的了
    while i<len(s)-len(t)+1:
        if s[i]==t[k]:
            if k==len(t)-1:
                return i-k+1
            else:
                k+=1
                i+=1
        else:
            if next_T[k]==-1:
                i+=1
                k=0
            else:
                k=next_T[k]
            if len(s)-i<len(t)-k:
                return -1            



#%%       
testS='acaa+aaca'
testT='aaaaax'


getNext(testS)