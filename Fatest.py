#%%
def Fbi(n):
    if n<=1:
        return 1 if n==1 else 0
    else:
        return Fbi(n-1)+Fbi(n-2)


Fbi(10)

m=[1,2,3]
m.pop()
m
import queue
#最多接受10个数据
q=queue.Queue(10)
q.put(10)  //进队

q.qsize()
q.get() # 取出最前面的一个数据
