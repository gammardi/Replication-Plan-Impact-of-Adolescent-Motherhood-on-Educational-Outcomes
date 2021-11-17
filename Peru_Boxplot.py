# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 10:56:05 2021

@author: dirga.muhammad
"""

import seaborn as sns
import pandas as pd
  
#set seaborn style
_ = sns.set(style="whitegrid", palette="colorblind")

# reading data from the xls
file = 'D://S2//MGPS//1 First Semester//Methods_Ji Ma//Datasets//Code//Peru_Cleaned1.xlsx'
Peru_data = pd.read_excel(file)
 
#Generate box plot, assign it as df
df = sns.boxplot(x = 'Teen_Marriage', y ='Final_Years_of_Education', data = Peru_data)

#labeling 
labels = [item.get_text() for item in df.get_xticklabels()]
labels[0] = 'Non Adolescent marriage'
labels[1] = 'Adolescent marriage'
df.set_xticklabels(labels)

