# About the Pushshift Reddit API Crawler

This code tool uses [pushshift.io](https://pushshift.io/) and `python` to crawl [Reddit](https://www.reddit.com/) data from defined dates. This document will walk you through the steps needed to run the code. This repository is meant for low- and no-code researchers, hence, I've avoided technical jarggon. When run successfully, this code allows you to crawl Reddit posts and their associated comments within a designated timeframe (unlike other tools, such as [PRAW](https://praw.readthedocs.io/en/stable/) that crawl latest or popular posts). You will get this data organized in a .csv file that can be opened on Microsoft Excel or Google Sheets. [Read more about the Pushshift API](https://github.com/pushshift/api).

## Getting Started

### Running Python on your computer
I *strongly* recommend you download and install [Anaconda](https://www.anaconda.com/) and use [Jupyter Notebook](https://jupyter.org/) to run your `python` code. Jupyter Notebook allows you to break down your code's components, detect, and correct errors easily. It also installs the pre-required libraries to run this tool successfully. Check out a guide on [how to install Anaconda and run your Jupyter Notebook](https://sparkbyexamples.com/python/install-anaconda-jupyter-notebook/).

### Python notes to keep in mind
In Python, hashtag '#' symbols represent in-line comments. Comments are lines of code that are *ignored* when running the program. You'll see the tool uses these comments to signpost key components. Comments are helpful to track the relevant variables you want to manipulate. For example: 

```python
sub = "digitalnomad" #The name of the subreddit as it appears in its URL, in this case, https://www.reddit.com/r/digitalnomad/
before = "1517443200" #Timestamp for February 1st
after = "1514764800" #Timestamp January 1st
```

## Using the Tool

### Head to your Jupyter Notebook

Once you've opened your new Jupyter Notebook, head to the folder above. Copy and paste the code into the notebook's cells. Each cell is commented in the code. 

## Tool's Components

### Import libraries

These commands will import the required libraries to run the program. 

```python
# In[1]:

import pandas as pd
import requests
import json
import csv
import time
import datetime
```

### Defining the timeframe function

A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function. This function sets up the Pushshift URL to get the Reddit data from. 

```python
# In[2]:

def getPushshiftData(after, before, sub):
    url = 'https://api.pushshift.io/reddit/search/submission/?&size=1000&after='+str(after)+'&before='+str(before)+'&subreddit='+str(sub)
    print(url)
    r = requests.get(url)
    data = json.loads(r.text)
    return data['data']
```
