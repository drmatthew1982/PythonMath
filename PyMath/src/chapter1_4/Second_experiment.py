'''
Created on Dec 8, 2019

@author: matthew.yiqing.zhu
'''
from scipy.stats import binom
import matplotlib.pyplot as plt
import seaborn
seaborn.set()

fig, ax = plt.subplots(3,1)
params = [(10,0.25), (10,0.5),(10,0.75)]
x=range(0,11)
for i in range(len(params)):
    binom_rv=binom(n=params[i][0],p=params[i][1])
    rvs=binom_rv.rvs(size=1000000)
    ax[i].hist(rvs,bins=11, normed=True)
    ax[i].set_title('n={},p={}'.format(params[i][0],params[i][1]))
    ax[i].set_xlim(0,10)
    ax[i].set_ylim(0,0.4)
    ax[i].set_xticks(x) 
    print('rvs{}:{}'.format(i,rvs))
plt.show()
    