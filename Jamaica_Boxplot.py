# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import seaborn as sns
import pandas as pd

#set seaborn style
_ = sns.set(style="whitegrid", palette="colorblind")

# reading data from the xls
file = 'D://S2//MGPS//1 First Semester//Methods_Ji Ma//Datasets//Code//Jamaica_cleaned2.xlsx'
Jamaica_data = pd.read_excel(file)
  
#Generate box plot, assign it as ax
ax = sns.boxplot(x = 'Teen_Marital_Union', y ='Yrs_Edu', data = Jamaica_data)

labels = [item.get_text() for item in ax.get_xticklabels()]
labels[0] = 'Non Adolescent marriage'
labels[1] = 'Adolescent marriage'
ax.set_xticklabels(labels)

