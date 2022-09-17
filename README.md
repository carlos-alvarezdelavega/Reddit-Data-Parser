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
def getPushshiftData(after, before, sub):
    url = 'https://api.pushshift.io/reddit/search/submission/?&size=1000&after='+str(after)+'&before='+str(before)+'&subreddit='+str(sub)
    print(url)
    r = requests.get(url)
    data = json.loads(r.text)
    return data['data']
```
### A function that parses sub data
This function will "collect" and organize the desired subReddit data into a list for later conversion into a .csv file.
Using the [Pushshift API parameters](https://pushshift.io/api-parameters/), you can collect much more information than the defined in the function below. 

```python

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
```

### Deifining key variables 

At this point, you will define _key variables_ for the tool to work properly. 

Let's break down the variables below:

* The `sub` variable stores the name of the subReddit from which you want to parse the data as shown in Reddit's unique URL. In the example below, it is the `digitalnomad` subReddit. 
* The `after` variable stores a [unix timestamp](https://www.unixtimestamp.com/), which indicates the exact date after which the data will be retrieved. In the example below, the unix timestamp is set to Junuary 1st, 2019.
* The `before` variable stores another unix timestamp, which indicates the date until which the data will be retrieve. 
    * Think of the `after` and `before` variables as a constrained timeframe from which data will be parsed. 
* The `subCount` and `subStats` variables will be used in a later function to aid the parsing and keeping track of posts retreived. 

```python

sub = "digitalnomad" #The subreddit name as written on its unique URL. For example: https://www.reddit.com/r/digitalnomad
after = "1514764800" #January 1st
before = "1517443200" #February 1st
subCount = 0
subStats = {}
```

### Collecting the data

The data variable calls the `getPushshiftData()` function (which was defined earlier). 
The `while` keyword means that the program will use the defined parameters and loop throught the data storing it a list defined in the `collectSubData()` function. 

```python

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
```
### Getting feedback

The following block of code will "print" on your notebook the following information:

* Number of submissions added to the list
* The name of the first post added to the list
* the name of the last post added to the list

```python
print(str(len(subStats)) + " submissions have added to list")
print("1st entry is:")
print(list(subStats.values())[0][0][1] + " created: " + str(list(subStats.values())[0][0][5]))
print("Last entry is:")
print(list(subStats.values())[-1][0][1] + " created: " + str(list(subStats.values())[-1][0][5]))
```
### Convert to csv file

The `updateSubs_file()` function will convert the retrived list into a csv file that can be opened with Microsoft Excel. 

Look out for the `location`and `filename` variables. These will determine the folder the csv file will be saved and its name. 

Once the list has been compiled, you will receive a message with the number of submissions that have been uploaded. 

```python
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
```

## Feel free to reach out should you have any questions!