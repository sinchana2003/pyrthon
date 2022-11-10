# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 21:16:20 2022

@author: SPTINT-09
"""
import pandas as pd
df=pd.DataFrame([[10,20,30,40],[50,60,70,80]])
print(df)

df=pd.DataFrame([[10,20,30,40],
                 [50,60,70,80],
                 [22,33,44]],
                 columns={'maths','kannada','engg','science'})
print(df.maths.agg(['sum','min','max']))
print(df.sum())
print(df.maths.sum())
print(df.agg(['sum','min','max']))
print(df.engg.sum(axis=0))
print(df.maths.agg(['sum','min','max']))


print(pd.pivot_table(df, index = ["maths"]))
