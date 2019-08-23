# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 13:00:33 2019

@author: dhirp
"""
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

df_12 = pd.read_csv('16mminfo.txt',sep='\s*\n')

firstword = df_12.apply(lambda x: x.str.split().str[0:12])

# Create the actual dataset with the necessary colums 'msgid','nsavetime','msg1','msg2'
mm_dataset = pd.DataFrame()


'''for i in range(len(firstword)):
    mm_dataset = mm_dataset.append(pd.DataFrame({'ssid':firstword.iloc[i][0][0],'name':firstword.iloc[i][0][1],'start_time':firstword.iloc[i][0][4],'end_time':firstword.iloc[i][0][5],'volume':firstword.iloc[i][0][6],'pool':firstword.iloc[i][0][7],'size':firstword.iloc[i][0][9],'level':firstword.iloc[i][0][11]}, index=[0]),ignore_index=True)


mm_dataset[['ssid','name']] = firstword'''

for i in range(len(firstword)):
    mm_dataset = mm_dataset.append(pd.DataFrame({'ssid':firstword.iloc[i][0][0],'name':firstword.iloc[i][0][1],'start_time':firstword.iloc[i][0][3],'end_time':firstword.iloc[i][0][5],'volume':firstword.iloc[i][0][6],'pool':firstword.iloc[i][0][7],'size':firstword.iloc[i][0][8],'unit':firstword.iloc[i][0][9]},index=[0]),ignore_index=True)

mm_dataset['start_time'] = pd.to_datetime(mm_dataset.start_time)
mm_dataset['end_time']= pd.to_datetime(mm_dataset.end_time)

# Calculate delata

mm_dataset['backup_time'] = mm_dataset['end_time'] - mm_dataset['start_time']
mm_dataset['backup_time']=mm_dataset['backup_time']/np.timedelta64(1,'s')

mm_dataset.to_excel('16mminfo_a.xls')
# Compare the timings and Size

12_mm = pd.read_excel('12mminfo_a.xls')