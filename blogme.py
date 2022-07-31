# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 21:05:38 2022

@author: Anup Banerjee
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#reading excel /xsls file
data = pd.read_excel('articles.xlsx')

#summary of data
data.describe()

#summary of columns
data.info()

#counting the number of articles per source
data.groupby(['source_id'])['article_id'].count()

#number of reactions received by publishers
data.groupby(['source_id'])['engagement_reaction_count'].sum()

#dropping columns
data =data.drop('engagement_comment_plugin_count', axis = 1)

#creating function with for loop to do sentiment analysis

keyword = 'murder'

def keywordflag(keyword):
    length = len(data)
    keyword_flag =[]
    for x in range (0,length):
        heading = data['title'][x]
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        keyword_flag.append(flag)
    return keyword_flag
keywordflag = keywordflag('murder')
#creating a column in df for jeyword flag
data['keyword_flag'] = pd.Series(keywordflag)

#SentimentIntensityAnalyzer

sent_int = SentimentIntensityAnalyzer()
text = data['title'][15]
sent = sent_int.polarity_scores(text)

neg = sent['neg']
pos = sent['pos']
neu = sent['neu']

#adding for loop to extract sentiment per title

title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []

length = len(data)

for x in range(0,length):
    try:
        text = data['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg = 0
        pos = 0
        neu = 0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)
    
title_neg_sentiment = pd.Series(title_neu_sentiment)
title_pos_sentiment = pd.Series(title_pos_sentiment)
title_neu_sentiment = pd.Series(title_neu_sentiment)

data['title_neg_sentiment'] = title_neg_sentiment
data['title_pos_sentiment'] = title_pos_sentiment
data['title_neu_sentiment'] = title_neu_sentiment

#Writing the data

data.to_excel('blogme_clean.xlsx', sheet_name='blogmedata', index = False)

































           
            
                    