#%%
def dpFibonacci(n):
    if n<2:
        return n
    one,two=0,1
    for i in range(2,n+1):
        result=one+two
        one,two=two,result
    return result


dpFibonacci(6)