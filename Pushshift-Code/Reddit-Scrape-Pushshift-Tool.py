#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
import json
import csv
import time
import datetime


# In[2]:


def getPushshiftData(after, before, sub):
    url = 'https://api.pushshift.io/reddit/search/submission/?&size=1000&after='+str(after)+'&before='+str(before)+'&subreddit='+str(sub)
    print(url)
    r = requests.get(url)
    data = json.loads(r.text)
    return data['data']


# In[3]:


def collectSubData(subm):
    subData = list() #list to store data points
    title = subm['title']
    body = subm['selftext'] if 'selftext' in subm else ''
    url = subm['url']
    try:
        flair = subm['link_flair_text']
    except KeyError:
        flair = "NaN"    
    author = subm['author']
    sub_id = subm['id']
    score = subm['score']
    created = datetime.datetime.fromtimestamp(subm['created_utc']) #For example, 1520561700.0
    numComms = subm['num_comments']
    permalink = subm['permalink']
    
    subData.append((sub_id,title,body,url,author,score,created,numComms,permalink,flair))
    subStats[sub_id] = subData


# In[4]:


sub = "digitalnomad"
before = "1517443200" #February 1st
after = "1514764800" #January 1st
subCount = 0
subStats = {}


# In[5]:


data = getPushshiftData(after, before, sub)
while len(data) > 0:
    for submission in data:
        collectSubData(submission)
        subCount+=1
    print(len(data))
    print(str(datetime.datetime.fromtimestamp(data[-1]['created_utc'])))
    after = data[-1]['created_utc']
    data = getPushshiftData(after, before, sub)
    
print(len(data))


# In[6]:


print(str(len(subStats)) + " submissions have added to list")
print("1st entry is:")
print(list(subStats.values())[0][0][1] + " created: " + str(list(subStats.values())[0][0][5]))
print("Last entry is:")
print(list(subStats.values())[-1][0][1] + " created: " + str(list(subStats.values())[-1][0][5]))


# In[7]:


def updateSubs_file():
    upload_count = 0
    location = "pushshift-data" #location of file in your computer, that is, the folder's where you want to save the file
    filename = input("example-file") #file's name as it will be saved
    file = location + filename
    with open(file, 'w', newline='', encoding='utf-8') as file: 
        a = csv.writer(file, delimiter=',')
        headers = ["Post ID","Title","Post Body","Url","Author","Score","Publish Date","Total No. of Comments","Permalink","Flair"] #Headers for the csv file's columns
        a.writerow(headers)
        for sub in subStats:
            a.writerow(subStats[sub][0])
            upload_count+=1
            
        print(str(upload_count) + " submissions have been uploaded")
updateSubs_file()


# In[8]:


subStats


# In[ ]:




