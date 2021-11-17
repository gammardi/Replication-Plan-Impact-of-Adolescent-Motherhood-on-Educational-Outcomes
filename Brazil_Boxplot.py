# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 11:00:35 2021

@author: dirga.muhammad
"""

import seaborn as sns
import pandas as pd
  
#set seaborn style
_ = sns.set(style="whitegrid", palette="colorblind")

# reading data from the xls
file = 'D://S2//MGPS//1 First Semester//Methods_Ji Ma//Datasets//Code//Brazil_clean2.xlsx'
Brazil_data = pd.read_excel(file)
  
#Generate box plot, assign it as df
ax = sns.boxplot(x = 'Teen_Marital_Union', y ='Total_Years_of_Education', data = Brazil_data)

#labeling 
labels = [item.get_text() for item in ax.get_xticklabels()]
labels[0] = 'Non Adolescent marriage'
labels[1] = 'Adolescent marriage'
ax.set_xticklabels(labels)