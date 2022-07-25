# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 13:59:55 2022

@author: Anup Banerjee
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#method1 to read json
json_file = open('loan_data_json.json')
data = json.load(json_file)

#method2 to read json
with open('loan_data_json.json') as json_file:
    data = json.load(json_file)

#it easier to debug and transform data with the 2nd method since there is
#proper indentation and we can include all kind of transformation within the indentation
#code is more readable and clean with "with"

#transforming json data to dataframe
loandata = pd.DataFrame(data)

#finding unique values for column 'purpose'
loandata['purpose'].unique()

#Describing data
loandata.describe()
#Describing a specific column in data
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

#using exp() to get annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annualincome'] = income

#Fico Score

fico = 700
# fico >= 300 and < 400: 'Very Poor'
# fico >= 400 and ficoscore < 600: 'Poor'
# fico >= 601 and ficoscore < 660: 'Fair'
# fico >= 660 and ficoscore < 780: 'Good'
# fico >=780: 'Excellent'

if fico >= 300 and fico < 400:
    ficocat = 'Very Poor'
elif fico >= 400 and fico < 600:
    ficocat = 'Poor'
elif fico >= 601 and fico < 660:
    ficocat = 'Fair'
elif fico >= 660 and fico < 700:
    ficocat = 'Good'
elif fico >= 700:
    ficocat = 'Excellent'
else:
    ficocat = 'Unknown'
print(ficocat)

#applying forloops to loan data

length = len(loandata)
ficocat =[]

for x in range(0,length):
    category = loandata['fico'][x]
    try:      
        if category >=300 and category < 400:
            cat ='Very Poor'
        elif category >=400 and category < 600:
            cat ='Poor'
        elif category >=601 and category < 660:
            cat ='Fair'
        elif category >=660 and category < 700:
            cat ='Good'
        elif category >=700:
            cat ='Excelent'
        else:
            cat = 'Unknown'
    except:
        cat = 'Unknown'
        
    ficocat.append(cat)

ficocat = pd.Series(ficocat)
loandata['fico.category'] = ficocat

#df.loc as conditional statements
#df.loc [df[columnname] condition, newcolumnname] = 'Value if the condition is met'

#for interest rate a new column is required , rate>0.12 then high, else low
loandata.loc[loandata['int.rate'] > 0.12,'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12,'int.rate.type'] = 'Low'

#number of loans/row by fico.category

catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color = 'green', width = 0.2)
plt.show()

purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color = 'red', width = 0.2)
plt.show()

#scatter plots

ypoint = loandata['annualincome']
xpoint = loandata['dti']
plt.scatter(xpoint,ypoint, color = 'blue')
plt.show()

#writing to csv
loandata.to_csv('loan_cleaned.csv',index = True)





















