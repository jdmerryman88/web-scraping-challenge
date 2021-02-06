#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo
import pandas as pd


# In[3]:


# URL of page to be scraped
url = 'https://mars.nasa.gov/news/'

# Retrieve page with the requests module
response = requests.get(url)
# Create BeautifulSoup object; parse with 'lxml'
soup = BeautifulSoup(response.text, 'lxml')
#print(soup.prettify())


# In[10]:


news_title = soup.find_all('div', class_='content_title')[0].text
print(news_title)
# news_p = soup.find_all('div', class_='article_teaser_body')[0].text
# print(news_p)


# In[14]:


news_synopsis = soup.find("div", class_="rollover_description_inner").text
print(news_synopsis)


# In[5]:


url2 = 'https://space-facts.com/mars/'


# In[6]:


tables = pd.read_html(url2)
tables


# In[7]:


df = tables[0]
df.head()


# In[8]:


df.to_html('table.html')


# In[ ]:





# In[ ]:




