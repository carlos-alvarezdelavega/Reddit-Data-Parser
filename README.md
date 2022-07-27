# About the Pushshift Reddit API Crawler

This code uses the [pushshift.io](https://pushshift.io/) tool and `python` to scrap [Reddit](https://www.reddit.com/) data. This document will walk you through the steps needed to run the code. This repository is meant for low- and no-code experts, hence, I avoid technical jarggon. When run successfully, this code allows you to get Reddit posts and their associated comments within a designated timeframe. You will get this data organized in a .csv file that can be opened Microsoft Excel or Google Sheets. 

## Getting Started

### How do I run Python on my computer?
I *strongly* recommend you download and install [Anaconda](https://www.anaconda.com/)'s [Jupyter Notebook](https://jupyter.org/) to run your `python` code. Jupyter Notebook allows you to break down your code's components, detect, and correct errors easily. It also installs the pre-required programs to run this tool successfully. Check out a guide on [how to install Anaconda and run your Jupyter Notebook](https://sparkbyexamples.com/python/install-anaconda-jupyter-notebook/).

### Python notes to keep in mind
In Python, hashtag '#' symbols represent in-line comments. Comments are lines of code that are *ignored* when running the program. You'll see the code uses these comments to signpost use. Comments are helpful to track the relevant variables you want to manipulate. For example: 

```python
sub = "digitalnomad" #The name of the subreddit as it appears in its URL.
before = "1517443200" #Timestamp for February 1st
after = "1514764800" #Timestamp January 1st
```

## Open your Jupyter Notebook

Head to the folder above. Copy and paste the code into the notebook's cells. Each cell is commented in the code. 

## Breaking Down the Important Lines of Code


