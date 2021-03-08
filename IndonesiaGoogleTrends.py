#!/usr/bin/env python
# coding: utf-8

# # Google Trends in Indonesia (2012-2020) 

# This is a curated dataset of Google Trends over the years. Every year, Google releases the trending search queries all over the world in various categories.It has trends from 2001 to 2020
# 

# In[101]:


# Data sourced from https://www.kaggle.com/dhruvildave/google-trends-dataset

import pandas as pd 
import matplotlib as plt

googletrends = pd.read_csv('C:/SyabaruddinFolder/Work/DATA/GoogleTrendsAnalysis/archive/trends.csv')
googletrends.head()


# In[102]:


# Dimension of the dataframe
googletrends.shape


# In[103]:


#Unique values from 'location column'. It shows where are the locations in every trends.

googletrends['location'].value_counts()


# In[104]:


#Unique values from 'year' column. It shows in what year that the trends occured

googletrends['year'].value_counts()


# In[105]:


#Unique values from 'year' column. It shows the terms that the trends in google form 2001 to 2021

googletrends['query'].value_counts()


# In[106]:


#We subset the location to Indonesia. This is to check what trends in Indonesia in Google search during 2001-2020 

indonesia = googletrends[googletrends['location']=='Indonesia']
indonesia = indonesia.loc[:,['year','category','rank','query']]
indonesia


# In[107]:


#data recorded Indonesia only from 2012-2020
indonesia['year'].unique()


# ## Indonesia Top 10 terms in 2012-2020 

# In[108]:


indonesiatop10 = indonesia['query'].value_counts().head(10)
indonesiatop10


# **wow, Our President, Pak 'Jokowi' is the most trending term in 2001-2020!**

# In[109]:


indonesiajokowi = indonesia.loc[:,['year','query','category']].set_index('year')
indonesiajokowi = indonesiajokowi[indonesiajokowi['query']=='Jokowi']
indonesiajokowi


# **So, Our President 'Jokowi' was trending in 2012, 2014, and 2017!**

# ### Indonesia Top Google Trends every year from 2012-2020
# 
# **Below are Top Google trends on each category every year from 2012-2020**

# #### Year 2012

# In[110]:


year2012 = indonesia[indonesia['year']==2012].set_index('year')
year2012 = year2012[year2012['rank']==1]
year2012


# #### Year 2013

# In[111]:


year2013 = indonesia[indonesia['year']==2013].set_index('year')
year2013 = year2013[year2013['rank']==1]
year2013


# #### Year 2014

# In[112]:


year2014 = indonesia[indonesia['year']==2014].set_index('year')
year2014 = year2014[year2014['rank']==1]
year2014


# #### Year 2015

# In[113]:


year2015 = indonesia[indonesia['year']==2015].set_index('year')
year2015 = year2015[year2015['rank']==1]
year2015


# #### Year 2016

# In[114]:


year2016 = indonesia[indonesia['year']==2016].set_index('year')
year2016 = year2016[year2016['rank']==1]
year2016


# #### Year 2017

# In[115]:


year2017 = indonesia[indonesia['year']==2017].set_index('year')
year2017 = year2017[year2017['rank']==1]
year2017


# #### Year 2018

# In[116]:


year2018 = indonesia[indonesia['year']==2018].set_index('year')
year2018 = year2018[year2018['rank']==1]
year2018


# #### Year 2019

# In[117]:


year2019 = indonesia[indonesia['year']==2019].set_index('year')
year2019 = year2019[year2019['rank']==1]
year2019


# #### Year 2020

# In[118]:


year2020 = indonesia[indonesia['year']==2020].set_index('year')
year2020 = year2020[year2020['rank']==1]
year2020

