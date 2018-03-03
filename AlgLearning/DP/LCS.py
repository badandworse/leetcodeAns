#%%
'''
最长公共子序列:
L(i,j)=L(i-1,j-1)+1 if l1(i)=l2(j)
L(i,j)=max(L(i,j-1),L(i-1,j))
'''
def getLCS(list1,list2):
    m=len(list1)
    n=len(list2)

    c=[[0 for k in range(n+1)] for k in range(m+1)]  
    bList=[[-1 for k in range(n)] for k in range(m)]

    for i in range(1,m+1):
        for j in range(1,n+1):
            if list1[i-1]==list2[j-1]:
                c[i][j]=c[i-1][j-1]+1
                bList[i-1][j-1]='b'
            elif c[i][j-1]>c[i-1][j]:
                c[i][j]=c[i][j-1]
                bList[i-1][j-1]='j'
            elif c[i][j-1]==c[i-1][j]:
                c[i][j]=c[i][j-1]
                bList[i-1][j-1]='t'
            else:
                c[i][j]=c[i-1][j]
                bList[i-1][j-1]='i'
    print('the lcs length of %s and %s is %d' %(list1,list2,c[m][n]))

    results=[]
    paths=[]
    addLcs(bList,list1,m-1,list2,n-1,results,paths)
    return results

def addLcs(bList,list1,m,list2,n,results,paths):
    if m<0 or n<0:
        results.append(paths)
        return
    if bList[m][n]=='b':
        addLcs(bList,list1,m-1,list2,n-1,results,paths)
        paths.append(list1[m])
    elif bList[m][n]=='i':
        addLcs(bList,list1,m-1,list2,n,results,paths)
    elif bList[m][n]=='t':
        pathsTwo=[i for i in paths]
        addLcs(bList,list1,m-1,list2,n,results,paths)
        addLcs(bList,list1,m,list2,n-1,results,pathsTwo)
    else:
        addLcs(bList,list1,m,list2,n-1,results,paths)




results=getLCS('BDCABA','ABCBDAB')
print(results)