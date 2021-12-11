# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 12:24:13 2021

@author: dirga.muhammad
"""

import statsmodels.api as sm
import pandas as pd
  
# reading data from the xls
file = 'D://S2//MGPS//1 First Semester//Methods_Ji Ma//Datasets//Code//Vietnam_clean3.xlsx'
Vietnam_data = pd.read_excel(file)
  
# defining the variables
y = Vietnam_data['Year_of_Education']
x = Vietnam_data[['Teen_Marital_Union','age','Area','Fathers_edu','Mothers_edu','hh_situ_financial']]
  
# adding the constant term
x = sm.add_constant(x)
  
# performing the regression
# and fitting the model
result = sm.OLS(y, x).fit()
print_result = result.summary()  
# printing the summary table
print(print_result)
#print(result.summary())