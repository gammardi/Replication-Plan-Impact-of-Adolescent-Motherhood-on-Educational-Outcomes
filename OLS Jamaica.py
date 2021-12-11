# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 09:55:36 2021

@author: dirga.muhammad
"""

import statsmodels.api as sm
import pandas as pd
  
# reading data from the xls
file = 'D://S2//MGPS//1 First Semester//Methods_Ji Ma//Datasets//Code//Jamaica_cleaned2.xlsx'
Jamaica_data = pd.read_excel(file)
  
# defining the variables
y = Jamaica_data['Yrs_Edu']
x = Jamaica_data[['Teen_Marital_Union','hh_situ_financial','Fathers_edu','Mothers_edu']]
  
# adding the constant term
x = sm.add_constant(x)
  
# performing the regression
# and fitting the model
result = sm.OLS(y, x).fit()
print_result = result.summary()  
# printing the summary table
print(print_result)
#print(result.summary())