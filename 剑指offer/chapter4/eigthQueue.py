#%%
from itertools import permutations
cols=range(8)
for vec in permutations(cols):
    if (8==len(set(vec[i]+i for i in cols))==len(set(vec[i]-i for i in cols))):
        print(vec)