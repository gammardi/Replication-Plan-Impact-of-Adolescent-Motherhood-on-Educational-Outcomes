# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 12:02:12 2021

@author: dirga.muhammad
"""


import statsmodels.api as sm
import pandas as pd
  
# reading data from the xls
file = 'D://S2//MGPS//1 First Semester//Methods_Ji Ma//Datasets//Code//Peru_cleaned1.xlsx'
Peru_data = pd.read_excel(file)
  
# defining the variables
y = Peru_data['Final_Years_of_Education']
x = Peru_data[['Teen_Marriage','Education_Level_(Father)','Education_Level_(Mother)','hh_situ_financial']]
  
# adding the constant term
x = sm.add_constant(x)
  
# performing the regression
# and fitting the model
result = sm.OLS(y, x).fit()
print_result = result.summary()  
# printing the summary table
print(print_result)
#print(result.summary())