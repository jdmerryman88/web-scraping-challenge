#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
from bs4 import BeautifulSoup
from lxml import html
import requests
import pymongo
import pandas as pd
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import time
from pymongo import MongoClient


# In[2]:

def scrape():
# Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)


    # In[3]:


    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(5)
    html = browser.html

    # Create BeautifulSoup object; parse with 'lxml'
    soup = BeautifulSoup(html, 'html.parser')
    #print(soup.prettify())


    # In[58]:


    news_title = soup.find_all('div', class_= "content_title")[1].text
    print(news_title)
    news_p = soup.find('div', class_= "article_teaser_body").text
    print(news_p)


    # In[59]:


    news = {'title' : news_title, 'image_url' : news_p}

    return news 
    # In[6]:

def scrape2():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    
    url2 = 'https://space-facts.com/mars/'


    # In[70]:


    tables = pd.read_html(url2)
    tables


    # In[75]:


    df = tables[0]
    df = df.rename(columns= {0 : "Description", 1 : "Mars" })
    df = df.set_index("Description")
    df.head()


    # In[ ]:





    # In[76]:


    df.to_html('table.html')


    # In[23]:


    # connect to mongo
    mongodb_url = 'mongodb://localhost:27017'
    mongo_client = MongoClient(mongodb_url)


    # In[61]:


    # get handle to mongo db and create collection
    mongo_db = mongo_client.mars_db
    collection = mongo_db.mars
    new = mongo_db.news


    # In[62]:


    url3 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url3)


    # In[63]:


    hemisphere_image_urls= []
    


    # In[64]:


    html = browser.html
    soup3 = BeautifulSoup(html, 'html.parser')
    hemispheres = soup3.find_all('div' , class_='item')

    for hemisphere in hemispheres:
        title= hemisphere.find('h3').text
        search_link = hemisphere.find("a")["href"]  
        complete_link = "https://astrogeology.usgs.gov/" + search_link
        browser.visit(complete_link)
        html = browser.html
        soup3 = BeautifulSoup(html, 'html.parser')
        image_url = soup3.find('li')
        image_url = image_url.find("a")["href"]
        hemisphere_image_urls.append({'title': title, 'image_url':image_url})
        
    #print(hemisphere_image_urls)


    # In[66]:


    # new.insert_one(news)


    # In[51]:


    # collection.insert_many(hemisphere_image_urls)


    # In[60]:


 

    
# In[ ]:





# In[ ]:

    return hemisphere_image_urls


