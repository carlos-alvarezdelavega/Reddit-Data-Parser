# About the Pushshift Reddit API Crawler

This code tool uses the [pushshift.io](https://pushshift.io/) and `python` to scrap [Reddit](https://www.reddit.com/) data. This document will walk you through the steps needed to run the code. This repository is meant for low- and no-code researchers (like me!), hence, I don't go into great detail about the technicalities of the program. When run successfully, this code allows you to get Reddit posts and their associated comments within a designated timeframe. You will get this data organized in a .csv file that can be opened on Microsoft Excel or Google Sheets. [Read more about the Pushshift API](https://github.com/pushshift/api).

## Getting Started

### Running Python on your computer
I *strongly* recommend you download and install [Anaconda](https://www.anaconda.com/) and use [Jupyter Notebook](https://jupyter.org/) to run your `python` code. Jupyter Notebook allows you to break down your code's components, detect, and correct errors easily. It also installs the pre-required libraries to run this tool successfully. Check out a guide on [how to install Anaconda and run your Jupyter Notebook](https://sparkbyexamples.com/python/install-anaconda-jupyter-notebook/).

### Python notes to keep in mind
In Python, hashtag '#' symbols represent in-line comments. Comments are lines of code that are _ignored_ when running the program. You'll see the tool uses comments to signpost key components. Also, comments are helpful to track the relevant variables you want to manipulate. For example: 

```python
sub = "digitalnomad" #The name of the subreddit as it appears in its URL, in this case, https://www.reddit.com/r/digitalnomad/
before = "1517443200" #Timestamp for February 1st
after = "1514764800" #Timestamp January 1st
```

## Using the Tool

### Head to your Jupyter Notebook

Once you've opened your new Jupyter Notebook, head to the folder above. Copy and paste the code into the notebook's cells. Each cell is commented in the code. 

## Code Overview

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

### Defining the PushshiftData function

A function is a block of code which only runs when it is called. In python, functions are defined with the `def` term.

You can pass data, known as parameters, into a function. This function below sets up the Pushshift URL to get the Reddit data from, its parameters are `after`, `before`, `sub` (you will provide these parameters later). 

```python
# In[2]:

def getPushshiftData(after, before, sub):
    url = 'https://api.pushshift.io/reddit/search/submission/?&size=1000&after='+str(after)+'&before='+str(before)+'&subreddit='+str(sub)
    print(url)
    r = requests.get(url)
    data = json.loads(r.text)
    return data['data']
```
### Deifining key variables 

At this point, you will define _key variables_ for the tool to work properly. 

Let's break down the variables below:

*The `sub` variable stores the name of the subReddit from which you want to parse the data as shown in Reddit's unique URL. In the example below, it is the `digitalnomad` subReddit. 
*The `after` variable stores a [unix timestamp](https://www.unixtimestamp.com/), which indicates the exact date after which the data will be retrieved. In the example below, the unix timestamp is set to Junuary 1st, 2019.
*The `before` variable stores another unix timestamp, which indicates the date until which the data will be retrieve. 
    *Think of the `after` and `before` variables as a constrained timeframe from which data will be parsed. 
*The `subCount` and `subStats` variables will be used in a later function to aid the parsing and keeping track of posts retreived. 

```python
# In[4]:

sub = "digitalnomad" #The subreddit name as written on its unique URL. For example: https://www.reddit.com/r/digitalnomad
after = "1514764800" #January 1st
before = "1517443200" #February 1st
subCount = 0
subStats = {}
```
## Feel free to reach out should you have any questions!