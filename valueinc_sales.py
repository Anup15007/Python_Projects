# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 16:34:15 2022

@author: Anup Banerjee
"""

import pandas as pd

#file_name = pd.read_csv('file.csv') <---- format to read csv
data = pd.read_csv('transaction.csv',sep=';')
#data summary

data.info()
#Calculations
CostPerItem= 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

ProfitPerItem = SellingPricePerItem - CostPerItem

CostPerTransaction = NumberOfItemsPurchased * CostPerItem
SellingPricePerTransaction = NumberOfItemsPurchased * SellingPricePerItem
ProfitPerTransaction = NumberOfItemsPurchased * ProfitPerItem

#CostPerTransaction column calucalation
#Calculating for the entire column
#variable = DataFrame['ColumnName']

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = NumberOfItemsPurchased * CostPerItem


# adding new column to DataFrame
data['CostPerTransaction'] = CostPerTransaction
# Alternate method
data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

data['SellingPricePerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

# Profit per transaction and Markup

data['ProfitPerTransaction'] = data['SellingPricePerTransaction'] - data['CostPerTransaction']
#Markup = (Cost - Sales)/Cost
data['MarkUp'] = (data['SellingPricePerTransaction'] - data['CostPerTransaction'])/data['CostPerTransaction']

data['MarkUp'] = data['ProfitPerTransaction']/data['CostPerTransaction']

#Rounding Markup and adding it back to Data Frame
data['MarkUp'] = round(data['MarkUp'],2)

#Combining data fields
my_data = 'Anup' + ' Banerjee'

#We can only combine data fields having same data type
# checking data type for day,month,year
print(data['Day'].dtype)

#Converting int day type to string
day = data['Day'].astype(str)
print(day.dtype)

year = data['Year'].astype(str)
print(year.dtype)
my_date = day + '-'+data['Month'] + '-' + year
data['date'] = my_date

#using iloc to view specific columns/rows
data.iloc[0] #brings in row with 0th index
data.iloc[0:3] #brings in row 0 to 3
data.iloc[-5]  #brings in last 5 rows
data.iloc[:,2]  #bring in all rows and 2nd column
data.iloc[4,2]  #brings in 4th row and 2nd column


data.head(5) #brings 1st 5 rows

#using split to split the client_keywords field
#new_var = column.str.split('sep',expand = True)

split_col = data['ClientKeywords'].str.split(',', expand = True)

# creating new columns for the split columns in client_keywords

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

#using the replace function
data['ClientAge'] = data['ClientAge'].str.replace('[','')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']','')


#Using lower case function to change Item description to lower case

data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files
#bringing in new dataset

seasons = pd.read_csv('value_inc_seasons.csv',sep =';')
seasons.info()

#merging files: merge_df = pd.merge(dfOld,dfNew, on='key')
data = pd.merge(data, seasons, on='Month')

#dropping columns

#df =df.drop('columnname', axis=1)# axis = 1/0,1 represents column & 0 represents row
data.info()
data = data.drop('ClientKeywords', axis=1)
#dropping multiple columns
data = data.drop(['Day','Month','Year'], axis=1)

#Export into CSV
data.to_csv('Value_Inc_Cleaned.csv', index=False)# Keeping index false since we have othe unique Identifiers for row

































