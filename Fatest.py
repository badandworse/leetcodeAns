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


#master-project test
'''
#%%
import pandas as pd
from pandas import DataFrame
filepath='c:/Users/xg302/git/leetcodeAns/data/'
person_dt=pd.read_csv('c:/Users/xg302/git/leetcodeAns/data/'+u'person.csv')
person_dt.info()
team_dt=pd.read_csv('c:/Users/xg302/git/leetcodeAns/data/'+'team.csv')
team_dt.info()
all_dt=pd.merge(team_dt,person_dt)
all_dt.info()

#%%
b_vec=[0.028235,0.015572,-0.092471,0.008351,-0.021592,0.006925,0.044534,0.500174,0.02177,-0.139065]
G_vec=[0.008839, 0.130610, 0.113353]

anti_pro_test=0.7688+b_vec[0]*all_dt['Gender_L9_1']+b_vec[1]*all_dt['Age_L9_2']+b_vec[2]*all_dt['Education_L9_3']
+b_vec[3]*all_dt['Position_L9_4']+b_vec[4]*all_dt['Income_L9_5']+b_vec[5]*all_dt['Industry']+b_vec[6]*all_dt['NC_M8_7']+0.0218*all_dt['formal_gap']+0.5002*all_dt['threat']-0.1391*all_dt['informal_gal']+4

from scipy import stats

stats.ks_2samp(anti_pro_test,all_dt['anti_pro'])
#%%
anti_pro_test.to_csv('anti_pro.csv')
person_dt.to_csv(filepath+'123.csv')
#%%

b_vec2=[0.249661,0.003496,-0.97518,-0.037869,0.019195,0.029339,0.089867,-0.62360]
G_vec2=[0.008839,0.130610,0.113353]
thread_test=2.8671+b_vec2[0]*all_dt['Gender_L9_1']+b_vec2[1]*all_dt['Age_L9_2']+b_vec2[2]*all_dt['Education_L9_3']
+b_vec2[3]*all_dt['Position_L9_4']+b_vec2[4]*all_dt['Income_L9_5']+b_vec2[5]*all_dt['Industry']+b_vec2[6]*all_dt['NC_M8_7']
+b_vec2[7]*all_dt['formal_gap']+G_vec[0]*all_dt['check']+G_vec[1]*all_dt['diff']+G_vec[2]*all_dt['diff_check']
-0.0729*all_dt['informal_gal']
-0.1118*all_dt['informal_gal']*all_dt['check']
-0.6184*all_dt['informal_gal']*all_dt['diff']
+0.1354*all_dt['informal_gal']*all_dt['check']*all_dt['diff']
stats.ks_2samp(thread_test,all_dt['threat'])
#%%
thread_test.to_csv('threat.csv')
'''