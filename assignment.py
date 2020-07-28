# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 20:53:00 2020

@author: NIKHIL YADAV
"""


import pandas as pd
data2c = pd.read_csv('D:/cpba/assignments/assignment2/denco.csv')
data2c
#%%
df1=data2c.groupby('custname').size().sort_values(ascending=False).head()
df1
#%%
df2=data2c.groupby('custname')['revenue'].sum().sort_values(ascending=False)
df2
#%%
df3=data2c.groupby('partnum')['revenue'].sum().sort_values(ascending=False)
df3
#%%
df4=data2c.groupby('partnum')['margin'].sum().sort_values(ascending=False)
df4
#%%
df5=data2c.groupby('custname')['margin'].sum().sort_values(ascending=False)
df5
#%%
writer = pd.ExcelWriter('assignment.xlsx', engine='xlsxwriter')
df1.to_excel(writer, sheet_name='sheet1')
df2.to_excel(writer, sheet_name='sheet2')
df3.to_excel(writer, sheet_name='sheet3')
df4.to_excel(writer, sheet_name='sheet4')
df5.to_excel(writer, sheet_name='sheet5')
writer.save()
