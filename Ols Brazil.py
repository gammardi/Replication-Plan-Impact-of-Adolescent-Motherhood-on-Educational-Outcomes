# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 17:43:58 2021

@author: dirga.muhammad
"""

import statsmodels.api as sm
import pandas as pd
  
# reading data from the xls
file = 'D://S2//MGPS//1 First Semester//Methods_Ji Ma//Datasets//Code//Brazil_clean2.xlsx'
Brazil_data = pd.read_excel(file)
  
# defining the variables
x = Brazil_data['Total_Years_of_Education'].tolist()
y = Brazil_data['Teen_Marital_Union'].tolist()
  
# adding the constant term
x = sm.add_constant(x)
  
# performing the regression
# and fitting the model
result = sm.OLS(y, x).fit()
  
# printing the summary table
print(result.summary())